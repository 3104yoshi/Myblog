from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_login import login_required, logout_user
import flask_login
from db.accessor.userCredentialAccessor import userCredentialAccessor
from user import User
from db.data.userCredential import userCredential


authentification = Blueprint('auth', __name__)


@authentification.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html')

    username = request.form.get('username')
    password = request.form.get('password')

    credential = userCredential(username, password)

    if userCredentialAccessor.getUser(credential):
        user = User(username)
        flask_login.login_user(user)
        return redirect(url_for('auth.canLogin', canLogin='ログインに成功しました'))

    return render_template('index.html')


@authentification.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('index.html')

    username = request.form.get('username')
    password = request.form.get('password')

    credential = userCredential(username, password)
    if userCredentialAccessor.checkUserIs(credential):
        return redirect(url_for('auth.canSignup', canSignup="既に登録されているユーザー名です"))

    userCredentialAccessor.addUser(credential)

    return redirect(url_for('auth.canSignup', canSignup="登録に成功しました"))


@authentification.route('/canSignup/<canSignup>/', methods=['GET', 'POST'])
def canSignup(canSignup):
    return render_template('index.html', signupStatus=canSignup)

@authentification.route('/canLogin/<canLogin>/', methods=['GET', 'POST'])
def canLogin(canLogin):
    return render_template('index.html', loginStatus=canLogin)


@authentification.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return render_template('index.html')

@authentification.route('/isLogin/', methods=['GET'])
def isLogin():
    return jsonify(flask_login.current_user.is_authenticated)