import sqlalchemy
from .db_session import SqlAlchemyBase


class Exercise(SqlAlchemyBase):
    __tablename__ = 'exercises'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    title = sqlalchemy.Column(sqlalchemy.String)

    age_up = sqlalchemy.Column(sqlalchemy.Integer)
    weight_up = sqlalchemy.Column(sqlalchemy.Integer)
    sex = sqlalchemy.Column(sqlalchemy.String)
    height_up = sqlalchemy.Column(sqlalchemy.Integer)

    age_down = sqlalchemy.Column(sqlalchemy.Integer)
    weight_down = sqlalchemy.Column(sqlalchemy.Integer)
    height_down = sqlalchemy.Column(sqlalchemy.Integer)
