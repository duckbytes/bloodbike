from flask import render_template, Blueprint

mod = Blueprint('session', __name__, url_prefix='/site/session', template_folder='templates', static_folder='static')


@mod.route('<session_id>', methods=['GET'])
def session(session_id):
    return render_template('session.html')

@mod.route('/manifest.json', methods=['GET'])
def manifest_json():
    return render_template('manifest.json')
@mod.route('/service-worker.js', methods=['GET'])
def service_worker():
    return render_template('service-worker.js')
