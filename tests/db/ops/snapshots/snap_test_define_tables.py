# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots['test_define_tables_start_with_empty_db 1'] = {
    'account_admins': GenericRepr(
        "Table('account_admins', MetaData(), Column('admin_id', INTEGER(), table=<account_admins>, primary_key=True, nullable=False), Column('git_hub_login', TEXT(), table=<account_admins>, nullable=False), schema=None)"
    ),
    'attribute_boolean': GenericRepr(
        "Table('attribute_boolean', MetaData(), Column('iid', INTEGER(), table=<attribute_boolean>, primary_key=True, nullable=False), Column('value', BOOLEAN(), table=<attribute_boolean>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<attribute_boolean>, nullable=False), Column('type_field_association_iid', INTEGER(), ForeignKey('type_field_association.iid'), table=<attribute_boolean>, nullable=False), Column('field_id', INTEGER(), ForeignKey('field.field_id'), table=<attribute_boolean>, nullable=False), schema=None)"
    ),
    'attribute_date': GenericRepr(
        "Table('attribute_date', MetaData(), Column('iid', INTEGER(), table=<attribute_date>, primary_key=True, nullable=False), Column('value', DATE(), table=<attribute_date>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<attribute_date>, nullable=False), Column('type_field_association_iid', INTEGER(), ForeignKey('type_field_association.iid'), table=<attribute_date>, nullable=False), Column('field_id', INTEGER(), ForeignKey('field.field_id'), table=<attribute_date>, nullable=False), schema=None)"
    ),
    'attribute_date_time': GenericRepr(
        "Table('attribute_date_time', MetaData(), Column('iid', INTEGER(), table=<attribute_date_time>, primary_key=True, nullable=False), Column('value', DATETIME(), table=<attribute_date_time>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<attribute_date_time>, nullable=False), Column('type_field_association_iid', INTEGER(), ForeignKey('type_field_association.iid'), table=<attribute_date_time>, nullable=False), Column('field_id', INTEGER(), ForeignKey('field.field_id'), table=<attribute_date_time>, nullable=False), schema=None)"
    ),
    'attribute_float': GenericRepr(
        "Table('attribute_float', MetaData(), Column('iid', INTEGER(), table=<attribute_float>, primary_key=True, nullable=False), Column('value', FLOAT(), table=<attribute_float>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<attribute_float>, nullable=False), Column('type_field_association_iid', INTEGER(), ForeignKey('type_field_association.iid'), table=<attribute_float>, nullable=False), Column('field_id', INTEGER(), ForeignKey('field.field_id'), table=<attribute_float>, nullable=False), schema=None)"
    ),
    'attribute_integer': GenericRepr(
        "Table('attribute_integer', MetaData(), Column('iid', INTEGER(), table=<attribute_integer>, primary_key=True, nullable=False), Column('value', INTEGER(), table=<attribute_integer>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<attribute_integer>, nullable=False), Column('type_field_association_iid', INTEGER(), ForeignKey('type_field_association.iid'), table=<attribute_integer>, nullable=False), Column('field_id', INTEGER(), ForeignKey('field.field_id'), table=<attribute_integer>, nullable=False), schema=None)"
    ),
    'attribute_time': GenericRepr(
        "Table('attribute_time', MetaData(), Column('iid', INTEGER(), table=<attribute_time>, primary_key=True, nullable=False), Column('value', TIME(), table=<attribute_time>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<attribute_time>, nullable=False), Column('type_field_association_iid', INTEGER(), ForeignKey('type_field_association.iid'), table=<attribute_time>, nullable=False), Column('field_id', INTEGER(), ForeignKey('field.field_id'), table=<attribute_time>, nullable=False), schema=None)"
    ),
    'attribute_unicode_text': GenericRepr(
        "Table('attribute_unicode_text', MetaData(), Column('iid', INTEGER(), table=<attribute_unicode_text>, primary_key=True, nullable=False), Column('value', TEXT(), table=<attribute_unicode_text>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<attribute_unicode_text>, nullable=False), Column('type_field_association_iid', INTEGER(), ForeignKey('type_field_association.iid'), table=<attribute_unicode_text>, nullable=False), Column('field_id', INTEGER(), ForeignKey('field.field_id'), table=<attribute_unicode_text>, nullable=False), schema=None)"
    ),
    'field': GenericRepr(
        "Table('field', MetaData(), Column('field_id', INTEGER(), table=<field>, primary_key=True, nullable=False), Column('name', TEXT(), table=<field>, nullable=False), Column('type_', VARCHAR(length=11), table=<field>, nullable=False), schema=None)"
    ),
    'github_org_memberships': GenericRepr(
        "Table('github_org_memberships', MetaData(), Column('entry_id', INTEGER(), table=<github_org_memberships>, primary_key=True, nullable=False), Column('org_id', INTEGER(), ForeignKey('github_orgs.org_id'), table=<github_org_memberships>, nullable=False), Column('member_id', INTEGER(), ForeignKey('github_users.user_id'), table=<github_org_memberships>, nullable=False), schema=None)"
    ),
    'github_orgs': GenericRepr(
        "Table('github_orgs', MetaData(), Column('org_id', INTEGER(), table=<github_orgs>, primary_key=True, nullable=False), Column('git_hub_id', TEXT(), table=<github_orgs>, nullable=False), Column('login', TEXT(), table=<github_orgs>, nullable=False), Column('avatar_url', TEXT(), table=<github_orgs>), Column('url', TEXT(), table=<github_orgs>), schema=None)"
    ),
    'github_tokens': GenericRepr(
        "Table('github_tokens', MetaData(), Column('token_id', INTEGER(), table=<github_tokens>, primary_key=True, nullable=False), Column('token', BLOB(), table=<github_tokens>), Column('scope', TEXT(), table=<github_tokens>), Column('user_id', INTEGER(), ForeignKey('github_users.user_id'), table=<github_tokens>, nullable=False), Column('time_created', DATETIME(), table=<github_tokens>), schema=None)"
    ),
    'github_users': GenericRepr(
        "Table('github_users', MetaData(), Column('user_id', INTEGER(), table=<github_users>, primary_key=True, nullable=False), Column('git_hub_id', TEXT(), table=<github_users>, nullable=False), Column('login', TEXT(), table=<github_users>, nullable=False), Column('name', TEXT(), table=<github_users>), Column('avatar_url', TEXT(), table=<github_users>), Column('url', TEXT(), table=<github_users>), schema=None)"
    ),
    'log': GenericRepr(
        "Table('log', MetaData(), Column('id_', INTEGER(), table=<log>, primary_key=True, nullable=False), Column('level', TEXT(), table=<log>), Column('message', TEXT(), table=<log>), Column('time', DATETIME(), table=<log>), schema=None)"
    ),
    'product_file_paths': GenericRepr(
        "Table('product_file_paths', MetaData(), Column('path_id', INTEGER(), table=<product_file_paths>, primary_key=True, nullable=False), Column('path', TEXT(), table=<product_file_paths>), Column('note', TEXT(), table=<product_file_paths>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<product_file_paths>), schema=None)"
    ),
    'product_relation_types': GenericRepr(
        "Table('product_relation_types', MetaData(), Column('type_id', INTEGER(), table=<product_relation_types>, primary_key=True, nullable=False), Column('name', TEXT(), table=<product_relation_types>, nullable=False), Column('reverse_type_id', INTEGER(), ForeignKey('product_relation_types.type_id'), table=<product_relation_types>), Column('indef_article', TEXT(), table=<product_relation_types>), Column('singular', TEXT(), table=<product_relation_types>), Column('plural', TEXT(), table=<product_relation_types>), schema=None)"
    ),
    'product_relations': GenericRepr(
        "Table('product_relations', MetaData(), Column('relation_id', INTEGER(), table=<product_relations>, primary_key=True, nullable=False), Column('type_id', INTEGER(), ForeignKey('product_relation_types.type_id'), table=<product_relations>, nullable=False), Column('self_product_id', INTEGER(), ForeignKey('products.product_id'), table=<product_relations>, nullable=False), Column('other_product_id', INTEGER(), ForeignKey('products.product_id'), table=<product_relations>, nullable=False), Column('reverse_relation_id', INTEGER(), ForeignKey('product_relations.relation_id'), table=<product_relations>), schema=None)"
    ),
    'product_types': GenericRepr(
        "Table('product_types', MetaData(), Column('type_id', INTEGER(), table=<product_types>, primary_key=True, nullable=False), Column('name', TEXT(), table=<product_types>, nullable=False), Column('order', INTEGER(), table=<product_types>), Column('indef_article', TEXT(), table=<product_types>), Column('singular', TEXT(), table=<product_types>), Column('plural', TEXT(), table=<product_types>), Column('icon', TEXT(), table=<product_types>), schema=None)"
    ),
    'products': GenericRepr(
        "Table('products', MetaData(), Column('product_id', INTEGER(), table=<products>, primary_key=True, nullable=False), Column('type_id', INTEGER(), ForeignKey('product_types.type_id'), table=<products>, nullable=False), Column('name', TEXT(), table=<products>, nullable=False), Column('time_posted', DATETIME(), table=<products>), Column('posting_git_hub_user_id', INTEGER(), ForeignKey('github_users.user_id'), table=<products>), Column('time_updated', DATETIME(), table=<products>), Column('updating_git_hub_user_id', INTEGER(), ForeignKey('github_users.user_id'), table=<products>), Column('note', TEXT(), table=<products>), schema=None)"
    ),
    'type_field_association': GenericRepr(
        "Table('type_field_association', MetaData(), Column('iid', INTEGER(), table=<type_field_association>, primary_key=True, nullable=False), Column('order', INTEGER(), table=<type_field_association>), Column('type_id', INTEGER(), ForeignKey('product_types.type_id'), table=<type_field_association>, nullable=False), Column('field_id', INTEGER(), ForeignKey('field.field_id'), table=<type_field_association>, nullable=False), schema=None)"
    ),
    'web_config': GenericRepr(
        "Table('web_config', MetaData(), Column('id_', INTEGER(), table=<web_config>, primary_key=True, nullable=False), Column('json', TEXT(), table=<web_config>), schema=None)"
    ),
}

