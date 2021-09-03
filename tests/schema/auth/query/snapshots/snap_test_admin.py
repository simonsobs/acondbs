# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[dojocat] 1'] = {
    'data': {
        'isAdmin': False
    }
}

snapshots['test_schema[no-token] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 1
                }
            ],
            'message': 'Cannot query field "isAdmin" on type "QueryPublic".'
        }
    ]
}

snapshots['test_schema[octocat] 1'] = {
    'data': {
        'isAdmin': True
    }
}

snapshots['test_schema[wrong-token] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 1
                }
            ],
            'message': 'Cannot query field "isAdmin" on type "QueryPublic".'
        }
    ]
}
