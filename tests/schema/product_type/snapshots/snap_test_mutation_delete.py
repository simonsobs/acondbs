# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_error[error-nonexistent] 1'] = {
    'data': {
        'deleteProductType': None
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
                'deleteProductType'
            ]
        }
    ]
}

snapshots['test_schema_error[error-nonexistent] 2'] = {
    'data': {
        'allProductTypes': {
            'edges': [
                {
                    'node': {
                        'name': 'map',
                        'typeId': '1'
                    }
                },
                {
                    'node': {
                        'name': 'beam',
                        'typeId': '2'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[error-unempty] 1'] = {
    'data': {
        'deleteProductType': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 3
                }
            ],
            'message': '''(sqlite3.IntegrityError) NOT NULL constraint failed: products.type_id
[SQL: UPDATE products SET type_id=? WHERE products.product_id = ?]
[parameters: ((None, 1), (None, 2), (None, 3))]
(Background on this error at: http://sqlalche.me/e/gkpj)''',
            'path': [
                'deleteProductType'
            ]
        }
    ]
}

snapshots['test_schema_error[error-unempty] 2'] = {
    'data': {
        'allProductTypes': {
            'edges': [
                {
                    'node': {
                        'name': 'map',
                        'typeId': '1'
                    }
                },
                {
                    'node': {
                        'name': 'beam',
                        'typeId': '2'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_success[delete] 1'] = {
    'data': {
        'deleteProductType': {
            'ok': True
        }
    }
}

snapshots['test_schema_success[delete] 2'] = {
    'data': {
        'allProductTypes': {
            'edges': [
                {
                    'node': {
                        'name': 'map',
                        'typeId': '1'
                    }
                }
            ]
        }
    }
}
