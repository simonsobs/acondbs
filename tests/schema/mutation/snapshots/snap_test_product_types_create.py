# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[createProduct] 1'] = {
    'data': {
        'createProductType': {
            'productType': {
                'name': 'compass'
            }
        }
    }
}

snapshots['test_schema_error[createProduct-error-already-exist] 1'] = {
    'data': {
        'createProductType': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': '''(sqlite3.IntegrityError) UNIQUE constraint failed: product_types.name
[SQL: INSERT INTO product_types (name, "order", indef_article, singular, plural, icon) VALUES (?, ?, ?, ?, ?, ?)]
[parameters: ('map', None, None, None, None, None)]
(Background on this error at: http://sqlalche.me/e/gkpj)''',
            'path': [
                'createProductType'
            ]
        }
    ]
}

snapshots['test_schema_error[createProduct-error-already-exist] 2'] = {
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
                        'name': 'simulation'
                    }
                },
                {
                    'node': {
                        'name': 'anchor'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_success[createProduct] 2'] = {
    'data': {
        'productType': {
            'icon': 'mdi-compass',
            'indefArticle': 'a',
            'name': 'compass',
            'plural': 'compasses',
            'products': {
                'edges': [
                ]
            },
            'singular': 'compass',
            'typeId': '5'
        }
    }
}
