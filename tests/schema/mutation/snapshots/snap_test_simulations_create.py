# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_error[createSimulation-error-no-name] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 37,
                    'line': 3
                }
            ],
            'message': '''Argument "input" has invalid value {producedBy: "pwg-pmn"}.
In field "name": Expected "String!", found null.'''
        }
    ]
}

snapshots['test_schema_error[createSimulation-error-no-name] 2'] = {
    'data': {
        'allSimulations': {
            'edges': [
                {
                    'node': {
                        'productId': '1001'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_success[createSimulation-all-options] 1'] = {
    'data': {
        'createSimulation': {
            'simulation': {
                'name': 'simulation1'
            }
        }
    }
}

snapshots['test_schema_success[createSimulation-all-options] 2'] = {
    'data': {
        'simulation': {
            'contact': 'contact-person',
            'datePosted': '2020-05-04',
            'dateProduced': '2020-02-20',
            'dateUpdated': None,
            'name': 'simulation1',
            'note': '- Item 1',
            'paths': {
                'edges': [
                ]
            },
            'postedBy': 'poster',
            'producedBy': 'producer',
            'updatedBy': None
        }
    }
}

snapshots['test_schema_success[createSimulation-selective-options] 1'] = {
    'data': {
        'createSimulation': {
            'simulation': {
                'name': 'simulation1'
            }
        }
    }
}

snapshots['test_schema_success[createSimulation-selective-options] 2'] = {
    'data': {
        'simulation': {
            'contact': None,
            'datePosted': '2020-05-04',
            'dateProduced': None,
            'dateUpdated': None,
            'name': 'simulation1',
            'note': None,
            'paths': {
                'edges': [
                ]
            },
            'postedBy': None,
            'producedBy': 'pwg-pmn',
            'updatedBy': None
        }
    }
}
