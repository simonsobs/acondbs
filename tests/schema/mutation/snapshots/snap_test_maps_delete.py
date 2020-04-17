# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[deleteMap] 1'] = {
    'data': {
        'deleteMap': {
            'ok': True
        }
    }
}

snapshots['test_schema[deleteMap] 2'] = {
    'data': {
        'map': None
    }
}
