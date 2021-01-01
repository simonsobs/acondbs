# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_auth 1'] = [
    (
        (
        ),
        {
            'admin_token': 'token1',
            'org_name': 'test_github_org_name',
            'user_token': 'jpdq74xt'
        }
    )
]
