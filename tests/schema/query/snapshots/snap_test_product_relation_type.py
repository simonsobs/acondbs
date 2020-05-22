# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[productRelationType-by-TypeId-one)] 1'] = {
    'data': {
        'productRelationType': {
            'name': 'parent',
            'typeId': '1'
        }
    }
}

snapshots['test_schema[productRelationType-by-name-parent)] 1'] = {
    'data': {
        'productRelationType': {
            'name': 'parent',
            'typeId': '1'
        }
    }
}

snapshots['test_schema[productRelationType-by-id-and-name-parent)] 1'] = {
    'data': {
        'productRelationType': {
            'name': 'parent',
            'typeId': '1'
        }
    }
}

snapshots['test_schema[productRelationType-by-id-and-name-nonexistent)] 1'] = {
    'data': {
        'productRelationType': None
    }
}
