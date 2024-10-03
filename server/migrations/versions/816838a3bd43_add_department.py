"""add Department

Revision ID: 816838a3bd43
Revises: ca897884022d
Create Date: 2024-10-03 09:15:45.495231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '816838a3bd43'
down_revision = 'ca897884022d'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('departments', 'address', new_column_name='location')

def downgrade():
    op.alter_column('departments', 'location', new_column_name='address')