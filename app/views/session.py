from flask import jsonify
from app import schemas
from flask_restful import reqparse, Resource
import flask_praetorian
from app import sessionApi as api

parser = reqparse.RequestParser()
parser.add_argument('user')
sessionSchema = schemas.SessionSchema()
from app.views.functions.viewfunctions import *
from app.views.functions.userfunctions import get_user_object
from app.views.functions.sessionfunctions import *
from app.views.functions.errors import *


class Session(Resource):
    @flask_praetorian.auth_required
    def get(self, _id):
        if not _id:
            return not_found()

        session = get_session_object(_id)

        print(session)

        if (session):
            return jsonify(sessionSchema.dump(session).data)
        else:
            return not_found("session",_id)

    @flask_praetorian.roles_accepted('coordinator', 'admin')
    @session_id_match_or_admin
    def delete(self, _id):
        if not _id:
            return not_found("session")

        session = get_session_object(_id)

        if not session:
            return not_found("session", _id)

        if session.flaggedForDeletion:
            return forbidden_error("this session is already flagged for deletion")

        session.flaggedForDeletion = True

        delete = models.DeleteFlags(objectId=_id, objectType=models.Objects.SESSION, timeToDelete=10)

        db.session.add(session)
        db.session.add(delete)

        db.session.commit()

        return {'id': _id, 'message': "Session {} queued for deletion".format(session.id)}, 202

class Sessions(Resource):
    @flask_praetorian.roles_accepted('coordinator', 'admin')
    def post(self):
        args = parser.parse_args()

        if args['user']:
            print(models.User.query.filter_by(id=args['user']))
            if not models.User.query.filter_by(id=args['user']).first():
                return forbidden_error("cannot create a session for a non-existent user")

        session = models.Session()

        session.user_id = utilities.current_user_id()

        if args['user']:
            if 'admin' in utilities.current_rolenames():
                session.user_id = args['user']
            else:
                return unauthorised_error("only admins can create sessions for other users")

        db.session.add(session)
        db.session.commit()

        return {'id': session.id, 'user_id': session.user_id, 'message': 'Session {} created'.format(session.id)}, 201

    def get(self, user_id, _range=None, order="ascending"):
        user = get_user_object(user_id)
        if not user:
            return not_found('user', user_id)

        items = get_range(user.sessions.all(), _range, order)

        result = {}

        if not isinstance(items, list):
            return items

        for i in items:
            result[str(i.id)] = {user.username: str(i.timestamp)}

        print(result)

        return result, 200


api.add_resource(Sessions,
                 's',
                 's/<user_id>',
                 's/<user_id>/<_range>',
                 's/<user_id>/<_range>/<order>')
api.add_resource(Session,
                '/<_id>')
