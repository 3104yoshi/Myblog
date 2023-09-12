from flask import Blueprint, jsonify
from flask_login import login_required

from db.accessor.articlesAccessor import articlesAccessor

api = Blueprint('api', __name__)

@api.route('/articles')
def articles():
    articles = []
    fetched_articles = articlesAccessor.getAllArticles()
    for fetched_article in fetched_articles:
        articles.append({
            "title": fetched_article[1],
            "content": fetched_article[2]
        })

    return jsonify(articles)