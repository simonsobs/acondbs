# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[updateProductFilePath] 1'] = {
    'data': {
        'updateProductFilePath': {
            'productFilePath': {
                'path': 'nersc:/go/to/my/new_product_v2'
            }
        }
    }
}

snapshots['test_schema_success[updateProductFilePath] 2'] = {
    'data': {
        'product': {
            'datePosted': '2019-02-13',
            'name': 'lat20190213',
            'note': '''- This is a dummy test with a lat map
- This should not depend on any beam''',
            'paths': {
                'edges': [
                    {
                        'node': {
                            'note': '- Note 1 updated',
                            'path': 'nersc:/go/to/my/new_product_v2',
                            'product': {
                                'productId': '1001'
                            }
                        }
                    }
                ]
            },
            'producedBy': 'pwg-pmn'
        }
    }
}

snapshots['test_schema_error[updateProductFilePath-immutableField] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 61,
                    'line': 3
                }
            ],
            'message': '''Argument "input" has invalid value {productId: 1012}.
In field "productId": Unknown field.'''
        }
    ]
}

snapshots['test_schema_error[updateProductFilePath-immutableField] 2'] = {
    'data': {
        'product': {
            'paths': {
                'edges': [
                    {
                        'node': {
                            'note': '',
                            'path': 'nersc:/go/to/my/maps',
                            'product': {
                                'productId': '1001'
                            }
                        }
                    }
                ]
            }
        }
    }
}
