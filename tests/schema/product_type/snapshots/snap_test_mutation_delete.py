# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

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
                },
                {
                    'node': {
                        'name': 'beam',
                        'typeId': '2'
                    }
                },
                {
                    'node': {
                        'name': 'simulation',
                        'typeId': '3'
                    }
                }
            ]
        }
    }
}

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
            'message': "Class 'builtins.NoneType' is not mapped",
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
                },
                {
                    'node': {
                        'name': 'simulation',
                        'typeId': '3'
                    }
                },
                {
                    'node': {
                        'name': 'anchor',
                        'typeId': '4'
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
[parameters: ((None, 1001), (None, 1012), (None, 1013))]
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
                },
                {
                    'node': {
                        'name': 'simulation',
                        'typeId': '3'
                    }
                },
                {
                    'node': {
                        'name': 'anchor',
                        'typeId': '4'
                    }
                }
            ]
        }
    }
}
