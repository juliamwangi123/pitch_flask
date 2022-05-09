"""empty message

Revision ID: 4ca7560c3107
Revises: 778504ff59d2
Create Date: 2022-05-09 17:45:52.479475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ca7560c3107'
down_revision = '778504ff59d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitch', sa.Column('title', sa.String(length=60), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitch', 'title')
    # ### end Alembic commands ###
