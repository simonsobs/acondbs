# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[create] 1'] = {
    'data': {
        'deleteProductRelation': {
            'ok': True
        }
    }
}

snapshots['test_schema_success[create] 2'] = {
    'data': {
        'allProductRelations': {
            'edges': [
            ]
        }
    }
}

snapshots['test_schema_error[error-nonexistent] 1'] = {
    'data': {
        'deleteProductRelation': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 3
                }
            ],
            'message': 'No row was found for one()',
            'path': [
                'deleteProductRelation'
            ]
        }
    ]
}

snapshots['test_schema_error[error-nonexistent] 2'] = {
    'data': {
        'allProductRelations': {
            'edges': [
                {
                    'node': {
                        'other': {
                            'name': 'child1',
                            'productId': '1'
                        },
                        'relationId': '1',
                        'reverse': {
                            'relationId': '2'
                        },
                        'self_': {
                            'name': 'parent1',
                            'productId': '2'
                        },
                        'type_': {
                            'name': 'child',
                            'typeId': '1'
                        }
                    }
                },
                {
                    'node': {
                        'other': {
                            'name': 'parent1',
                            'productId': '2'
                        },
                        'relationId': '2',
                        'reverse': {
                            'relationId': '1'
                        },
                        'self_': {
                            'name': 'child1',
                            'productId': '1'
                        },
                        'type_': {
                            'name': 'parent',
                            'typeId': '2'
                        }
                    }
                }
            ]
        }
    }
}
