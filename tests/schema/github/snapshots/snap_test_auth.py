# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_auth 1'] = [
    (
        (
            'xyz',
            'https://github.com/login/oauth/access_token',
            'client_id_0123456789',
            'client_secret_abcdefghijklmnupqrstuvwxyz',
            'http://localhost:8080/signin'
        ),
        {
        }
    )
]

snapshots['test_auth 2'] = [
    (
        (
        ),
        {
            'admin_token': 'token123',
            'org_name': 'test_github_org_name',
            'user_token': 'user_token_xyz'
        }
    )
]
