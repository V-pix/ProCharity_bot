"""message

Revision ID: b5489e764848
Revises: 7e3358b5b907
Create Date: 2021-08-04 22:06:01.907286

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b5489e764848'
down_revision = '7e3358b5b907'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('date_external_registration', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'date_external_registration')
    # ### end Alembic commands ###
