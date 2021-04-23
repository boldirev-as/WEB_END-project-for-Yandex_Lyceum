from flask import jsonify
from flask_restful import Resource, reqparse
from werkzeug.exceptions import abort

from data import db_session
from data.users import User


def abort_if_users_not_found(users_id):
    session = db_session.create_session()
    users = session.query(User).get(users_id)
    if not users:
        abort(404, message=f"Users {users_id} not found")


parser = reqparse.RequestParser()
parser.add_argument('surname', required=True)
parser.add_argument('name', required=True)
parser.add_argument('age', required=True, type=int)
parser.add_argument('weight', required=True, type=int)
parser.add_argument('sex', required=True, type=str)
parser.add_argument('height', required=True, type=int)
parser.add_argument('email', required=True, type=str)


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'name', 'surname')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        try:
            users = User(
                surname=args["surname"],
                name=args["name"],
                age=args["age"],
                weight=args["weight"],
                sex=args["sex"],
                height=args["height"],
                email=args["email"]
            )
            session.add(users)
            session.commit()
            return jsonify({'success': 'OK'})
        except Exception as e:
            abort(404, message=f"{e}")


class UsersResource(Resource):
    def get(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        return jsonify(users.to_dict(
            only=('id', 'surname', 'name', 'age',
                  'weight', 'sex', 'height', 'email')))

    def delete(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})
