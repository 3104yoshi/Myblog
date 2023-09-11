import os
from flask import Flask, redirect, render_template, request, url_for
from flask_login import LoginManager, login_required
from api import api
from authentification import authentification
from db.accessor.articlesAccessor import articlesAccessor
from db.data.article import article
from user import User

appserver = Flask(__name__,
            static_folder = "../dist/static",
            template_folder="../dist")

login_manager = LoginManager(appserver)
login_manager.init_app(authentification)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

auth_prefix = 'auth'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for(auth_prefix + '.login'))

appserver.register_blueprint(api, url_prefix='/api')
appserver.register_blueprint(authentification, url_prefix='/' + auth_prefix)

appserver.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')

@appserver.route('/', defaults={'path': ''})
@appserver.route('/<path:path>')
def index(path):
    return render_template('index.html')

@appserver.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        articleId = articlesAccessor.getNextId()
        title = request.form.get('title')
        content = request.form.get('content')
        data = article(articleId, title, content)
        try:
            articlesAccessor.addArticle(data)
        except Exception as e:
            return redirect(url_for('canPost', postStatus="投稿に失敗しました"))
        return redirect(url_for('canPost', postStatus="投稿に成功しました"))
    else:
        return redirect(url_for('notfound'))

@appserver.route('/canPost/<postStatus>/', methods=['GET'])
@login_required
def canPost(postStatus):
    return render_template('index.html')

if __name__ == "__main__":
    appserver.run(host='0.0.0.0', port=80, debug=True)