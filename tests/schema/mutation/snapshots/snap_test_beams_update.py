# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[updateBeam] 1'] = {
    'data': {
        'updateBeam': {
            'beam': {
                'name': '20180101',
                'productId': '1010'
            }
        }
    }
}

snapshots['test_schema_success[updateBeam] 2'] = {
    'data': {
        'beam': None
    }
}

snapshots['test_schema_error[updateBeam-error-immutable-fields] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 46,
                    'line': 3
                }
            ],
            'message': '''Argument "input" has invalid value {name: "new-name"}.
In field "name": Unknown field.'''
        }
    ]
}

snapshots['test_schema_error[updateBeam-error-immutable-fields] 2'] = {
    'data': {
        'beam': None
    }
}
