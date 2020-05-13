# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[deleteMapFilePath] 1'] = {
    'data': {
        'deleteMapFilePath': {
            'ok': True
        }
    }
}

snapshots['test_schema_success[deleteMapFilePath] 2'] = {
    'data': {
        'map': {
            'beams': {
                'edges': [
                ]
            },
            'datePosted': '2019-02-13',
            'name': 'lat20190213',
            'note': '''- This is a dummy test with a lat map
- This should not depend on any beam''',
            'paths': {
                'edges': [
                ]
            },
            'producedBy': 'pwg-pmn'
        }
    }
}

snapshots['test_schema_error[deleteMapFilePath-error] 1'] = {
    'data': {
        'deleteMapFilePath': None
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
                'deleteMapFilePath'
            ]
        }
    ]
}

snapshots['test_schema_error[deleteMapFilePath-error] 2'] = {
    'data': {
        'allMapFilePaths': {
            'edges': [
                {
                    'node': {
                        'productId': 1001
                    }
                },
                {
                    'node': {
                        'productId': 1012
                    }
                },
                {
                    'node': {
                        'productId': 1012
                    }
                },
                {
                    'node': {
                        'productId': 1013
                    }
                }
            ]
        }
    }
}
