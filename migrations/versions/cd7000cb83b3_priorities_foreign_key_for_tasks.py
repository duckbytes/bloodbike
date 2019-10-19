"""priorities foreign key for tasks

Revision ID: cd7000cb83b3
Revises: d62c0f5f8b3c
Create Date: 2019-10-19 18:00:52.300808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd7000cb83b3'
down_revision = 'd62c0f5f8b3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('priority_id', sa.Integer(), nullable=True))
    op.drop_constraint('task_priority_fkey', 'task', type_='foreignkey')
    op.create_foreign_key(None, 'task', 'priority', ['priority_id'], ['id'])
    op.drop_column('task', 'priority')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('priority', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.create_foreign_key('task_priority_fkey', 'task', 'priority', ['priority'], ['id'])
    op.drop_column('task', 'priority_id')
    # ### end Alembic commands ###