# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[deleteSimulation] 1'] = {
    'data': {
        'deleteSimulation': {
            'ok': True
        }
    }
}

snapshots['test_schema_success[deleteSimulation] 2'] = {
    'data': {
        'allSimulationFilePaths': {
            'edges': [
            ]
        },
        'allSimulations': {
            'edges': [
            ]
        }
    }
}

snapshots['test_schema_error[deleteSimulation-error] 1'] = {
    'data': {
        'deleteSimulation': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 11,
                    'line': 3
                }
            ],
            'message': "Class 'builtins.NoneType' is not mapped",
            'path': [
                'deleteSimulation'
            ]
        }
    ]
}

snapshots['test_schema_error[deleteSimulation-error] 2'] = {
    'data': {
        'allSimulationFilePaths': {
            'edges': [
                {
                    'node': {
                        'path': 'nersc:/go/to/my/simulations',
                        'productId': 1001
                    }
                },
                {
                    'node': {
                        'path': 'abcde:/path/to/the/simulations',
                        'productId': 1001
                    }
                }
            ]
        },
        'allSimulations': {
            'edges': [
                {
                    'node': {
                        'name': 'xyz-s1234-20200101',
                        'productId': '1001'
                    }
                }
            ]
        }
    }
}
