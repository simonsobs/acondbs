# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_error[add] 1'] = {
    'data': {
        'allGitHubAdminAppTokens': {
            'edges': [
                {
                    'node': {
                        'tokenId': '1',
                        'tokenMasked': 'XXXXXXXXXXXXXXX'
                    }
                }
            ],
            'totalCount': 1
        }
    }
}

snapshots['test_schema_success[add] 1'] = {
    'data': {
        'addGitHubAdminAppToken': {
            'ok': True
        }
    }
}

snapshots['test_schema_success[add] 2'] = {
    'data': {
        'allGitHubAdminAppTokens': {
            'edges': [
                {
                    'node': {
                        'tokenId': '1',
                        'tokenMasked': 'XXXXXXXXXXXXXXX'
                    }
                },
                {
                    'node': {
                        'tokenId': '2',
                        'tokenMasked': 'XXXXXXXXXXXXXXX'
                    }
                }
            ],
            'totalCount': 2
        }
    }
}
