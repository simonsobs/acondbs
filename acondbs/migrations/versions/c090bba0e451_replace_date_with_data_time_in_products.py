"""replace date with data time in products

Revision ID: c090bba0e451
Revises: 4c32365bb655
Create Date: 2021-02-25 09:39:10.272222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c090bba0e451'
down_revision = '4c32365bb655'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('account_admins', schema=None) as batch_op:
        batch_op.drop_constraint('uq_account_admins_github_login', type_='unique')
        batch_op.create_unique_constraint(batch_op.f('uq_account_admins_git_hub_login'), ['git_hub_login'])

    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('time_posted', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('time_updated', sa.DateTime(), nullable=True))
        batch_op.drop_column('date_updated')
        batch_op.drop_column('date_posted')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_posted', sa.DATE(), nullable=True))
        batch_op.add_column(sa.Column('date_updated', sa.DATE(), nullable=True))
        batch_op.drop_column('time_updated')
        batch_op.drop_column('time_posted')

    with op.batch_alter_table('account_admins', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_account_admins_git_hub_login'), type_='unique')
        batch_op.create_unique_constraint('uq_account_admins_github_login', ['git_hub_login'])

    # ### end Alembic commands ###
