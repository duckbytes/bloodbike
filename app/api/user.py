from flask import jsonify
from marshmallow import ValidationError
from sqlalchemy import exc as sqlexc
from app import schemas, db, models
from app import user_ns as ns
from app import root_ns
from flask_restx import Resource
import flask_praetorian
from app.api.functions.viewfunctions import load_request_into_object
from app.api.functions.userfunctions import get_user_object_by_int_id, user_id_match_or_admin
from app.api.functions.errors import not_found, schema_validation_error, not_unique_error, forbidden_error, \
    internal_error, already_flagged_for_deletion_error
from app.exceptions import ObjectNotFoundError, SchemaValidationError, InvalidRangeError, AlreadyFlaggedForDeletionError
from app.utilities import add_item_to_delete_queue, get_object, get_all_objects, get_range, \
    remove_item_from_delete_queue
from app import guard
from flask_praetorian import utilities as prae_util

USER = models.Objects.USER
DELETE_FLAG = models.Objects.DELETE_FLAG

user_dump_schema = schemas.UserSchema(exclude=("password",))
user_schema = schemas.UserSchema()
users_schema = schemas.UserSchema(
    exclude=("address",
             "dob",
             "email",
             "password",))
address_schema = schemas.AddressSchema()
user_username_schema = schemas.UserSchema(exclude=("address",
                                                   "dob",
                                                   "email",
                                                   "password",
                                                   "name",
                                                   "roles",
                                                   "patch",
                                                   "links",
                                                   ))
user_address_schema = schemas.UserSchema(exclude=("username",
                                                   "dob",
                                                   "email",
                                                   "password",
                                                   "name",
                                                   "roles",
                                                   "patch",
                                                   "links",
                                                   ))
tasks_schema = schemas.TaskSchema(many=True)


@root_ns.route(
    '/whoami',
    endpoint='myself')
class Myself(Resource):
    @flask_praetorian.auth_required
    def get(self):
        jwt_details = flask_praetorian.utilities.get_jwt_data_from_app_context()
        try:
            user = get_user_object_by_int_id(prae_util.current_user_id())
        except ObjectNotFoundError:
            return not_found(USER, None)
        result = user_dump_schema.dump(user)
        result['login_expiry'] = jwt_details['rf_exp'] if jwt_details else None
        return jsonify(result)

@ns.route('/<user_id>/restore', endpoint="user_undelete")
class UserRestore(Resource):
    @flask_praetorian.roles_accepted("admin", "coordinator")
    def put(self, user_id):
        try:
            user = get_object(USER, user_id)
        except ObjectNotFoundError:
            return not_found(USER, user_id)

        if user.flagged_for_deletion:
            remove_item_from_delete_queue(user)
        else:
            return {'uuid': str(user.uuid), 'message': 'User {} not flagged for deletion.'.format(user.uuid)}, 200
        return {'uuid': str(user.uuid), 'message': 'User {} deletion flag removed.'.format(user.uuid)}, 200

@ns.route(
    '/<user_id>',
    endpoint='user')
class User(Resource):
    @flask_praetorian.auth_required
    @ns.doc(params={'user_id': 'ID for the user'})
    def get(self, user_id):
        try:
            return jsonify(user_dump_schema.dump(get_object(USER, user_id)))
        except ObjectNotFoundError:
            return not_found(USER, user_id)

    @flask_praetorian.auth_required
    @user_id_match_or_admin
    def delete(self, user_id):
        try:
            user = get_object(USER, user_id)
        except ObjectNotFoundError:
            return not_found(USER, user_id)
        try:
            add_item_to_delete_queue(user)
        except AlreadyFlaggedForDeletionError:
            return already_flagged_for_deletion_error(USER, str(user.uuid))

        return {'uuid': str(user.uuid), 'message': "User queued for deletion"}, 202

    @flask_praetorian.auth_required
    @user_id_match_or_admin
    def put(self, user_id):
        try:
            user = get_object(USER, user_id)
            if user.flagged_for_deletion:
                return not_found(USER, user_id)
        except ObjectNotFoundError:
            return not_found(USER, user_id)

        try:
            new_user = load_request_into_object(USER, instance=user)
        except ValidationError as e:
            return schema_validation_error(e)

        if new_user.password:
            new_user.password = guard.encrypt_password(new_user.password)

        db.session.commit()

        return {'uuid': str(user.uuid), 'message': 'User {} updated.'.format(user.username)}, 200


@ns.route(
    's',
    's/<_range>',
    's/<_range>/<order>',
    endpoint='users')
class Users(Resource):
    @flask_praetorian.roles_accepted('admin', 'coordinator')
    def get(self, _range=None, order="ascending"):
        try:
            items = get_range(get_all_objects(USER), _range, order)
        except InvalidRangeError as e:
            return forbidden_error(e)
        except Exception as e:
            return internal_error(e)

        return users_schema.dump(items, many=True)

    @flask_praetorian.roles_accepted('admin')
    def post(self):
        try:
            user = load_request_into_object(USER)
        except ValidationError as e:
            return schema_validation_error(str(e))

        user.password = guard.hash_password(user.password if user.password else "")

        db.session.add(user)
        db.session.commit()

        return {'uuid': str(user.uuid), 'message': 'User {} created'.format(user.username)}, 201


@ns.route('/<user_id>/tasks')
class AssignedTasksList(Resource):
    @flask_praetorian.auth_required
    def get(self, user_id):
        try:
            return jsonify(tasks_schema.dump(get_object(USER, user_id).tasks))
        except ObjectNotFoundError:
            return not_found(USER, user_id)


@ns.route('/<user_id>/username')
class UserNameField(Resource):
    @flask_praetorian.auth_required
    def get(self, user_id):
        try:
            return jsonify(user_username_schema.dump(get_object(USER, user_id)).data)
        except ObjectNotFoundError:
            return not_found(USER, user_id)


@ns.route('/<user_id>/address')
class UserAddressField(Resource):
    @flask_praetorian.auth_required
    def get(self, user_id):
        try:
            return jsonify(user_address_schema.dump(get_object(USER, user_id)).data)
        except ObjectNotFoundError:
            return not_found(USER, user_id)

