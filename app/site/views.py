from flask import render_template, Blueprint

mod = Blueprint('site', __name__, url_prefix='/site', template_folder='templates', static_folder='static')


@mod.route('/', methods=['GET'])
def hello():
    return render_template('index_old.html')

@mod.route('/fetch.js', methods=['GET'])
def fetch():
    return render_template('javascript/fetches.js',
                           api_url="/api/v0.1/")

@mod.route('new', methods=['GET'])
def start_session():

    return "startsession"

@mod.route("registercord")
def register_coordinator():
    return "registercoord"


@mod.route("registerrider")
def register_rider():
    return "registerrider"

@mod.route("additem")
def add_item():
    return "additem"
