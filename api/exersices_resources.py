from flask import jsonify
from flask_restful import Resource, reqparse
from werkzeug.exceptions import abort

from data import db_session
from data.exercises import Exercise


def abort_if_exercises_not_found(exercises_id):
    session = db_session.create_session()
    exercises = session.query(Exercise).get(exercises_id)
    if not exercises:
        abort(404, message=f"exercises {exercises_id} not found")


parser = reqparse.RequestParser()
parser.add_argument('age_up', required=True, type=int)
parser.add_argument('weight_up', required=True, type=int)
parser.add_argument('sex', required=True, type=str)
parser.add_argument('weight', required=True, type=int)
parser.add_argument('height_up', required=True, type=int)
parser.add_argument('age_down', required=True, type=int)
parser.add_argument('weight_down', required=True, type=int)
parser.add_argument('height_down', required=True, type=int)
parser.add_argument('title', required=True, type=str)


class ExercisesListResource(Resource):
    def get(self):
        session = db_session.create_session()
        exercises = session.query(Exercise).all()
        return jsonify({'exercises': [item.to_dict(
            only=('id', 'title')) for item in exercises]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        try:
            exercises = Exercise(
                title=args["title"],
                age_up=args["age_up"],
                weight_up=args["weight_up"],
                sex=args["sex"],
                height_up=args["height_up"],
                age_down=args["age_down"],
                weight_down=args["weight_down"],
                height_down=args["height_down"]
            )
            session.add(exercises)
            session.commit()
            return jsonify({'success': 'OK'})
        except Exception as e:
            abort(404, message=f"{e}")


class ExercisesResource(Resource):
    def get(self, exercises_id):
        abort_if_exercises_not_found(exercises_id)
        session = db_session.create_session()
        exercises = session.query(Exercise).get(exercises_id)
        return jsonify(exercises.to_dict(
            only=('id', 'title', 'age_up', 'weight_up',
                  'sex', 'height_up', 'age_down', 'weight_down',
                  'height_down')))

    def delete(self, exercises_id):
        abort_if_exercises_not_found(exercises_id)
        session = db_session.create_session()
        exercises = session.query(Exercise).get(exercises_id)
        session.delete(exercises)
        session.commit()
        return jsonify({'success': 'OK'})
