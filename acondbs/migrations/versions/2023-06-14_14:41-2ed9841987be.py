"""Initial migration.

Revision ID: 2ed9841987be
Revises: 
Create Date: 2023-06-14 14:41:32.587052

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
revision = '2ed9841987be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account_admins',
    sa.Column('admin_id', sa.Integer(), nullable=False),
    sa.Column('git_hub_login', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('admin_id', name=op.f('pk_account_admins')),
    sa.UniqueConstraint('git_hub_login', name=op.f('uq_account_admins_git_hub_login'))
    )
    op.create_table('field',
    sa.Column('field_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.UnicodeText(), nullable=False),
    sa.Column('type_', sa.Enum('UnicodeText', 'Boolean', 'Integer', 'Float', 'Date', 'DateTime', 'Time', name='fieldtype'), nullable=False),
    sa.PrimaryKeyConstraint('field_id', name=op.f('pk_field'))
    )
    op.create_table('github_orgs',
    sa.Column('org_id', sa.Integer(), nullable=False),
    sa.Column('git_hub_id', sa.Text(), nullable=False),
    sa.Column('login', sa.Text(), nullable=False),
    sa.Column('avatar_url', sa.Text(), nullable=True),
    sa.Column('url', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('org_id', name=op.f('pk_github_orgs')),
    sa.UniqueConstraint('git_hub_id', name=op.f('uq_github_orgs_git_hub_id'))
    )
    op.create_table('github_users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('git_hub_id', sa.Text(), nullable=False),
    sa.Column('login', sa.Text(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('avatar_url', sa.Text(), nullable=True),
    sa.Column('url', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('user_id', name=op.f('pk_github_users')),
    sa.UniqueConstraint('git_hub_id', name=op.f('uq_github_users_git_hub_id')),
    sa.UniqueConstraint('login', name=op.f('uq_github_users_login'))
    )
    op.create_table('log',
    sa.Column('id_', sa.Integer(), nullable=False),
    sa.Column('level', sa.Text(), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id_', name=op.f('pk_log'))
    )
    op.create_table('product_relation_types',
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('reverse_type_id', sa.Integer(), nullable=True),
    sa.Column('indef_article', sa.Text(), nullable=True),
    sa.Column('singular', sa.Text(), nullable=True),
    sa.Column('plural', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['reverse_type_id'], ['product_relation_types.type_id'], name=op.f('fk_product_relation_types_reverse_type_id_product_relation_types')),
    sa.PrimaryKeyConstraint('type_id', name=op.f('pk_product_relation_types'))
    )
    with op.batch_alter_table('product_relation_types', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_product_relation_types_name'), ['name'], unique=True)

    op.create_table('product_types',
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('indef_article', sa.Text(), nullable=True),
    sa.Column('singular', sa.Text(), nullable=True),
    sa.Column('plural', sa.Text(), nullable=True),
    sa.Column('icon', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('type_id', name=op.f('pk_product_types'))
    )
    with op.batch_alter_table('product_types', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_product_types_name'), ['name'], unique=True)

    op.create_table('web_config',
    sa.Column('id_', sa.Integer(), nullable=False),
    sa.Column('json', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id_', name=op.f('pk_web_config'))
    )
    op.create_table('github_org_memberships',
    sa.Column('entry_id', sa.Integer(), nullable=False),
    sa.Column('org_id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['member_id'], ['github_users.user_id'], name=op.f('fk_github_org_memberships_member_id_github_users')),
    sa.ForeignKeyConstraint(['org_id'], ['github_orgs.org_id'], name=op.f('fk_github_org_memberships_org_id_github_orgs')),
    sa.PrimaryKeyConstraint('entry_id', name=op.f('pk_github_org_memberships'))
    )
    op.create_table('github_tokens',
    sa.Column('token_id', sa.Integer(), nullable=False),
    sa.Column('token', sqlalchemy_utils.types.encrypted.encrypted_type.EncryptedType(), nullable=True),
    sa.Column('scope', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('time_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['github_users.user_id'], name=op.f('fk_github_tokens_user_id_github_users')),
    sa.PrimaryKeyConstraint('token_id', name=op.f('pk_github_tokens'))
    )
    op.create_table('products',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('time_posted', sa.DateTime(), nullable=True),
    sa.Column('posting_git_hub_user_id', sa.Integer(), nullable=True),
    sa.Column('time_updated', sa.DateTime(), nullable=True),
    sa.Column('updating_git_hub_user_id', sa.Integer(), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['posting_git_hub_user_id'], ['github_users.user_id'], name=op.f('fk_products_posting_git_hub_user_id_github_users')),
    sa.ForeignKeyConstraint(['type_id'], ['product_types.type_id'], name=op.f('fk_products_type_id_product_types')),
    sa.ForeignKeyConstraint(['updating_git_hub_user_id'], ['github_users.user_id'], name=op.f('fk_products_updating_git_hub_user_id_github_users')),
    sa.PrimaryKeyConstraint('product_id', name=op.f('pk_products')),
    sa.UniqueConstraint('type_id', 'name', name='_type_id_name')
    )
    op.create_table('type_field_association',
    sa.Column('iid', sa.Integer(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('field_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['field_id'], ['field.field_id'], name=op.f('fk_type_field_association_field_id_field')),
    sa.ForeignKeyConstraint(['type_id'], ['product_types.type_id'], name=op.f('fk_type_field_association_type_id_product_types')),
    sa.PrimaryKeyConstraint('iid', name=op.f('pk_type_field_association')),
    sa.UniqueConstraint('type_id', 'field_id', name='_type_field')
    )
    op.create_table('attribute_boolean',
    sa.Column('iid', sa.Integer(), nullable=False),
    sa.Column('value', sa.Boolean(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('type_field_association_iid', sa.Integer(), nullable=False),
    sa.Column('field_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['field_id'], ['field.field_id'], name=op.f('fk_attribute_boolean_field_id_field')),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], name=op.f('fk_attribute_boolean_product_id_products')),
    sa.ForeignKeyConstraint(['type_field_association_iid'], ['type_field_association.iid'], name=op.f('fk_attribute_boolean_type_field_association_iid_type_field_association')),
    sa.PrimaryKeyConstraint('iid', name=op.f('pk_attribute_boolean'))
    )
    op.create_table('attribute_date',
    sa.Column('iid', sa.Integer(), nullable=False),
    sa.Column('value', sa.Date(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('type_field_association_iid', sa.Integer(), nullable=False),
    sa.Column('field_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['field_id'], ['field.field_id'], name=op.f('fk_attribute_date_field_id_field')),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], name=op.f('fk_attribute_date_product_id_products')),
    sa.ForeignKeyConstraint(['type_field_association_iid'], ['type_field_association.iid'], name=op.f('fk_attribute_date_type_field_association_iid_type_field_association')),
    sa.PrimaryKeyConstraint('iid', name=op.f('pk_attribute_date'))
    )
    op.create_table('attribute_date_time',
    sa.Column('iid', sa.Integer(), nullable=False),
    sa.Column('value', sa.DateTime(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('type_field_association_iid', sa.Integer(), nullable=False),
    sa.Column('field_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['field_id'], ['field.field_id'], name=op.f('fk_attribute_date_time_field_id_field')),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], name=op.f('fk_attribute_date_time_product_id_products')),
    sa.ForeignKeyConstraint(['type_field_association_iid'], ['type_field_association.iid'], name=op.f('fk_attribute_date_time_type_field_association_iid_type_field_association')),
    sa.PrimaryKeyConstraint('iid', name=op.f('pk_attribute_date_time'))
    )
    op.create_table('attribute_float',
    sa.Column('iid', sa.Integer(), nullable=False),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('type_field_association_iid', sa.Integer(), nullable=False),
    sa.Column('field_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['field_id'], ['field.field_id'], name=op.f('fk_attribute_float_field_id_field')),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], name=op.f('fk_attribute_float_product_id_products')),
    sa.ForeignKeyConstraint(['type_field_association_iid'], ['type_field_association.iid'], name=op.f('fk_attribute_float_type_field_association_iid_type_field_association')),
    sa.PrimaryKeyConstraint('iid', name=op.f('pk_attribute_float'))
    )
    op.create_table('attribute_integer',
    sa.Column('iid', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('type_field_association_iid', sa.Integer(), nullable=False),
    sa.Column('field_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['field_id'], ['field.field_id'], name=op.f('fk_attribute_integer_field_id_field')),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], name=op.f('fk_attribute_integer_product_id_products')),
    sa.ForeignKeyConstraint(['type_field_association_iid'], ['type_field_association.iid'], name=op.f('fk_attribute_integer_type_field_association_iid_type_field_association')),
    sa.PrimaryKeyConstraint('iid', name=op.f('pk_attribute_integer'))
    )
    op.create_table('attribute_time',
    sa.Column('iid', sa.Integer(), nullable=False),
    sa.Column('value', sa.Time(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('type_field_association_iid', sa.Integer(), nullable=False),
    sa.Column('field_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['field_id'], ['field.field_id'], name=op.f('fk_attribute_time_field_id_field')),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], name=op.f('fk_attribute_time_product_id_products')),
    sa.ForeignKeyConstraint(['type_field_association_iid'], ['type_field_association.iid'], name=op.f('fk_attribute_time_type_field_association_iid_type_field_association')),
    sa.PrimaryKeyConstraint('iid', name=op.f('pk_attribute_time'))
    )
    op.create_table('attribute_unicode_text',
    sa.Column('iid', sa.Integer(), nullable=False),
    sa.Column('value', sa.UnicodeText(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('type_field_association_iid', sa.Integer(), nullable=False),
    sa.Column('field_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['field_id'], ['field.field_id'], name=op.f('fk_attribute_unicode_text_field_id_field')),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], name=op.f('fk_attribute_unicode_text_product_id_products')),
    sa.ForeignKeyConstraint(['type_field_association_iid'], ['type_field_association.iid'], name=op.f('fk_attribute_unicode_text_type_field_association_iid_type_field_association')),
    sa.PrimaryKeyConstraint('iid', name=op.f('pk_attribute_unicode_text'))
    )
    op.create_table('product_file_paths',
    sa.Column('path_id', sa.Integer(), nullable=False),
    sa.Column('path', sa.Text(), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], name=op.f('fk_product_file_paths_product_id_products')),
    sa.PrimaryKeyConstraint('path_id', name=op.f('pk_product_file_paths'))
    )
    op.create_table('product_relations',
    sa.Column('relation_id', sa.Integer(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('self_product_id', sa.Integer(), nullable=False),
    sa.Column('other_product_id', sa.Integer(), nullable=False),
    sa.Column('reverse_relation_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['other_product_id'], ['products.product_id'], name=op.f('fk_product_relations_other_product_id_products')),
    sa.ForeignKeyConstraint(['reverse_relation_id'], ['product_relations.relation_id'], name=op.f('fk_product_relations_reverse_relation_id_product_relations')),
    sa.ForeignKeyConstraint(['self_product_id'], ['products.product_id'], name=op.f('fk_product_relations_self_product_id_products')),
    sa.ForeignKeyConstraint(['type_id'], ['product_relation_types.type_id'], name=op.f('fk_product_relations_type_id_product_relation_types')),
    sa.PrimaryKeyConstraint('relation_id', name=op.f('pk_product_relations')),
    sa.UniqueConstraint('type_id', 'self_product_id', 'other_product_id', name='_type_id_self_product_id_other_product_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_relations')
    op.drop_table('product_file_paths')
    op.drop_table('attribute_unicode_text')
    op.drop_table('attribute_time')
    op.drop_table('attribute_integer')
    op.drop_table('attribute_float')
    op.drop_table('attribute_date_time')
    op.drop_table('attribute_date')
    op.drop_table('attribute_boolean')
    op.drop_table('type_field_association')
    op.drop_table('products')
    op.drop_table('github_tokens')
    op.drop_table('github_org_memberships')
    op.drop_table('web_config')
    with op.batch_alter_table('product_types', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_product_types_name'))

    op.drop_table('product_types')
    with op.batch_alter_table('product_relation_types', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_product_relation_types_name'))

    op.drop_table('product_relation_types')
    op.drop_table('log')
    op.drop_table('github_users')
    op.drop_table('github_orgs')
    op.drop_table('field')
    op.drop_table('account_admins')
    # ### end Alembic commands ###
