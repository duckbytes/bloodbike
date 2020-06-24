from functools import reduce

import phonenumbers
from marshmallow import ValidationError, pre_dump, post_dump, post_load, EXCLUDE, fields, validates, validate, pre_load
from phonenumbers import NumberParseException

from app.exceptions import ObjectNotFoundError
from marshmallow_sqlalchemy import field_for
from app import models, ma, flask_version
from app.utilities import get_object, calculate_tasks_etag, get_all_objects


class TimesMixin:
    time_created = ma.DateTime()
    time_modified = ma.DateTime(dump_only=True)


class DeleteFilterMixin:
    @pre_dump(pass_many=True)
    def filter_deleted(self, data, many):
        if many:
            return list(filter(lambda t: not t.flagged_for_deletion, data))
        else:
            if data.flagged_for_deletion:
                raise ObjectNotFoundError
            else:
                return data


class PostLoadMixin:
    @post_load
    def load_into_object(self, data, many, partial):
        if self.instance:
            for key, value in data.items():
                setattr(self.instance, key, value)
            return self.instance
        else:
            return self.Meta.model(**data)


class ServerSettingsSchema(ma.SQLAlchemySchema, TimesMixin, PostLoadMixin):
    class Meta:
        model = models.ServerSettings
        fields = ('organisation_name', 'image_url',
                  'version', 'hostname', 'favicon', 'locale',
                  'locale_id')

    locale = ma.Nested('LocaleSchema', dump_only=True, exclude=('id',))


class LocaleSchema(ma.SQLAlchemySchema, PostLoadMixin):
    class Meta:
        model = models.Locale
        fields = ('label', 'id', 'code')


class CommentSchema(ma.SQLAlchemySchema, TimesMixin, DeleteFilterMixin, PostLoadMixin):
    class Meta:
        unknown = EXCLUDE
        model = models.Comment
        fields = ('uuid', 'body', 'author', 'parent_uuid', 'author_uuid',
                  "time_created", "time_modified", "publicly_visible")

    author = ma.Nested(
        'UserSchema', dump_only=True,
        exclude=('username', 'address', 'password', 'name', 'email',
                 'dob', 'patch', 'roles', 'comments', 'assigned_vehicles', 'patch_id',
                 "time_created", "time_modified"))



class DeliverableTypeSchema(ma.SQLAlchemySchema, TimesMixin, PostLoadMixin):
    class Meta:
        model = models.DeliverableType
        fields = ('id', 'label')


class DeliverableSchema(ma.SQLAlchemySchema, TimesMixin, DeleteFilterMixin, PostLoadMixin):
    class Meta:
        unknown = EXCLUDE
        model = models.Deliverable
        fields = ('uuid', 'task_uuid', 'comments', 'type', 'type_id',
                  "time_created", "time_modified")

    comments = ma.Nested(CommentSchema, dump_only=True, many=True)
    type = fields.Pluck(DeliverableTypeSchema, "label", dump_only=True)


class AddressSchema(ma.SQLAlchemySchema, PostLoadMixin):
    class Meta:
        model = models.Address

        fields = ('ward', 'line1', 'line2', 'town',
                  'county', 'country', 'postcode',
                  'what3words')

    ward = ma.Str(allow_none=True)
    line1 = ma.Str(allow_none=True)
    line2 = ma.Str(allow_none=True)
    town = ma.Str(allow_none=True)
    county = ma.Str(allow_none=True)
    country = ma.Str(allow_none=True)
    postcode = ma.Str(allow_none=True)
    what3words = ma.Str(allow_none=True)


class PatchSchema(ma.SQLAlchemySchema, PostLoadMixin):
    class Meta:
        model = models.Patch
        fields = ('id', 'label')