snapshots['test_define_tables_start_with_nonempty_db 1'] = {
    'account_admins': GenericRepr(
        "Table('account_admins', MetaData(), Column('admin_id', INTEGER(), table=<account_admins>, primary_key=True, nullable=False), Column('git_hub_login', TEXT(), table=<account_admins>, nullable=False), schema=None)"
    ),
    'attribute_boolean': GenericRepr(
        "Table('attribute_boolean', MetaData(), Column('iid', INTEGER(), table=<attribute_boolean>, primary_key=True, nullable=False), Column('value', BOOLEAN(), table=<attribute_boolean>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<attribute_boolean>, nullable=False), Column('type_field_association_iid', INTEGER(), ForeignKey('type_field_association.iid'), table=<attribute_boolean>, nullable=False), Column('field_id', INTEGER(), ForeignKey('field.field_id'), table=<attribute_boolean>, nullable=False), schema=None)"
    ),
    'attribute_date': GenericRepr(
        "Table('attribute_date', MetaData(), Column('iid', INTEGER(), table=<attribute_date>, primary_key=True, nullable=False), Column('value', DATE(), table=<attribute_date>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<attribute_date>, nullable=False), Column('type_field_association_iid', INTEGER(), ForeignKey('type_field_association.iid'), table=<attribute_date>, nullable=False), Column('field_id', INTEGER(), ForeignKey('field.field_id'), table=<attribute_date>, nullable=False), schema=None)"
    ),
    'attribute_date_time': GenericRepr(
        "Table('attribute_date_time', MetaData(), Column('iid', INTEGER(), table=<attribute_date_time>, primary_key=True, nullable=False), Column('value', DATETIME(), table=<attribute_date_time>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<attribute_date_time>, nullable=False), Column('type_field_association_iid', INTEGER(), ForeignKey('type_field_association.iid'), table=<attribute_date_time>, nullable=False), Column('field_id', INTEGER(), ForeignKey('field.field_id'), table=<attribute_date_time>, nullable=False), schema=None)"
    ),
    'attribute_float': GenericRepr(
        "Table('attribute_float', MetaData(), Column('iid', INTEGER(), table=<attribute_float>, primary_key=True, nullable=False), Column('value', FLOAT(), table=<attribute_float>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<attribute_float>, nullable=False), Column('type_field_association_iid', INTEGER(), ForeignKey('type_field_association.iid'), table=<attribute_float>, nullable=False), Column('field_id', INTEGER(), ForeignKey('field.field_id'), table=<attribute_float>, nullable=False), schema=None)"
    ),
    'attribute_integer': GenericRepr(
        "Table('attribute_integer', MetaData(), Column('iid', INTEGER(), table=<attribute_integer>, primary_key=True, nullable=False), Column('value', INTEGER(), table=<attribute_integer>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<attribute_integer>, nullable=False), Column('type_field_association_iid', INTEGER(), ForeignKey('type_field_association.iid'), table=<attribute_integer>, nullable=False), Column('field_id', INTEGER(), ForeignKey('field.field_id'), table=<attribute_integer>, nullable=False), schema=None)"
    ),
    'attribute_time': GenericRepr(
        "Table('attribute_time', MetaData(), Column('iid', INTEGER(), table=<attribute_time>, primary_key=True, nullable=False), Column('value', TIME(), table=<attribute_time>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<attribute_time>, nullable=False), Column('type_field_association_iid', INTEGER(), ForeignKey('type_field_association.iid'), table=<attribute_time>, nullable=False), Column('field_id', INTEGER(), ForeignKey('field.field_id'), table=<attribute_time>, nullable=False), schema=None)"
    ),
    'attribute_unicode_text': GenericRepr(
        "Table('attribute_unicode_text', MetaData(), Column('iid', INTEGER(), table=<attribute_unicode_text>, primary_key=True, nullable=False), Column('value', TEXT(), table=<attribute_unicode_text>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<attribute_unicode_text>, nullable=False), Column('type_field_association_iid', INTEGER(), ForeignKey('type_field_association.iid'), table=<attribute_unicode_text>, nullable=False), Column('field_id', INTEGER(), ForeignKey('field.field_id'), table=<attribute_unicode_text>, nullable=False), schema=None)"
    ),
    'field': GenericRepr(
        "Table('field', MetaData(), Column('field_id', INTEGER(), table=<field>, primary_key=True, nullable=False), Column('name', TEXT(), table=<field>, nullable=False), Column('type_', VARCHAR(length=11), table=<field>, nullable=False), schema=None)"
    ),
    'github_org_memberships': GenericRepr(
        "Table('github_org_memberships', MetaData(), Column('entry_id', INTEGER(), table=<github_org_memberships>, primary_key=True, nullable=False), Column('org_id', INTEGER(), ForeignKey('github_orgs.org_id'), table=<github_org_memberships>, nullable=False), Column('member_id', INTEGER(), ForeignKey('github_users.user_id'), table=<github_org_memberships>, nullable=False), schema=None)"
    ),
    'github_orgs': GenericRepr(
        "Table('github_orgs', MetaData(), Column('org_id', INTEGER(), table=<github_orgs>, primary_key=True, nullable=False), Column('git_hub_id', TEXT(), table=<github_orgs>, nullable=False), Column('login', TEXT(), table=<github_orgs>, nullable=False), Column('avatar_url', TEXT(), table=<github_orgs>), Column('url', TEXT(), table=<github_orgs>), schema=None)"
    ),
    'github_tokens': GenericRepr(
        "Table('github_tokens', MetaData(), Column('token_id', INTEGER(), table=<github_tokens>, primary_key=True, nullable=False), Column('token', BLOB(), table=<github_tokens>), Column('scope', TEXT(), table=<github_tokens>), Column('user_id', INTEGER(), ForeignKey('github_users.user_id'), table=<github_tokens>, nullable=False), Column('time_created', DATETIME(), table=<github_tokens>), schema=None)"
    ),
    'github_users': GenericRepr(
        "Table('github_users', MetaData(), Column('user_id', INTEGER(), table=<github_users>, primary_key=True, nullable=False), Column('git_hub_id', TEXT(), table=<github_users>, nullable=False), Column('login', TEXT(), table=<github_users>, nullable=False), Column('name', TEXT(), table=<github_users>), Column('avatar_url', TEXT(), table=<github_users>), Column('url', TEXT(), table=<github_users>), schema=None)"
    ),
    'log': GenericRepr(
        "Table('log', MetaData(), Column('id_', INTEGER(), table=<log>, primary_key=True, nullable=False), Column('level', TEXT(), table=<log>), Column('message', TEXT(), table=<log>), Column('time', DATETIME(), table=<log>), schema=None)"
    ),
    'product_file_paths': GenericRepr(
        "Table('product_file_paths', MetaData(), Column('path_id', INTEGER(), table=<product_file_paths>, primary_key=True, nullable=False), Column('path', TEXT(), table=<product_file_paths>), Column('note', TEXT(), table=<product_file_paths>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<product_file_paths>), schema=None)"
    ),
    'product_relation_types': GenericRepr(
        "Table('product_relation_types', MetaData(), Column('type_id', INTEGER(), table=<product_relation_types>, primary_key=True, nullable=False), Column('name', TEXT(), table=<product_relation_types>, nullable=False), Column('reverse_type_id', INTEGER(), ForeignKey('product_relation_types.type_id'), table=<product_relation_types>), Column('indef_article', TEXT(), table=<product_relation_types>), Column('singular', TEXT(), table=<product_relation_types>), Column('plural', TEXT(), table=<product_relation_types>), schema=None)"
    ),
    'product_relations': GenericRepr(
        "Table('product_relations', MetaData(), Column('relation_id', INTEGER(), table=<product_relations>, primary_key=True, nullable=False), Column('type_id', INTEGER(), ForeignKey('product_relation_types.type_id'), table=<product_relations>, nullable=False), Column('self_product_id', INTEGER(), ForeignKey('products.product_id'), table=<product_relations>, nullable=False), Column('other_product_id', INTEGER(), ForeignKey('products.product_id'), table=<product_relations>, nullable=False), Column('reverse_relation_id', INTEGER(), ForeignKey('product_relations.relation_id'), table=<product_relations>), schema=None)"
    ),
    'product_types': GenericRepr(
        "Table('product_types', MetaData(), Column('type_id', INTEGER(), table=<product_types>, primary_key=True, nullable=False), Column('name', TEXT(), table=<product_types>, nullable=False), Column('order', INTEGER(), table=<product_types>), Column('indef_article', TEXT(), table=<product_types>), Column('singular', TEXT(), table=<product_types>), Column('plural', TEXT(), table=<product_types>), Column('icon', TEXT(), table=<product_types>), schema=None)"
    ),
    'products': GenericRepr(
        "Table('products', MetaData(), Column('product_id', INTEGER(), table=<products>, primary_key=True, nullable=False), Column('type_id', INTEGER(), ForeignKey('product_types.type_id'), table=<products>, nullable=False), Column('name', TEXT(), table=<products>, nullable=False), Column('time_posted', DATETIME(), table=<products>), Column('posting_git_hub_user_id', INTEGER(), ForeignKey('github_users.user_id'), table=<products>), Column('time_updated', DATETIME(), table=<products>), Column('updating_git_hub_user_id', INTEGER(), ForeignKey('github_users.user_id'), table=<products>), Column('note', TEXT(), table=<products>), schema=None)"
    ),
    'type_field_association': GenericRepr(
        "Table('type_field_association', MetaData(), Column('iid', INTEGER(), table=<type_field_association>, primary_key=True, nullable=False), Column('order', INTEGER(), table=<type_field_association>), Column('type_id', INTEGER(), ForeignKey('product_types.type_id'), table=<type_field_association>, nullable=False), Column('field_id', INTEGER(), ForeignKey('field.field_id'), table=<type_field_association>, nullable=False), schema=None)"
    ),
    'web_config': GenericRepr(
        "Table('web_config', MetaData(), Column('id_', INTEGER(), table=<web_config>, primary_key=True, nullable=False), Column('json', TEXT(), table=<web_config>), schema=None)"
    ),
}
