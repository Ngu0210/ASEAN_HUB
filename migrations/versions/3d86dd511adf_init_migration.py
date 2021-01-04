"""init migration

Revision ID: 3d86dd511adf
Revises: 
Create Date: 2021-01-04 02:19:05.389981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d86dd511adf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drink_menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('ice', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('main_menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('vegetarian', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('main_menu', sa.Integer(), nullable=False),
    sa.Column('drink_menu', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['drink_menu'], ['drink_menu.id'], ),
    sa.ForeignKeyConstraint(['main_menu'], ['main_menu.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('menu_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['menu_id'], ['menu.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_order')
    op.drop_table('menu')
    op.drop_table('users')
    op.drop_table('main_menu')
    op.drop_table('drink_menu')
    # ### end Alembic commands ###