class UserSchema(ma.SQLAlchemySchema, TimesMixin, DeleteFilterMixin, PostLoadMixin):
    class Meta:
        unknown = EXCLUDE
        model = models.User
        fields = ('uuid', 'username', 'address', 'password', 'name', 'email',
                  'dob', 'patch', 'roles', 'comments', 'display_name',
                  'assigned_vehicles', 'patch_id', 'contact_number',
                  'time_created', 'time_modified', 'links')

    username = ma.Str(required=True)
    email = ma.Email()
    dob = ma.DateTime(format='%d/%m/%Y')
    address = ma.Nested(AddressSchema)
    uuid = field_for(models.User, 'uuid', dump_only=True)
    assigned_vehicles = ma.Nested("VehicleSchema", many=True, dump_only=True, exclude=("assigned_user",))
    comments = ma.Nested(CommentSchema, dump_only=True, many=True)
    password = ma.Str(load_only=True)

    links = ma.Hyperlinks(
        {"self": ma.URLFor("user", user_id="<uuid>"), "collection": ma.URLFor("users")}
    )

    patch = fields.Pluck(PatchSchema, "label", dump_only=True)

    @validates("display_name")
    def check_display_name_unique(self, value):
        users = get_all_objects(models.Objects.USER)
        if any(list(filter(lambda u: u.display_name == value, users))):
            raise ValidationError("This display name is already taken.")

    @validates("username")
    def check_username_unique(self, value):
        users = get_all_objects(models.Objects.USER)
        if any(list(filter(lambda u: u.username == value, users))):
            raise ValidationError("This username is already taken.")

    @pre_dump
    def get_tasks_etag(self, data, many):
        return data
        if not many:
            data.tasks_etag = calculate_tasks_etag(data.tasks)
        return data

    @post_dump
    def split_roles(self, data, many):
        try:
            data['roles'] = data['roles'].split(",")
        except KeyError:
            return data
        return data


class VehicleSchema(ma.SQLAlchemySchema, TimesMixin, DeleteFilterMixin, PostLoadMixin):
    class Meta:
        unknown = EXCLUDE
        model = models.Vehicle
        fields = ('uuid', 'manufacturer', 'model', 'date_of_manufacture', 'date_of_registration',
                  'registration_number', 'comments', 'links', 'name', 'assigned_user', 'assigned_user_uuid',
                  "time_created", "time_modified")

    date_of_manufacture = ma.DateTime(format='%d/%m/%Y')
    date_of_registration = ma.DateTime(format='%d/%m/%Y')
    assigned_user = ma.Nested(UserSchema, dump_only=True)
    assigned_user_uuid = ma.String(allow_none=True)
    comments = ma.Nested(CommentSchema, dump_only=True, many=True)
    uuid = ma.String(dump_only=True)

    links = ma.Hyperlinks({
        'self': ma.URLFor('vehicle_detail', vehicle_id='<uuid>'),
        'collection': ma.URLFor('vehicle_list')
    }, dump_only=True)


class PrioritySchema(ma.SQLAlchemySchema, PostLoadMixin):
    class Meta:
        model = models.Priority
        fields = ('id', 'label')


def display_names_reducer(result, user):
    if user[0] == 0:
        return result + user[1].display_name
    else:
        return result + ", {}".format(user[1].display_name)


class TaskSchema(ma.SQLAlchemySchema, TimesMixin, DeleteFilterMixin, PostLoadMixin):
    class Meta:
        unknown = EXCLUDE
        model = models.Task
        fields = ('uuid', 'pickup_address', 'dropoff_address', 'patch', 'patch_id', 'contact_name',
                  'contact_number', 'priority', 'session_uuid', 'time_of_call', 'deliverables',
                  'comments', 'links', 'assigned_rider', 'time_picked_up', 'time_dropped_off', 'rider',
                  'priority_id', 'time_cancelled', 'time_rejected', "patient_name", "patient_contact_number",
                  "destination_contact_number", "destination_contact_name",
                  "time_created", "time_modified", "assigned_users", "assigned_users_display_string")

    pickup_address = ma.Nested(AddressSchema)
    dropoff_address = ma.Nested(AddressSchema)
    rider = ma.Nested(UserSchema, exclude=('uuid', 'address', 'password', 'email', 'dob', 'roles', 'comments'),
                      dump_only=True)
    assigned_users = ma.Nested(UserSchema,
                               exclude=('address', 'password', 'email', 'dob', 'roles', 'comments'),
                               many=True, dump_only=True)
    deliverables = ma.Nested(DeliverableSchema, many=True)
    comments = ma.Nested(CommentSchema, dump_only=True, many=True)
    time_picked_up = ma.DateTime(allow_none=True)
    time_dropped_off = ma.DateTime(allow_none=True)
    time_cancelled = ma.DateTime(allow_none=True)
    time_rejected = ma.DateTime(allow_none=True)
    priority = fields.Pluck(PrioritySchema, "label", dump_only=True)
    patch = fields.Pluck(PatchSchema, "label", dump_only=True)
    time_of_call = ma.DateTime()
    assigned_users_display_string = ma.String(dump_only=True)

    links = ma.Hyperlinks({
        'self': ma.URLFor('task_detail', task_id='<uuid>'),
        'collection': ma.URLFor('tasks_list')
    })

    @pre_dump
    def concatenate_assigned_users_display_string(self, data, many):
        data.assigned_users_display_string = reduce(display_names_reducer, enumerate(data.assigned_users), "")
        return data

    @validates("contact_number")
    def contact_number(self, value):
        validate_tel_number(value)
        return
        # TODO: see if this is a better way to do things
        if not value:
            return
        try:
            phonenumbers.parse(value)
        except NumberParseException:
            raise
            raise ValidationError("Not a valid telephone number.")

    @validates("patient_contact_number")
    def patient_contact_number(self, value):
        validate_tel_number(value)

    @validates("destination_contact_number")
    def destination_contact_number(self, value):
        validate_tel_number(value)


