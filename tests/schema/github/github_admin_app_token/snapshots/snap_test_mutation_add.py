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

snapshots['test_schema_error[add] 2'] = [
    (
        (
            'https://github.com/login/oauth/access_token'
        ,),
        {
            'headers': {
                'Accept': 'application/vnd.github.v3+json, application/json'
            },
            'json': {
                'client_id': 'client_id_admin_0123',
                'client_secret': 'client_secret_admin_abcdefghijklmnupqrst',
                'code': 'code_01234',
                'grant_type': 'authorization_code',
                'redirect_uri': 'http://localhost:8080/admin/signin'
            }
        }
    )
]

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

snapshots['test_schema_success[add] 3'] = [
    (
        (
            'https://github.com/login/oauth/access_token'
        ,),
        {
            'headers': {
                'Accept': 'application/vnd.github.v3+json, application/json'
            },
            'json': {
                'client_id': 'client_id_admin_0123',
                'client_secret': 'client_secret_admin_abcdefghijklmnupqrst',
                'code': 'code_01234',
                'grant_type': 'authorization_code',
                'redirect_uri': 'http://localhost:8080/admin/signin'
            }
        }
    )
]