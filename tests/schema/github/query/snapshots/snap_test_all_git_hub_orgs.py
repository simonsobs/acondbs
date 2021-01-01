# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[simple] 1'] = {
    'data': {
        'allGitHubOrgs': {
            'edges': [
                {
                    'node': {
                        'login': 'org1',
                        'orgId': '1'
                    }
                }
            ],
            'totalCount': 1
        }
    }
}
