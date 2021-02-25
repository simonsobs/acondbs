# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_define_tables_start_with_empty_db 1'] = {
    'account_admins': GenericRepr("Table('account_admins', MetaData(bind=None), Column('admin_id', INTEGER(), table=<account_admins>, primary_key=True, nullable=False), Column('git_hub_login', TEXT(), table=<account_admins>, nullable=False), schema=None)"),
    'github_org_memberships': GenericRepr("Table('github_org_memberships', MetaData(bind=None), Column('entry_id', INTEGER(), table=<github_org_memberships>, primary_key=True, nullable=False), Column('org_id', INTEGER(), ForeignKey('github_orgs.org_id'), table=<github_org_memberships>, nullable=False), Column('member_id', INTEGER(), ForeignKey('github_users.user_id'), table=<github_org_memberships>, nullable=False), schema=None)"),
    'github_orgs': GenericRepr("Table('github_orgs', MetaData(bind=None), Column('org_id', INTEGER(), table=<github_orgs>, primary_key=True, nullable=False), Column('git_hub_id', TEXT(), table=<github_orgs>, nullable=False), Column('login', TEXT(), table=<github_orgs>, nullable=False), Column('avatar_url', TEXT(), table=<github_orgs>), Column('url', TEXT(), table=<github_orgs>), schema=None)"),
    'github_tokens': GenericRepr("Table('github_tokens', MetaData(bind=None), Column('token_id', INTEGER(), table=<github_tokens>, primary_key=True, nullable=False), Column('token', BLOB(), table=<github_tokens>), Column('scope', TEXT(), table=<github_tokens>), Column('user_id', INTEGER(), ForeignKey('github_users.user_id'), table=<github_tokens>, nullable=False), Column('time_created', DATETIME(), table=<github_tokens>), schema=None)"),
    'github_users': GenericRepr("Table('github_users', MetaData(bind=None), Column('user_id', INTEGER(), table=<github_users>, primary_key=True, nullable=False), Column('git_hub_id', TEXT(), table=<github_users>, nullable=False), Column('login', TEXT(), table=<github_users>, nullable=False), Column('name', TEXT(), table=<github_users>), Column('avatar_url', TEXT(), table=<github_users>), Column('url', TEXT(), table=<github_users>), schema=None)"),
    'product_file_paths': GenericRepr("Table('product_file_paths', MetaData(bind=None), Column('path_id', INTEGER(), table=<product_file_paths>, primary_key=True, nullable=False), Column('path', TEXT(), table=<product_file_paths>), Column('note', TEXT(), table=<product_file_paths>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<product_file_paths>), schema=None)"),
    'product_relation_types': GenericRepr("Table('product_relation_types', MetaData(bind=None), Column('type_id', INTEGER(), table=<product_relation_types>, primary_key=True, nullable=False), Column('name', TEXT(), table=<product_relation_types>, nullable=False), Column('reverse_type_id', INTEGER(), ForeignKey('product_relation_types.type_id'), table=<product_relation_types>), Column('indef_article', TEXT(), table=<product_relation_types>), Column('singular', TEXT(), table=<product_relation_types>), Column('plural', TEXT(), table=<product_relation_types>), schema=None)"),
    'product_relations': GenericRepr("Table('product_relations', MetaData(bind=None), Column('relation_id', INTEGER(), table=<product_relations>, primary_key=True, nullable=False), Column('type_id', INTEGER(), ForeignKey('product_relation_types.type_id'), table=<product_relations>, nullable=False), Column('self_product_id', INTEGER(), ForeignKey('products.product_id'), table=<product_relations>, nullable=False), Column('other_product_id', INTEGER(), ForeignKey('products.product_id'), table=<product_relations>, nullable=False), Column('reverse_relation_id', INTEGER(), ForeignKey('product_relations.relation_id'), table=<product_relations>), schema=None)"),
    'product_types': GenericRepr("Table('product_types', MetaData(bind=None), Column('type_id', INTEGER(), table=<product_types>, primary_key=True, nullable=False), Column('name', TEXT(), table=<product_types>, nullable=False), Column('order', INTEGER(), table=<product_types>), Column('indef_article', TEXT(), table=<product_types>), Column('singular', TEXT(), table=<product_types>), Column('plural', TEXT(), table=<product_types>), Column('icon', TEXT(), table=<product_types>), schema=None)"),
    'products': GenericRepr("Table('products', MetaData(bind=None), Column('product_id', INTEGER(), table=<products>, primary_key=True, nullable=False), Column('type_id', INTEGER(), ForeignKey('product_types.type_id'), table=<products>, nullable=False), Column('name', TEXT(), table=<products>, nullable=False), Column('contact', TEXT(), table=<products>), Column('date_produced', DATE(), table=<products>), Column('produced_by', TEXT(), table=<products>), Column('time_posted', DATETIME(), table=<products>), Column('posted_by', TEXT(), table=<products>), Column('time_updated', DATETIME(), table=<products>), Column('updated_by', TEXT(), table=<products>), Column('note', TEXT(), table=<products>), schema=None)"),
    'web_config': GenericRepr("Table('web_config', MetaData(bind=None), Column('config_id', INTEGER(), table=<web_config>, primary_key=True, nullable=False), Column('head_title', TEXT(), table=<web_config>), Column('toolbar_title', TEXT(), table=<web_config>), Column('devtool_loadingstate', BOOLEAN(), table=<web_config>), Column('product_creation_dialog', BOOLEAN(), table=<web_config>), Column('product_update_dialog', BOOLEAN(), table=<web_config>), Column('product_deletion_dialog', BOOLEAN(), table=<web_config>), schema=None)")
}

