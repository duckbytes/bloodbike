import functools
from flask_praetorian import utilities
from flask import request
from app import models
from app.exceptions import InvalidRangeError
from app.exceptions import SchemaValidationError
from app.views.functions.errors import forbidden_error


def user_id_match_or_admin(func):
    @functools.wraps(func)
    def wrapper(self, _id):
        print(_id, utilities.current_user_id(), "SJAKLDFJKLSAF")
        if 'admin' in utilities.current_rolenames():
            return func(self, _id)
        if utilities.current_user_id() == _id:
            return func(self, _id)
        else:
            return forbidden_error("Object not owned by user: user id:".format(_id))
    return wrapper


def load_request_into_object(schema, object_to_load_into):
    request_json = request.get_json()
    if not request_json:
        raise SchemaValidationError("No json input data provided")

    parsed_schema = schema.load(request_json)
    if parsed_schema.errors:
        raise SchemaValidationError(parsed_schema.errors)

    object_to_load_into.updateFromDict(**parsed_schema.data)


def get_all_users():
    return models.User.query.all()


def get_range(items, _range="0-50", order="descending"):

    start = 0
    end = 50

    if _range:
        between = _range.split('-')

        if between[0].isdigit() and between[1].isdigit():
            start = int(between[0])
            end = int(between[1])
        else:
            raise InvalidRangeError("invalid range")

    if start > end:
        raise InvalidRangeError("invalid range")

    if end - start > 1000:
        raise InvalidRangeError("range too large")

    if order == "descending":
        items.reverse()

    for i in items[:]:
        if i.flaggedForDeletion:
            items.remove(i)

    return items[start:end]
