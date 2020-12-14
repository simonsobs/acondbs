# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_store_admin_app_token 1'] = [
    (
        (
            'xyz',
            'https://github.com/login/oauth/access_token',
            'client_id_admin_0123',
            'client_secret_admin_abcdefghijklmnupqrst',
            'http://localhost:8080/admin/signin'
        ),
        {
        }
    )
]

snapshots['test_store_admin_app_token_update 1'] = [
    (
        (
            'xyz',
            'https://github.com/login/oauth/access_token',
            'client_id_admin_0123',
            'client_secret_admin_abcdefghijklmnupqrst',
            'http://localhost:8080/admin/signin'
        ),
        {
        }
    )
]
