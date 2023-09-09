from flask import Blueprint, app, jsonify, render_template
from flask_login import login_required

api = Blueprint('api', __name__)

@api.route('/hello')
@login_required
def hello():
    response = {'msg': 'world'}
    return jsonify(response)

@api.route('/articles')
def articles():
    articles = [
    {
        "title": 'api1',
        "body": 'api1'
    },
    {
        "title": 'api2',
        "body": 'api2'
    },
    {
        "title": 'api3',
        "body": 'api3'
    }
    ]
    return jsonify(articles)