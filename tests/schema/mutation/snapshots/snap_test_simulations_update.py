# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[updateSimulation] 1'] = {
    'data': {
        'updateSimulation': {
            'simulation': {
                'name': 'xyz-s1234-20200101',
                'productId': '1001'
            }
        }
    }
}

snapshots['test_schema_success[updateSimulation] 2'] = {
    'data': {
        'simulation': {
            'contact': 'new-contact',
            'datePosted': '2019-03-15',
            'dateProduced': '2019-03-15',
            'dateUpdated': '2020-05-04',
            'name': 'xyz-s1234-20200101',
            'note': '- updated note 123',
            'paths': {
                'edges': [
                    {
                        'node': {
                            'path': 'nersc:/go/to/my/simulations'
                        }
                    },
                    {
                        'node': {
                            'path': 'abcde:/path/to/the/simulations'
                        }
                    }
                ]
            },
            'postedBy': 'abc-def',
            'producedBy': 'abc-def',
            'updatedBy': 'updater'
        }
    }
}

snapshots['test_schema_error[updateSimulation-error-immutable-fields] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 52,
                    'line': 3
                }
            ],
            'message': '''Argument "input" has invalid value {name: "new-name"}.
In field "name": Unknown field.'''
        }
    ]
}

snapshots['test_schema_error[updateSimulation-error-immutable-fields] 2'] = {
    'data': {
        'simulation': None
    }
}
