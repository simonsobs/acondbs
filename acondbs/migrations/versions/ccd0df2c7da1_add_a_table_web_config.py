"""add a table web_config

Revision ID: ccd0df2c7da1
Revises: aeec123e508c
Create Date: 2020-10-13 10:36:06.201703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccd0df2c7da1'
down_revision = 'aeec123e508c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('web_config',
    sa.Column('config_id', sa.Integer(), nullable=False),
    sa.Column('head_title', sa.Text(), nullable=True),
    sa.Column('toolbar_title', sa.Text(), nullable=True),
    sa.Column('devtool_loadingstate', sa.Boolean(), nullable=True),
    sa.Column('product_creation_dialog', sa.Boolean(), nullable=True),
    sa.Column('product_update_dialog', sa.Boolean(), nullable=True),
    sa.Column('product_deletion_dialog', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('config_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('web_config')
    # ### end Alembic commands ###