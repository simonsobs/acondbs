# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_error[deleteBeamFilePath-error] 1'] = {
    'data': {
        'deleteBeamFilePath': None
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
                'deleteBeamFilePath'
            ]
        }
    ]
}

snapshots['test_schema_error[deleteBeamFilePath-error] 2'] = {
    'data': {
        'allBeamFilePaths': {
            'edges': [
                {
                    'node': {
                        'productId': 1070
                    }
                },
                {
                    'node': {
                        'productId': 1120
                    }
                },
                {
                    'node': {
                        'productId': 1130
                    }
                },
                {
                    'node': {
                        'productId': 1150
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_success[deleteBeamFilePath] 1'] = {
    'data': {
        'deleteBeamFilePath': {
            'ok': True
        }
    }
}

snapshots['test_schema_success[deleteBeamFilePath] 2'] = {
    'data': {
        'beam': None
    }
}
