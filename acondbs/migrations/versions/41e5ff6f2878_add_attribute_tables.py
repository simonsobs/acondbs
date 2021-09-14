"""add attribute tables

Revision ID: 41e5ff6f2878
Revises: babb78f6f6b3
Create Date: 2021-09-14 14:59:30.551921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "41e5ff6f2878"
down_revision = "babb78f6f6b3"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "attribute_date",
        sa.Column("attribute_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("value", sa.Date(), nullable=True),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["products.product_id"],
            name=op.f("fk_attribute_date_product_id_products"),
        ),
        sa.PrimaryKeyConstraint(
            "attribute_id", name=op.f("pk_attribute_date")
        ),
    )
    op.create_table(
        "attribute_date_time",
        sa.Column("attribute_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("value", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["products.product_id"],
            name=op.f("fk_attribute_date_time_product_id_products"),
        ),
        sa.PrimaryKeyConstraint(
            "attribute_id", name=op.f("pk_attribute_date_time")
        ),
    )
    op.create_table(
        "attribute_text",
        sa.Column("attribute_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("value", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["products.product_id"],
            name=op.f("fk_attribute_text_product_id_products"),
        ),
        sa.PrimaryKeyConstraint(
            "attribute_id", name=op.f("pk_attribute_text")
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("attribute_text")
    op.drop_table("attribute_date_time")
    op.drop_table("attribute_date")
    # ### end Alembic commands ###
