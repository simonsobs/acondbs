# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[type_id] 1'] = {
    'data': {
        'productRelation': {
            'other': {
                'name': 'lat20200120',
                'productId': '1012'
            },
            'relationId': '1',
            'reverse': {
                'relationId': '2'
            },
            'self_': {
                'name': '20200123',
                'productId': '1130'
            },
            'type_': {
                'name': 'parent',
                'typeId': '1'
            }
        }
    }
}

snapshots['test_schema[type_id-nonexistent] 1'] = {
    'data': {
        'productRelation': None
    }
}
