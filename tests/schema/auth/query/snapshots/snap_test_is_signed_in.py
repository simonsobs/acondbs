# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_scratch[dojocat] 1'] = {
    'data': {
        'isSignedIn': True
    }
}

snapshots['test_scratch[no-token] 1'] = {
    'data': {
        'isSignedIn': False
    }
}

snapshots['test_scratch[octocat] 1'] = {
    'data': {
        'isSignedIn': True
    }
}

snapshots['test_scratch[wrong-token] 1'] = {
    'data': {
        'isSignedIn': False
    }
}
