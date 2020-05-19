# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[allProductRelationTypes] 1'] = {
    'data': {
        'allProductRelationTypes': {
            'edges': [
                {
                    'node': {
                        'name': 'parent',
                        'typeId': '1'
                    }
                },
                {
                    'node': {
                        'name': 'child',
                        'typeId': '2'
                    }
                },
                {
                    'node': {
                        'name': 'invigilator',
                        'typeId': '3'
                    }
                }
            ]
        }
    }
}

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
