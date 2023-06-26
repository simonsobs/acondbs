# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_table_names 1'] = [
    'account_admins',
    'github_orgs',
    'github_org_memberships',
    'github_tokens',
    'github_users',
    'log',
    'product_types',
    'products',
    'product_file_paths',
    'product_relation_types',
    'product_relations',
    'attribute_unicode_text',
    'attribute_boolean',
    'attribute_integer',
    'attribute_float',
    'attribute_date',
    'attribute_date_time',
    'attribute_time',
    'field',
    'type_field_association',
    'web_config'
]
