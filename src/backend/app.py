import os
from flask import Flask, redirect, render_template, request, url_for
from flask_login import LoginManager, login_required
from api import api
from authentification import authentification
from db.accessor.articlesAccessor import articlesAccessor
from db.data.article import article
from user import User

app = Flask(__name__,
            static_folder = "../dist/static",
            template_folder="../dist")

login_manager = LoginManager(app)
login_manager.init_app(authentification)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

auth_prefix = 'auth'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for(auth_prefix + '.login'))

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(authentification, url_prefix='/' + auth_prefix)

app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'GET':
        return render_template('index.html')
    title = request.form.get('title')
    content = request.form.get('content')
    data = article(title, content)
    try:
        articlesAccessor.addArticle(data)
    except Exception as e:
        print(e)
        return redirect(url_for('canPost', postStatus=False))
    return redirect(url_for('canPost', postStatus=True))

@app.route('/canPost/<postStatus>/', methods=['GET'])
@login_required
def canPost(postStatus):
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
