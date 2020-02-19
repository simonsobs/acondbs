# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[createMap] 1'] = {
    'data': {
        'createMap': {
            'map': {
                'name': 'map1'
            }
        }
    }
}

snapshots['test_schema[createMap] 2'] = {
    'data': {
        'map': {
            'name': 'map1'
        }
    }
}

snapshots['test_schema[updateMap] 1'] = {
    'data': {
        'updateMap': {
            'map': {
                'mapId': '1001',
                'name': 'new-name'
            }
        }
    }
}

snapshots['test_schema[updateMap] 2'] = {
    'data': {
        'map': {
            'mapId': '1001',
            'name': 'new-name'
        }
    }
}
