# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[updateMap] 1'] = {
    'data': {
        'updateMap': {
            'map': {
                'name': 'lat20190213',
                'productId': '1001'
            }
        }
    }
}

snapshots['test_schema_error[updateMap-error-immutable-fields] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 45,
                    'line': 3
                }
            ],
            'message': '''Argument "input" has invalid value {name: "new-name"}.
In field "name": Unknown field.'''
        }
    ]
}

snapshots['test_schema_success[updateMap] 2'] = {
    'data': {
        'map': None
    }
}

snapshots['test_schema_error[updateMap-error-immutable-fields] 2'] = {
    'data': {
        'map': {
            'beams': {
                'edges': [
                ]
            },
            'contact': 'pwg-pmn',
            'datePosted': '2019-02-13',
            'dateProduced': '2019-02-13',
            'dateUpdated': '2019-02-13',
            'name': 'lat20190213',
            'note': '''- This is a dummy test with a lat map
- This should not depend on any beam''',
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
            'updatedBy': 'pwg-pmn'
        }
    }
}
