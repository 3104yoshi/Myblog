from flask import Blueprint, jsonify
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
        "content": 'api1'
    },
    {
        "title": 'api2',
        "content": 'api2'
    },
    {
        "title": 'api3',
        "content": 'api3'
    }
    ]
    return jsonify(articles)