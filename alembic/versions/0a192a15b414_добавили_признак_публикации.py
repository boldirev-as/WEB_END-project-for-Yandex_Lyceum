"""добавили признак публикации

Revision ID: 0a192a15b414
Revises: 
Create Date: 2021-04-21 17:10:21.675491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a192a15b414'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercises',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('age_up', sa.Integer(), nullable=True),
    sa.Column('weight_up', sa.Integer(), nullable=True),
    sa.Column('sex', sa.String(), nullable=True),
    sa.Column('height_up', sa.Integer(), nullable=True),
    sa.Column('age_down', sa.Integer(), nullable=True),
    sa.Column('weight_down', sa.Integer(), nullable=True),
    sa.Column('height_down', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('surname', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('sex', sa.String(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('modified_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('exercises')
    # ### end Alembic commands ###
