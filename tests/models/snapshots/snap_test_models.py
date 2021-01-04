# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_table_names 1'] = GenericRepr("dict_keys(['product_types', 'products', 'product_file_paths', 'product_relation_types', 'product_relations', 'github_tokens', 'github_orgs', 'github_users', 'github_org_memberships', 'web_config'])")
