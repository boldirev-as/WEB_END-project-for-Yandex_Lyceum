import sqlalchemy
from .db_session import SqlAlchemyBase


class Exercise(SqlAlchemyBase):
    __tablename__ = 'exercises'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    title = sqlalchemy.Column(sqlalchemy.String)

    body_part = sqlalchemy.Column(sqlalchemy.String)
    equipment = sqlalchemy.Column(sqlalchemy.String)
    difficulty = sqlalchemy.Column(sqlalchemy.Integer)

    img = sqlalchemy.Column(sqlalchemy.String)
    plot = sqlalchemy.Column(sqlalchemy.String)
