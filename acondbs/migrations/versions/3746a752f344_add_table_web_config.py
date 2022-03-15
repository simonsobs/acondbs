"""add table web_config

Revision ID: 3746a752f344
Revises: 63790f65e724
Create Date: 2021-10-27 16:20:22.446644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3746a752f344'
down_revision = '63790f65e724'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('web_config',
    sa.Column('id_', sa.Integer(), nullable=False),
    sa.Column('json', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id_', name=op.f('pk_web_config'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('web_config')
    # ### end Alembic commands ###