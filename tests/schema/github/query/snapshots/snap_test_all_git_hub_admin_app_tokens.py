# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[simple] 1'] = {
    'data': {
        'allGitHubAdminAppTokens': {
            'edges': [
                {
                    'node': {
                        'scope': 'read:org',
                        'tokenId': '1',
                        'tokenMasked': 'XXXXXXXXXXXXXXX'
                    }
                },
                {
                    'node': {
                        'scope': '',
                        'tokenId': '2',
                        'tokenMasked': 'XXXXXXXXXXXXXXX'
                    }
                },
                {
                    'node': {
                        'scope': '',
                        'tokenId': '3',
                        'tokenMasked': 'XXXXXXXXXXXXXXX'
                    }
                },
                {
                    'node': {
                        'scope': '',
                        'tokenId': '4',
                        'tokenMasked': 'XXXXXXXXXXXXXXX'
                    }
                }
            ],
            'totalCount': 4
        }
    }
}
