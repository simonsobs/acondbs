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
    'attribute_unicode_text',
    'attribute_boolean',
    'attribute_integer',
    'attribute_float',
    'attribute_date',
    'attribute_date_time',
    'attribute_time',
    'field',
    'products',
    'product_file_paths',
    'product_relations',
    'product_relation_types',
    'product_types',
    'type_field_association',
    'web_config'
]
