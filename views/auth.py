from flask import Blueprint, render_template, redirect, url_for, request, flash
# from http import HTTPStatus
auth_app = Blueprint("auth_app", __name__)
from werkzeug.security import generate_password_hash, check_password_hash
from models import db
from models.model import User
from flask_login import login_user, logout_user, login_required, current_user



@auth_app.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('root_view'))
    return render_template('login.html')


@auth_app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flash('Указаны невалидные данные. Пожалуйста, проверьте корректность ввода логина/пароля.')
        return redirect(url_for('auth_app.login'))

    login_user(user, remember=remember)
    return redirect(url_for('root_view'))


@auth_app.route('/signup')
def signup():
    return render_template('signup.html')


@auth_app.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    if user:
        flash('Пользователь с таким логином уже существует.')
        return redirect(url_for('auth_app.signup'))

    new_user = User(username=username, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth_app.login'))


@auth_app.route('/logout')
# @login_required
def logout():
    if not current_user.is_authenticated:
        return redirect(url_for('root_view'))
    logout_user()
    return redirect(url_for('root_view'))