import flask
import flask_login
from flask import render_template, make_response, jsonify
from flask_login import LoginManager, login_user
from flask_restful import Api
from werkzeug.utils import redirect

from CONSTANTS import HOST, PORT
from api import users_resources, exersices_resources
from data import db_session
from data.exercises import Exercise
from data.users import User
from login_page import LoginForm, RegisterForm

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "sd7asf4qeu89r8rhee5hu674eu"

api = Api(app)
flask_login.LoginManager()

login_manager = LoginManager()
login_manager.init_app(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': error}), 404)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
def main_page():
    db_sess = db_session.create_session()
    exercises = db_sess.query(Exercise).all()
    return render_template("templates.html", exercises=exercises)


@app.route("/myace/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    db_session.global_init("db/club_body.sqlite")

    api.add_resource(users_resources.UsersListResource, '/api/users')
    api.add_resource(users_resources.UsersResource, '/api/users/<int:users_id>')
    api.add_resource(exersices_resources.ExercisesListResource, '/api/exercises')
    api.add_resource(exersices_resources.ExercisesResource, '/api/exercises/<int:exercises_id>')

    app.run(host=HOST, port=PORT)
