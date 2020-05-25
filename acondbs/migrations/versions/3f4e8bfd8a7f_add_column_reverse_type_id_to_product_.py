"""add column reverse_type_id to product_relation_types

Revision ID: 3f4e8bfd8a7f
Revises: d8afc036053a
Create Date: 2020-05-24 20:31:48.005028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f4e8bfd8a7f'
down_revision = 'd8afc036053a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product_relation_types', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reverse_type_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_product_relation_types_reverse_type_id_type_id', 'product_relation_types', ['reverse_type_id'], ['type_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product_relation_types', schema=None) as batch_op:
        batch_op.drop_constraint('fk_product_relation_types_reverse_type_id_type_id', type_='foreignkey')
        batch_op.drop_column('reverse_type_id')

    # ### end Alembic commands ###
