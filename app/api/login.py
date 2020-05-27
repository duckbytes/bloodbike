from flask_restx import reqparse, Resource
from app import guard
from app import login_ns as ns
from flask import jsonify


parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('password')


@ns.route('')
class Login(Resource):
    def post(self):
        args = parser.parse_args()
        user = guard.authenticate(args['username'], args['password'])
        ret = {'access_token': guard.encode_jwt_token(user)}
        return ret, 200


@ns.route('/refresh_token')
class Login(Resource):
    def get(self):
        old_token = guard.read_token_from_header()
        new_token = guard.refresh_jwt_token(old_token)
        return jsonify(access_token=new_token)
