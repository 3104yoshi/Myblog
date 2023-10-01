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
    elif request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        data = article(title, content)
        try:
            articlesAccessor.addArticle(data)
        except Exception as e:
            print(e)
            return redirect(url_for('canPost', postStatus=False))
        return redirect(url_for('canPost', postStatus=True))
    else:
        return redirect(url_for('notfound'))

@app.route('/canPost/<postStatus>/', methods=['GET'])
@login_required
def canPost(postStatus):
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

#  q: post() を可読性の高いコードに置き換えることはできるか？
#  a: できる。post() は、GET と POST で処理を分けているが、
#     これを、GET と POST で処理を分ける関数に分割することで、
#     可読性の高いコードに置き換えることができる。
#     例えば、以下のようなコードに置き換えることができる。
#     def get():
#         return render_template('index.html')
#     def post():
#         title = request.form.get('title')
#         content = request.form.get('content')
#         data = article(title, content)
#         try:
#             articlesAccessor.addArticle(data)
#         except Exception as e:
#             print(e)

#  q: canPost() を可読性の高いコードに置き換えることはできるか？
#  a: できる。canPost() は、GET で処理を行っているが、
#     これを、GET で処理を行う関数に分割することで、
#     可読性の高いコードに置き換えることができる。
#     例えば、以下のようなコードに置き換えることができる。
#     def get():
#         return render_template('index.html')

# q: Could you write a test code for the post() function?
# a: Yes, I can. I will write a test code for the post() function.
#    I will use pytest to write the test code.
#    I will write the test code in the following way.
#    def test_post():
#        with app.test_client() as client:
#            response = client.post('/post', data=dict(
#                title='test_title',
#                content='test_content'
#            ))
#            assert response.status_code == 200
#            assert response.data == b'OK'
#    I will run the test code in the following way.
#    pytest test_app.py
#    I will check the result of the test code in the following way.
#    If the test code is correct, the following message will be displayed.
#    1 passed in 0.01s
#    If the test code is incorrect, the following message will be displayed.
#    1 failed in 0.01s


