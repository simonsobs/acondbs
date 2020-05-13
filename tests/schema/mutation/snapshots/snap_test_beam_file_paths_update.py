# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_error[updateBeamFilePath-immutableField] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 50,
                    'line': 3
                }
            ],
            'message': '''Argument "input" has invalid value {productId: 1012}.
In field "productId": Unknown field.'''
        }
    ]
}

snapshots['test_schema_error[updateBeamFilePath-immutableField] 2'] = {
    'data': {
        'beam': None
    }
}

snapshots['test_schema_success[updateBeamFilePath] 1'] = {
    'data': {
        'updateBeamFilePath': {
            'beamFilePath': {
                'path': 'nersc:/go/to/my/new_beam_v2'
            }
        }
    }
}

snapshots['test_schema_success[updateBeamFilePath] 2'] = {
    'data': {
        'beam': None
    }
}
