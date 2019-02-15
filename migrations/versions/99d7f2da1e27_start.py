"""start

Revision ID: 99d7f2da1e27
Revises: 
Create Date: 2019-01-19 23:43:45.623659

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from enum import IntEnum, auto


# revision identifiers, used by Alembic.
revision = '99d7f2da1e27'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    
    class Objects(IntEnum):
            USER = auto()
            SESSION = auto()
            TASK = auto()
            VEHICLE = auto()
    op.create_table('delete_flags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('objectId', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('timeToDelete', sa.Integer(), nullable=True),
    sa.Column('objectType', sqlalchemy_utils.types.choice.ChoiceType(Objects), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_delete_flags_timestamp'), 'delete_flags', ['timestamp'], unique=False)
    op.create_table('saved_locations',
    sa.Column('address1', sa.String(length=64), nullable=True),
    sa.Column('address2', sa.String(length=64), nullable=True),
    sa.Column('town', sa.String(length=64), nullable=True),
    sa.Column('county', sa.String(length=64), nullable=True),
    sa.Column('country', sa.String(length=64), nullable=True),
    sa.Column('postcode', sa.String(length=7), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('notes', sa.String(length=10000), nullable=True),
    sa.Column('contact', sa.String(length=64), nullable=True),
    sa.Column('phoneNumber', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_saved_locations_timestamp'), 'saved_locations', ['timestamp'], unique=False)
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('manufacturer', sa.String(length=64), nullable=True),
    sa.Column('model', sa.String(length=64), nullable=True),
    sa.Column('dateOfManufacture', sa.Date(), nullable=True),
    sa.Column('dateOfRegistration', sa.Date(), nullable=True),
    sa.Column('registrationNumber', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_vehicle_timestamp'), 'vehicle', ['timestamp'], unique=False)
    op.create_table('user',
    sa.Column('address1', sa.String(length=64), nullable=True),
    sa.Column('address2', sa.String(length=64), nullable=True),
    sa.Column('town', sa.String(length=64), nullable=True),
    sa.Column('county', sa.String(length=64), nullable=True),
    sa.Column('country', sa.String(length=64), nullable=True),
    sa.Column('postcode', sa.String(length=7), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('dob', sa.Date(), nullable=True),
    sa.Column('assignedVehicle', sa.Integer(), nullable=True),
    sa.Column('patch', sa.String(length=64), nullable=True),
    sa.Column('status', sa.String(length=64), nullable=True),
    sa.Column('flaggedForDeletion', sa.Boolean(), nullable=True),
    sa.Column('roles', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='true', nullable=True),
    sa.ForeignKeyConstraint(['assignedVehicle'], ['vehicle.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_user_timestamp'), 'user', ['timestamp'], unique=False)
    op.create_table('session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_session_timestamp'), 'session', ['timestamp'], unique=False)
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('pickupAddress1', sa.String(length=64), nullable=True),
    sa.Column('pickupAddress2', sa.String(length=64), nullable=True),
    sa.Column('pickupTown', sa.String(length=64), nullable=True),
    sa.Column('pickupPostcode', sa.String(length=7), nullable=True),
    sa.Column('destinationAddress1', sa.String(length=64), nullable=True),
    sa.Column('destinationAddress2', sa.String(length=64), nullable=True),
    sa.Column('destinationTown', sa.String(length=64), nullable=True),
    sa.Column('destinationPostcode', sa.String(length=7), nullable=True),
    sa.Column('patch', sa.String(length=64), nullable=True),
    sa.Column('contactName', sa.String(length=64), nullable=True),
    sa.Column('contactNumber', sa.Integer(), nullable=True),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('finalDuration', sa.Time(), nullable=True),
    sa.Column('miles', sa.Integer(), nullable=True),
    sa.Column('session', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['session'], ['session.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_task_timestamp'), 'task', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_timestamp'), table_name='task')
    op.drop_table('task')
    op.drop_index(op.f('ix_session_timestamp'), table_name='session')
    op.drop_table('session')
    op.drop_index(op.f('ix_user_timestamp'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_vehicle_timestamp'), table_name='vehicle')
    op.drop_table('vehicle')
    op.drop_index(op.f('ix_saved_locations_timestamp'), table_name='saved_locations')
    op.drop_table('saved_locations')
    op.drop_index(op.f('ix_delete_flags_timestamp'), table_name='delete_flags')
    op.drop_table('delete_flags')
    # ### end Alembic commands ###