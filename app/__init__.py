import flask
from flask import Flask, Blueprint, render_template
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import flask_praetorian
import logging
from config import Config
import flask_cors
from flask_buzz import FlaskBuzz
from elasticsearch import Elasticsearch
from flask import jsonify

logging.basicConfig(filename='/dev/null', level=logging.DEBUG)
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

app = Flask(__name__, static_folder="site/static", template_folder="site")
flask_version = flask.__version__

app.config.from_object(Config)

app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None

db = SQLAlchemy(app, engine_options={"connect_args": {"options": "-c timezone=utc"}})
ma = Marshmallow(app)
cors = flask_cors.CORS()
cors.init_app(app)

guard = flask_praetorian.Praetorian()

api_version = 'v0.1'

api = Api(app, version='0.1', title='Blood Bike API',
          description='API for use with blood bike dispatching')

login_ns = api.namespace('api/{}/login'.format(api_version), description='Login operations')
user_ns = api.namespace('api/{}/user'.format(api_version), description='User operations')
session_ns = api.namespace('api/{}/session'.format(api_version), description='Session operations')
task_ns = api.namespace('api/{}/task'.format(api_version), description='Task operations')
vehicle_ns = api.namespace('api/{}/vehicle'.format(api_version), description='Vehicle operations')
comment_ns = api.namespace('api/{}/comment'.format(api_version), description='Comment operations')
deliverable_ns = api.namespace('api/{}/deliverable'.format(api_version), description='Deliverable operations')
location_ns = api.namespace('api/{}/location'.format(api_version), description='Saved location operations')
any_object_ns = api.namespace('api/{}/any'.format(api_version), description='Lookup for any object')
search_ns = api.namespace('api/{}/search'.format(api_version), description='Elasticsearch functions')
root_ns = api.namespace('api/{}'.format(api_version), description='Root api calls')


FlaskBuzz.register_error_handler_with_flask_restplus(api)

app.debug = True
migrate = Migrate(app, db)

from app import models
from app.api import task, user, views, site, login, session, vehicle, comment, testing_views, deliverable, location, uuid_lookup, search, priority, patch, ping, server_settings

site_blueprint = Blueprint('site', __name__, url_prefix='/')

guard.init_app(app, models.User)
app.register_blueprint(site_blueprint)
app.register_blueprint(testing_views.mod)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