def validate_tel_number(value):
    if not value:
        return
    split_list = list(value)
    if len(list((filter(lambda n: n == "+", split_list)))) > 1:
        raise ValidationError("Not a valid telephone number.")
    if "+" in split_list and split_list[0] != "+":
        raise ValidationError("Not a valid telephone number.")
    if any(list(filter(int_check, split_list))):
        raise ValidationError("Not a valid telephone number.")


def int_check(value):
    if value == "+" or value == " ":
        return False
    try:
        int(value)
    except ValueError:
        return True
    return False


class UserUsernameSchema(ma.SQLAlchemySchema):
    class Meta:
        model = models.User
        fields = ('uuid', 'username')

    username = ma.Str(required=True)


class UserAddressSchema(ma.SQLAlchemySchema):
    class Meta:
        model = models.User
        fields = ('uuid', 'name', 'address')

    postcode = ma.Function(lambda obj: obj.postcode.upper())
    address = ma.Nested(AddressSchema, exclude=("ward",))


class SessionSchema(ma.SQLAlchemySchema, TimesMixin, DeleteFilterMixin, PostLoadMixin):
    class Meta:
        unknown = EXCLUDE
        model = models.Session
        fields = ('uuid', 'coordinator_uuid',
                  'time_created', 'tasks', 'comments',
                  'links', 'task_count', 'last_active',
                  'time_created', 'time_modified', 'tasks_etag',
                  'collaborators')

    tasks = ma.Nested(TaskSchema, dump_only=True, many=True,
                      exclude=('comments', 'deliverables'))
    comments = ma.Nested(CommentSchema, dump_only=True, many=True)
    collaborators = ma.Nested(UserSchema, dump_only=True, many=True, exclude=(
        "address",
        "time_created",
        "dob",
        "username",
        "patch",
        "contact_number",
        "email",
        "assigned_vehicles",
        "comments",
        "patch_id",
        "time_modified",
        "roles",
        "name"))

    links = ma.Hyperlinks({
        'self': ma.URLFor('session_detail', session_id='<uuid>'),
        'collection': ma.URLFor('sessions_list')
    })

    @pre_dump
    def get_last_active(self, data, many):
        session = get_object(models.Objects.SESSION, data.uuid)
        tasks_plus_deleted = session.tasks.all()
        last_changed_task = sorted(tasks_plus_deleted, key=lambda t: t.time_modified)
        data.last_active = last_changed_task[-1].time_modified if last_changed_task else session.time_modified
        return data

    @pre_dump
    def get_tasks_etag(self, data, many):
        data.tasks_etag = calculate_tasks_etag(data.tasks.all())
        return data


class LocationSchema(ma.SQLAlchemySchema, TimesMixin, DeleteFilterMixin, PostLoadMixin):
    class Meta:
        model = models.Location
        fields = ('uuid', 'name', 'contact_name', 'contact_number', 'address', 'comments', 'links',
                  "time_created", "time_modified")

    comments = ma.Nested(CommentSchema, dump_only=True, many=True)
    address = ma.Nested(AddressSchema)

    links = ma.Hyperlinks({
        'self': ma.URLFor('location_detail', location_id='<uuid>'),
        'collection': ma.URLFor('location_list')
    })


class SearchSchema():
    class Meta:
        fields = ('query', 'type', 'page')
