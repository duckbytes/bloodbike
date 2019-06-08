from flask import render_template
from app import app
import flask_praetorian

from app import db

@app.route('/home', methods=['GET'])
def hello():
    return render_template('index.html',
                           title="Freewheelers EVS")

@app.route('/fetch.js', methods=['GET'])
def fetch():
    return render_template('javascript/fetches.js',
                           api_url="/api/v0.1/")
