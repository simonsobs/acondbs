# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_error[error-already-exist] 1'] = {
    'data': {
        'createProductType': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 3
                }
            ],
            'message': '''(sqlite3.IntegrityError) UNIQUE constraint failed: product_types.name
[SQL: INSERT INTO product_types (name, "order", indef_article, singular, plural, icon) VALUES (?, ?, ?, ?, ?, ?)]
[parameters: ('map', 5, 'a', 'map', 'maps', 'mdi-map')]
(Background on this error at: http://sqlalche.me/e/gkpj)''',
            'path': [
                'createProductType'
            ]
        }
    ]
}

snapshots['test_schema_error[error-already-exist] 2'] = {
    'data': {
        'allProductTypes': {
            'edges': [
                {
                    'node': {
                        'name': 'map'
                    }
                },
                {
                    'node': {
                        'name': 'beam'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_success[create] 1'] = {
    'data': {
        'createProductType': {
            'ok': True,
            'productType': {
                'icon': 'mdi-compass',
                'indefArticle': 'a',
                'name': 'compass',
                'order': 5,
                'plural': 'compasses',
                'products': {
                    'edges': [
                    ]
                },
                'singular': 'compass',
                'typeId': '3'
            }
        }
    }
}

snapshots['test_schema_success[create] 2'] = {
    'data': {
        'allProductTypes': {
            'edges': [
                {
                    'node': {
                        'name': 'map'
                    }
                },
                {
                    'node': {
                        'name': 'beam'
                    }
                },
                {
                    'node': {
                        'name': 'compass'
                    }
                }
            ]
        }
    }
}
