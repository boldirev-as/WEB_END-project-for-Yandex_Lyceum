"""добавили признак публикации

Revision ID: 8f138152faf4
Revises: 0a192a15b414
Create Date: 2021-04-21 18:17:17.819190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f138152faf4'
down_revision = '0a192a15b414'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('exercises', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('exercises', 'title')
    # ### end Alembic commands ###
