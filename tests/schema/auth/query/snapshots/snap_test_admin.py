# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_success[dojocat] 1'] = {
    'data': {
        'isAdmin': False
    }
}

snapshots['test_success[no-token] 1'] = {
    'data': {
        'isAdmin': False
    }
}

snapshots['test_success[octocat] 1'] = {
    'data': {
        'isAdmin': True
    }
}

snapshots['test_success[wrong-token] 1'] = {
    'data': {
        'isAdmin': False
    }
}
