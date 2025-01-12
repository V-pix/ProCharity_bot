"""Update Base model

Revision ID: 976c4b9b4514
Revises: 87c7d29e3ddb
Create Date: 2022-12-26 12:56:27.764392

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '976c4b9b4514'
down_revision = '87c7d29e3ddb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        'tasks','created_date',
        new_column_name='created_at' 
    )
    op.alter_column(
        'tasks','updated_date',
        new_column_name='updated_at' 
    )
    op.alter_column(
        'statistics', 'added_date',
        new_column_name='created_at'
    )
    op.alter_column(
        'reasons_canceling', 'added_date',
        new_column_name='created_at'
    )
    op.alter_column(
        'reasons_canceling','updated_date',
        new_column_name='updated_at' 
    )
    op.alter_column(
        'external_site_users','created_date',
        new_column_name='created_at' 
    )
    op.alter_column(
        'external_site_users', 'updated_date',
        new_column_name='updated_at'
    )
    op.alter_column(
        'notifications','sent_date',
        new_column_name='created_at' 
    )
    
    for tbl in ['admin_users', 'users', 'categories', 'users_categories', 'admin_token_requests']: 
        op.add_column(tbl, sa.Column('created_at', sa.TIMESTAMP, nullable=True)) 
    
    for tbl in ['admin_users', 'users', 'categories', 'statistics', 'notifications', 'users_categories', 'admin_token_requests']: 
        op.add_column(tbl, sa.Column('updated_at', sa.TIMESTAMP, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###        
    op.alter_column(
        'tasks','created_at',
        new_column_name='created_date' 
    )
    op.alter_column(
        'tasks','updated_at',
        new_column_name='updated_date' 
    )
    op.alter_column(
        'statistics', 'created_at',
        new_column_name='added_date'
    )
    op.alter_column(
        'reasons_canceling', 'created_at',
        new_column_name='added_date'
    )
    op.alter_column(
        'reasons_canceling','updated_at',
        new_column_name='updated_date' 
    )
    op.alter_column(
        'external_site_users','created_at',
        new_column_name='created_date' 
    )
    op.alter_column(
        'external_site_users', 'updated_at',
        new_column_name='updated_date'
    )
    op.alter_column(
        'notifications','created_at',
        new_column_name='sent_date' 
    )
    
    for tbl in ['admin_users', 'users', 'categories', 'users_categories', 'admin_token_requests']: 
        op.drop_column(tbl, 'created_at') 
    
    for tbl in ['admin_users', 'users', 'categories', 'statistics', 'notifications', 'users_categories', 'admin_token_requests']: 
        op.drop_column(tbl, 'updated_at')
    # ### end Alembic commands ###