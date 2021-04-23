import flask
from flask import render_template
from flask_restful import Api

from api import users_resources, exersices_resources
from data import db_session
from CONSTANTS import HOST, PORT

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "sd7asf4qeu89r8rhee5hu674eu"

api = Api(app)


@app.route("/")
def test():
    return render_template("templates.html")


if __name__ == '__main__':
    db_session.global_init("db/club_body.sqlite")

    api.add_resource(users_resources.UsersListResource, '/api/users')
    api.add_resource(users_resources.UsersResource, '/api/users/<int:users_id>')
    api.add_resource(exersices_resources.ExercisesListResource, '/api/exercises')
    api.add_resource(exersices_resources.ExercisesResource, '/api/exercises/<int:exercises_id>')

    app.run(host=HOST, port=PORT)
