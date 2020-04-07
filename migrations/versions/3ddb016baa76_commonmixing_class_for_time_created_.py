"""CommonMixing class for time_created, time_modified and flagged_for_deletion

Revision ID: 3ddb016baa76
Revises: 4529a80c2aad
Create Date: 2020-04-06 20:07:27.079063

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3ddb016baa76'
down_revision = '4529a80c2aad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('deliverable', sa.Column('time_created', sa.DateTime(), nullable=True))
    op.add_column('deliverable', sa.Column('time_modified', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_deliverable_time_created'), 'deliverable', ['time_created'], unique=False)
    op.create_index(op.f('ix_deliverable_time_modified'), 'deliverable', ['time_modified'], unique=False)
    op.add_column('deliverable_type', sa.Column('flagged_for_deletion', sa.Boolean(), nullable=True))
    op.add_column('deliverable_type', sa.Column('time_created', sa.DateTime(), nullable=True))
    op.add_column('deliverable_type', sa.Column('time_modified', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_deliverable_type_time_created'), 'deliverable_type', ['time_created'], unique=False)
    op.create_index(op.f('ix_deliverable_type_time_modified'), 'deliverable_type', ['time_modified'], unique=False)
    op.add_column('location', sa.Column('time_created', sa.DateTime(), nullable=True))
    op.add_column('location', sa.Column('time_modified', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_location_time_created'), 'location', ['time_created'], unique=False)
    op.create_index(op.f('ix_location_time_modified'), 'location', ['time_modified'], unique=False)
    op.add_column('note', sa.Column('flagged_for_deletion', sa.Boolean(), nullable=True))
    op.add_column('note', sa.Column('time_created', sa.DateTime(), nullable=True))
    op.add_column('note', sa.Column('time_modified', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_note_time_created'), 'note', ['time_created'], unique=False)
    op.create_index(op.f('ix_note_time_modified'), 'note', ['time_modified'], unique=False)
    op.add_column('patch', sa.Column('flagged_for_deletion', sa.Boolean(), nullable=True))
    op.add_column('patch', sa.Column('time_created', sa.DateTime(), nullable=True))
    op.add_column('patch', sa.Column('time_modified', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_patch_time_created'), 'patch', ['time_created'], unique=False)
    op.create_index(op.f('ix_patch_time_modified'), 'patch', ['time_modified'], unique=False)
    op.add_column('priority', sa.Column('flagged_for_deletion', sa.Boolean(), nullable=True))
    op.add_column('priority', sa.Column('time_created', sa.DateTime(), nullable=True))
    op.add_column('priority', sa.Column('time_modified', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_priority_time_created'), 'priority', ['time_created'], unique=False)
    op.create_index(op.f('ix_priority_time_modified'), 'priority', ['time_modified'], unique=False)
    op.add_column('session', sa.Column('time_created', sa.DateTime(), nullable=True))
    op.add_column('session', sa.Column('time_modified', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_session_time_created'), 'session', ['time_created'], unique=False)
    op.create_index(op.f('ix_session_time_modified'), 'session', ['time_modified'], unique=False)
    op.add_column('task', sa.Column('time_created', sa.DateTime(), nullable=True))
    op.add_column('task', sa.Column('time_modified', sa.DateTime(), nullable=True))
    op.add_column('task', sa.Column('time_of_call', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_task_time_created'), 'task', ['time_created'], unique=False)
    op.create_index(op.f('ix_task_time_modified'), 'task', ['time_modified'], unique=False)
    op.create_index(op.f('ix_task_time_of_call'), 'task', ['time_of_call'], unique=False)
    op.drop_index('ix_task_timestamp', table_name='task')
    op.drop_column('task', 'timestamp')
    op.add_column('user', sa.Column('time_created', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('time_modified', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_time_created'), 'user', ['time_created'], unique=False)
    op.create_index(op.f('ix_user_time_modified'), 'user', ['time_modified'], unique=False)
    op.add_column('vehicle', sa.Column('time_created', sa.DateTime(), nullable=True))
    op.add_column('vehicle', sa.Column('time_modified', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_vehicle_time_created'), 'vehicle', ['time_created'], unique=False)
    op.create_index(op.f('ix_vehicle_time_modified'), 'vehicle', ['time_modified'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_vehicle_time_modified'), table_name='vehicle')
    op.drop_index(op.f('ix_vehicle_time_created'), table_name='vehicle')
    op.drop_column('vehicle', 'time_modified')
    op.drop_column('vehicle', 'time_created')
    op.drop_index(op.f('ix_user_time_modified'), table_name='user')
    op.drop_index(op.f('ix_user_time_created'), table_name='user')
    op.drop_column('user', 'time_modified')
    op.drop_column('user', 'time_created')
    op.add_column('task', sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.create_index('ix_task_timestamp', 'task', ['timestamp'], unique=False)
    op.drop_index(op.f('ix_task_time_of_call'), table_name='task')
    op.drop_index(op.f('ix_task_time_modified'), table_name='task')
    op.drop_index(op.f('ix_task_time_created'), table_name='task')
    op.drop_column('task', 'time_of_call')
    op.drop_column('task', 'time_modified')
    op.drop_column('task', 'time_created')
    op.drop_index(op.f('ix_session_time_modified'), table_name='session')
    op.drop_index(op.f('ix_session_time_created'), table_name='session')
    op.drop_column('session', 'time_modified')
    op.drop_column('session', 'time_created')
    op.drop_index(op.f('ix_priority_time_modified'), table_name='priority')
    op.drop_index(op.f('ix_priority_time_created'), table_name='priority')
    op.drop_column('priority', 'time_modified')
    op.drop_column('priority', 'time_created')
    op.drop_column('priority', 'flagged_for_deletion')
    op.drop_index(op.f('ix_patch_time_modified'), table_name='patch')
    op.drop_index(op.f('ix_patch_time_created'), table_name='patch')
    op.drop_column('patch', 'time_modified')
    op.drop_column('patch', 'time_created')
    op.drop_column('patch', 'flagged_for_deletion')
    op.drop_index(op.f('ix_note_time_modified'), table_name='note')
    op.drop_index(op.f('ix_note_time_created'), table_name='note')
    op.drop_column('note', 'time_modified')
    op.drop_column('note', 'time_created')
    op.drop_column('note', 'flagged_for_deletion')
    op.drop_index(op.f('ix_location_time_modified'), table_name='location')
    op.drop_index(op.f('ix_location_time_created'), table_name='location')
    op.drop_column('location', 'time_modified')
    op.drop_column('location', 'time_created')
    op.drop_index(op.f('ix_deliverable_type_time_modified'), table_name='deliverable_type')
    op.drop_index(op.f('ix_deliverable_type_time_created'), table_name='deliverable_type')
    op.drop_column('deliverable_type', 'time_modified')
    op.drop_column('deliverable_type', 'time_created')
    op.drop_column('deliverable_type', 'flagged_for_deletion')
    op.drop_index(op.f('ix_deliverable_time_modified'), table_name='deliverable')
    op.drop_index(op.f('ix_deliverable_time_created'), table_name='deliverable')
    op.drop_column('deliverable', 'time_modified')
    op.drop_column('deliverable', 'time_created')
    # ### end Alembic commands ###
