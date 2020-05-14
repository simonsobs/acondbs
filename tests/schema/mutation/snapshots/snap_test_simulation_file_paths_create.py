# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_error[createSimulationFilePath-noSuchField] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 45,
                    'line': 3
                }
            ],
            'message': '''Argument "input" has invalid value {path: "nersc:/go/to/my/new_simulation_v1", note: "- Note 1", productId: 1001, noSuchField: "xxx"}.
In field "noSuchField": Unknown field.'''
        }
    ]
}

snapshots['test_schema_error[createSimulationFilePath-noSuchField] 2'] = {
    'data': {
        'allSimulationFilePaths': {
            'edges': [
                {
                    'node': {
                        'productId': 1001
                    }
                },
                {
                    'node': {
                        'productId': 1001
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_success[createSimulationFilePath] 1'] = {
    'data': {
        'createSimulationFilePath': {
            'simulationFilePath': {
                'path': 'nersc:/go/to/my/new_simulation_v1'
            }
        }
    }
}

snapshots['test_schema_success[createSimulationFilePath] 2'] = {
    'data': {
        'simulation': {
            'datePosted': '2019-03-15',
            'name': 'xyz-s1234-20200101',
            'note': '''- note 1
- note 2''',
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
                    },
                    {
                        'node': {
                            'note': '- Note 1',
                            'path': 'nersc:/go/to/my/new_simulation_v1',
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
