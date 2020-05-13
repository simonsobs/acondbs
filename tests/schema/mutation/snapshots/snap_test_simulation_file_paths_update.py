# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_error[updateSimulationFilePath-immutableField] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 56,
                    'line': 3
                }
            ],
            'message': '''Argument "input" has invalid value {productId: 1002}.
In field "productId": Unknown field.'''
        }
    ]
}

snapshots['test_schema_error[updateSimulationFilePath-immutableField] 2'] = {
    'data': {
        'simulation': {
            'paths': {
                'edges': [
                    {
                        'node': {
                            'note': '',
                            'path': 'nersc:/go/to/my/simulations',
                            'product': {
                                'productId': '1001'
                            }
                        }
                    },
                    {
                        'node': {
                            'note': '',
                            'path': 'abcde:/path/to/the/simulations',
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

snapshots['test_schema_success[updateSimulationFilePath] 1'] = {
    'data': {
        'updateSimulationFilePath': {
            'simulationFilePath': {
                'path': 'nersc:/go/to/my/new_simulation_v2'
            }
        }
    }
}

snapshots['test_schema_success[updateSimulationFilePath] 2'] = {
    'data': {
        'simulation': {
            'datePosted': None,
            'name': 'xyz-s1234-20200101',
            'note': '''- note 1
- note 2''',
            'paths': {
                'edges': [
                    {
                        'node': {
                            'note': '- Note 1 updated',
                            'path': 'nersc:/go/to/my/new_simulation_v2',
                            'product': {
                                'productId': '1001'
                            }
                        }
                    },
                    {
                        'node': {
                            'note': '',
                            'path': 'abcde:/path/to/the/simulations',
                            'product': {
                                'productId': '1001'
                            }
                        }
                    }
                ]
            },
            'producedBy': 'abc-def'
        }
    }
}