snapshots['test_define_tables_start_with_nonempty_db 1'] = {
    'account_admins': GenericRepr("Table('account_admins', MetaData(bind=None), Column('admin_id', INTEGER(), table=<account_admins>, primary_key=True, nullable=False), Column('git_hub_login', TEXT(), table=<account_admins>, nullable=False), schema=None)"),
    'github_org_memberships': GenericRepr("Table('github_org_memberships', MetaData(bind=None), Column('entry_id', INTEGER(), table=<github_org_memberships>, primary_key=True, nullable=False), Column('org_id', INTEGER(), ForeignKey('github_orgs.org_id'), table=<github_org_memberships>, nullable=False), Column('member_id', INTEGER(), ForeignKey('github_users.user_id'), table=<github_org_memberships>, nullable=False), schema=None)"),
    'github_orgs': GenericRepr("Table('github_orgs', MetaData(bind=None), Column('org_id', INTEGER(), table=<github_orgs>, primary_key=True, nullable=False), Column('git_hub_id', TEXT(), table=<github_orgs>, nullable=False), Column('login', TEXT(), table=<github_orgs>, nullable=False), Column('avatar_url', TEXT(), table=<github_orgs>), Column('url', TEXT(), table=<github_orgs>), schema=None)"),
    'github_tokens': GenericRepr("Table('github_tokens', MetaData(bind=None), Column('token_id', INTEGER(), table=<github_tokens>, primary_key=True, nullable=False), Column('token', BLOB(), table=<github_tokens>), Column('scope', TEXT(), table=<github_tokens>), Column('user_id', INTEGER(), ForeignKey('github_users.user_id'), table=<github_tokens>, nullable=False), Column('time_created', DATETIME(), table=<github_tokens>), schema=None)"),
    'github_users': GenericRepr("Table('github_users', MetaData(bind=None), Column('user_id', INTEGER(), table=<github_users>, primary_key=True, nullable=False), Column('git_hub_id', TEXT(), table=<github_users>, nullable=False), Column('login', TEXT(), table=<github_users>, nullable=False), Column('name', TEXT(), table=<github_users>), Column('avatar_url', TEXT(), table=<github_users>), Column('url', TEXT(), table=<github_users>), schema=None)"),
    'product_file_paths': GenericRepr("Table('product_file_paths', MetaData(bind=None), Column('path_id', INTEGER(), table=<product_file_paths>, primary_key=True, nullable=False), Column('path', TEXT(), table=<product_file_paths>), Column('note', TEXT(), table=<product_file_paths>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<product_file_paths>), schema=None)"),
    'product_relation_types': GenericRepr("Table('product_relation_types', MetaData(bind=None), Column('type_id', INTEGER(), table=<product_relation_types>, primary_key=True, nullable=False), Column('name', TEXT(), table=<product_relation_types>, nullable=False), Column('reverse_type_id', INTEGER(), ForeignKey('product_relation_types.type_id'), table=<product_relation_types>), Column('indef_article', TEXT(), table=<product_relation_types>), Column('singular', TEXT(), table=<product_relation_types>), Column('plural', TEXT(), table=<product_relation_types>), schema=None)"),
    'product_relations': GenericRepr("Table('product_relations', MetaData(bind=None), Column('relation_id', INTEGER(), table=<product_relations>, primary_key=True, nullable=False), Column('type_id', INTEGER(), ForeignKey('product_relation_types.type_id'), table=<product_relations>, nullable=False), Column('self_product_id', INTEGER(), ForeignKey('products.product_id'), table=<product_relations>, nullable=False), Column('other_product_id', INTEGER(), ForeignKey('products.product_id'), table=<product_relations>, nullable=False), Column('reverse_relation_id', INTEGER(), ForeignKey('product_relations.relation_id'), table=<product_relations>), schema=None)"),
    'product_types': GenericRepr("Table('product_types', MetaData(bind=None), Column('type_id', INTEGER(), table=<product_types>, primary_key=True, nullable=False), Column('name', TEXT(), table=<product_types>, nullable=False), Column('order', INTEGER(), table=<product_types>), Column('indef_article', TEXT(), table=<product_types>), Column('singular', TEXT(), table=<product_types>), Column('plural', TEXT(), table=<product_types>), Column('icon', TEXT(), table=<product_types>), schema=None)"),
    'products': GenericRepr("Table('products', MetaData(bind=None), Column('product_id', INTEGER(), table=<products>, primary_key=True, nullable=False), Column('type_id', INTEGER(), ForeignKey('product_types.type_id'), table=<products>, nullable=False), Column('name', TEXT(), table=<products>, nullable=False), Column('contact', TEXT(), table=<products>), Column('date_produced', DATE(), table=<products>), Column('produced_by', TEXT(), table=<products>), Column('time_posted', DATETIME(), table=<products>), Column('posted_by', TEXT(), table=<products>), Column('time_updated', DATETIME(), table=<products>), Column('updated_by', TEXT(), table=<products>), Column('note', TEXT(), table=<products>), schema=None)"),
    'web_config': GenericRepr("Table('web_config', MetaData(bind=None), Column('config_id', INTEGER(), table=<web_config>, primary_key=True, nullable=False), Column('head_title', TEXT(), table=<web_config>), Column('toolbar_title', TEXT(), table=<web_config>), Column('devtool_loadingstate', BOOLEAN(), table=<web_config>), Column('product_creation_dialog', BOOLEAN(), table=<web_config>), Column('product_update_dialog', BOOLEAN(), table=<web_config>), Column('product_deletion_dialog', BOOLEAN(), table=<web_config>), schema=None)")
}
