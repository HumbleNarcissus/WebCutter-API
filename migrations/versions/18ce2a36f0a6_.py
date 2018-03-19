"""empty message

Revision ID: 18ce2a36f0a6
Revises: 10364daef15e
Create Date: 2018-03-18 16:16:02.390745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18ce2a36f0a6'
down_revision = '10364daef15e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sites', 'is_working',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sites', 'is_working',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
