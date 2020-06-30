"""empty message

Revision ID: 02bd2cd7181a
Revises: 05b4318c5600
Create Date: 2020-06-27 17:26:38.212179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02bd2cd7181a'
down_revision = '05b4318c5600'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('banner', sa.Column('is_delete', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('banner', 'is_delete')
    # ### end Alembic commands ###