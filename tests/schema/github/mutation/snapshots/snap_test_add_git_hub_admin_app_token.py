# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_error[add] 1'] = {
    'data': {
        'allGitHubTokens': {
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
                'client_id': 'client_id_0123456789',
                'client_secret': 'client_secret_abcdefghijklmnupqrstuvwxyz',
                'code': 'code_01234',
                'grant_type': 'authorization_code',
                'redirect_uri': 'http://localhost:8080/signin'
            }
        }
    )
]

snapshots['test_schema_success[existing-user] 1'] = {
    'data': {
        'addGitHubAdminAppToken': {
            'ok': True
        }
    }
}

snapshots['test_schema_success[existing-user] 2'] = {
    'data': {
        'allGitHubTokens': {
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
                },
                {
                    'node': {
                        'scope': None,
                        'tokenId': '5',
                        'tokenMasked': 'XXXXXXXXXXXXXXX'
                    }
                }
            ],
            'totalCount': 5
        }
    }
}

snapshots['test_schema_success[existing-user] 3'] = [
    (
        (
            'https://github.com/login/oauth/access_token'
        ,),
        {
            'headers': {
                'Accept': 'application/vnd.github.v3+json, application/json'
            },
            'json': {
                'client_id': 'client_id_0123456789',
                'client_secret': 'client_secret_abcdefghijklmnupqrstuvwxyz',
                'code': 'code_01234',
                'grant_type': 'authorization_code',
                'redirect_uri': 'http://localhost:8080/signin'
            }
        }
    )
]

snapshots['test_schema_success[new-user] 1'] = {
    'data': {
        'addGitHubAdminAppToken': {
            'ok': True
        }
    }
}

snapshots['test_schema_success[new-user] 2'] = {
    'data': {
        'allGitHubTokens': {
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
                },
                {
                    'node': {
                        'scope': None,
                        'tokenId': '5',
                        'tokenMasked': 'XXXXXXXXXXXXXXX'
                    }
                }
            ],
            'totalCount': 5
        }
    }
}

snapshots['test_schema_success[new-user] 3'] = [
    (
        (
            'https://github.com/login/oauth/access_token'
        ,),
        {
            'headers': {
                'Accept': 'application/vnd.github.v3+json, application/json'
            },
            'json': {
                'client_id': 'client_id_0123456789',
                'client_secret': 'client_secret_abcdefghijklmnupqrstuvwxyz',
                'code': 'code_01234',
                'grant_type': 'authorization_code',
                'redirect_uri': 'http://localhost:8080/signin'
            }
        }
    )
]
