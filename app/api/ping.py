from app import root_ns as ns
from flask_restx import Resource


@ns.route('/ping', endpoint="api_ping")
class Ping(Resource):
    def get(self):
        return "pong", 200