# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_error[deleteSimulationFilePath-error] 1'] = {
    'data': {
        'deleteSimulationFilePath': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': "Class 'builtins.NoneType' is not mapped",
            'path': [
                'deleteSimulationFilePath'
            ]
        }
    ]
}

snapshots['test_schema_error[deleteSimulationFilePath-error] 2'] = {
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

snapshots['test_schema_success[deleteSimulationFilePath] 1'] = {
    'data': {
        'deleteSimulationFilePath': {
            'ok': True
        }
    }
}

snapshots['test_schema_success[deleteSimulationFilePath] 2'] = {
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
