"""empty message

Revision ID: b34a8dece7ed
Revises: 97a332c397de
Create Date: 2019-01-27 18:12:13.634198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b34a8dece7ed'
down_revision = '97a332c397de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('sites_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'users', 'sites', ['sites_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'sites_id')
    # ### end Alembic commands ###