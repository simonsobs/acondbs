# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[createBeamFilePath] 1'] = {
    'data': {
        'createBeamFilePath': {
            'beamFilePath': {
                'path': 'nersc:/go/to/my/new_beam_v1'
            }
        }
    }
}

snapshots['test_schema_success[createBeamFilePath] 2'] = {
    'data': {
        'beam': {
            'datePosted': '2018-01-01',
            'name': '20180101',
            'note': '- test entry',
            'paths': {
                'edges': [
                    {
                        'node': {
                            'note': '- Note 1',
                            'path': 'nersc:/go/to/my/new_beam_v1',
                            'product': {
                                'productId': '1010'
                            }
                        }
                    }
                ]
            },
            'producedBy': 'pwg-pmn'
        }
    }
}

snapshots['test_schema_error[createBeamFilePath-noSuchField] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 39,
                    'line': 3
                }
            ],
            'message': '''Argument "input" has invalid value {path: "nersc:/go/to/my/new_beam_v1", note: "- Note 1", productId: 1010, noSuchField: "xxx"}.
In field "noSuchField": Unknown field.'''
        }
    ]
}

snapshots['test_schema_error[createBeamFilePath-noSuchField] 2'] = {
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
