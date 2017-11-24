"""Adding tag column to Page

Revision ID: 912600c93bb2
Revises: 0a633752ae0e
Create Date: 2017-11-24 11:43:10.073263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '912600c93bb2'
down_revision = '0a633752ae0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('page', sa.Column('tag', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('page', 'tag')
    # ### end Alembic commands ###
