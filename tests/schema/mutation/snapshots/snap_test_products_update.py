# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[updateProduct] 1'] = {
    'data': {
        'updateProduct': {
            'product': {
                'name': 'lat20190213',
                'productId': '1001'
            }
        }
    }
}

snapshots['test_schema_success[updateProduct] 2'] = {
    'data': {
        'product': {
            'contact': 'new-contact',
            'datePosted': '2019-02-13',
            'dateProduced': '2019-02-13',
            'dateUpdated': '2020-05-04',
            'name': 'lat20190213',
            'note': '- updated note 123',
            'paths': {
                'edges': [
                    {
                        'node': {
                            'path': 'nersc:/go/to/my/maps'
                        }
                    }
                ]
            },
            'postedBy': 'pwg-pmn',
            'producedBy': 'pwg-pmn',
            'updatedBy': 'updater'
        }
    }
}

snapshots['test_schema_error[updateProduct-error-immutable-fields] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 49,
                    'line': 3
                }
            ],
            'message': '''Argument "input" has invalid value {name: "new-name"}.
In field "name": Unknown field.'''
        }
    ]
}

snapshots['test_schema_error[updateProduct-error-immutable-fields] 2'] = {
    'data': {
        'product': {
            'contact': 'pwg-pmn',
            'datePosted': '2018-01-01',
            'dateProduced': '2018-01-01',
            'dateUpdated': None,
            'name': '20180101',
            'note': '- test entry',
            'paths': {
                'edges': [
                ]
            },
            'postedBy': 'pwg-pmn',
            'producedBy': 'pwg-pmn',
            'updatedBy': ''
        }
    }
}
