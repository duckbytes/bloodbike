"""uuid now primary key

Revision ID: e7a36600ebf7
Revises: 11f11c27110b
Create Date: 2019-04-29 20:58:41.616747

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'e7a36600ebf7'
down_revision = '11f11c27110b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('delete_flags', 'id')
    op.drop_column('saved_locations', 'id')
    op.drop_constraint('session_user_id_fkey', 'session', type_='foreignkey')
    op.create_foreign_key(None, 'session', 'user', ['user_id'], ['uuid'])
    op.drop_column('session', 'id')
    op.drop_constraint('task_session_fkey', 'task', type_='foreignkey')
    op.create_foreign_key(None, 'task', 'session', ['session'], ['uuid'])
    op.drop_column('task', 'id')
    op.drop_constraint('user_assignedVehicle_fkey', 'user', type_='foreignkey')
    op.create_foreign_key(None, 'user', 'vehicle', ['assignedVehicle'], ['uuid'])
    op.drop_column('user', 'id')
    op.drop_column('vehicle', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vehicle', sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('vehicle_id_seq'::regclass)"), autoincrement=True, nullable=False))
    op.add_column('user', sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('user_id_seq'::regclass)"), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.create_foreign_key('user_assignedVehicle_fkey', 'user', 'vehicle', ['assignedVehicle'], ['id'])
    op.add_column('task', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.create_foreign_key('task_session_fkey', 'task', 'session', ['session'], ['id'])
    op.add_column('session', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'session', type_='foreignkey')
    op.create_foreign_key('session_user_id_fkey', 'session', 'user', ['user_id'], ['id'])
    op.add_column('saved_locations', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.add_column('delete_flags', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    # ### end Alembic commands ###
