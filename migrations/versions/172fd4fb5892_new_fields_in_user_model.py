"""new fields in user model

Revision ID: 172fd4fb5892
Revises: 780739b227a7
Create Date: 2023-04-08 20:26:59.080979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '172fd4fb5892'
down_revision = '780739b227a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
