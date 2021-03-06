"""rename the table admin_app_token github_admin_app_token

Revision ID: f92f99aa6fdd
Revises: 3f6526e7e5ff
Create Date: 2020-12-21 11:44:44.034531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f92f99aa6fdd'
down_revision = '3f6526e7e5ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('admin_app_token', 'github_admin_app_token')
    # op.create_table('github_admin_app_token',
    # sa.Column('token_id', sa.Integer(), nullable=False),
    # sa.Column('token', sqlalchemy_utils.types.encrypted.encrypted_type.EncryptedType(), nullable=True),
    # sa.PrimaryKeyConstraint('token_id')
    # )
    # op.drop_table('admin_app_token')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('github_admin_app_token', 'admin_app_token')
    # op.create_table('admin_app_token',
    # sa.Column('token_id', sa.INTEGER(), nullable=False),
    # sa.Column('token', sa.BLOB(), nullable=True),
    # sa.PrimaryKeyConstraint('token_id')
    # )
    # op.drop_table('github_admin_app_token')
    # ### end Alembic commands ###
