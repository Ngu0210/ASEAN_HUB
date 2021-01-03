"""Removed nullable on order table

Revision ID: 50d6bd5af403
Revises: 2d9664274efb
Create Date: 2021-01-03 18:31:01.695618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50d6bd5af403'
down_revision = '2d9664274efb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('order', 'menu_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('order', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('order', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('order', 'menu_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
