"""Initial migration.

Revision ID: 3349749b27f1
Revises: 
Create Date: 2024-08-24 02:41:14.081848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3349749b27f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('priority', sa.String(length=50), nullable=False),
    sa.Column('due_date', sa.DateTime(), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    # ### end Alembic commands ###
