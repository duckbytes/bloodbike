import os
from flask_login import LoginManager
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import flask_praetorian
import logging
from config import Config
import _thread
import time

logging.basicConfig(filename='/dev/null', level=logging.DEBUG)
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
ma = Marshmallow(app)
guard = flask_praetorian.Praetorian()

apiVersion = 'v0.1'

userApi = Api(app, prefix='/api/{}/user'.format(apiVersion))
loginApi = Api(app, prefix='/api/{}/login'.format(apiVersion))
sessionApi = Api(app, prefix='/api/{}/session'.format(apiVersion))
taskApi = Api(app, prefix='/api/{}/task'.format(apiVersion))
vehicleApi = Api(app, prefix='/api/{}/vehicle'.format(apiVersion))

app.debug = True
migrate = Migrate(app, db)


from app import models
from app.views import task, user, views, site, login, session, vehicle, testing_views
from app.housekeeping import monitor_deletions

#_thread.start_new_thread(monitor_deletions, ())
#monitor_deletions()

guard.init_app(app, models.User)
#app.register_blueprint(task.mod)
app.register_blueprint(site.mod)
app.register_blueprint(testing_views.mod)
#app.register_blueprint(decoder.mod)
#app.register_blueprint(encoder.mod)

#app.run(host='0.0.0.0', debug=True)
