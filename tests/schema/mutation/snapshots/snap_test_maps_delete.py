# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[deleteMap] 1'] = {
    'data': {
        'deleteMap': {
            'ok': True
        }
    }
}

snapshots['test_schema_success[deleteMap] 2'] = {
    'data': {
        'allMapFilePaths': {
            'edges': [
                {
                    'node': {
                        'path': 'nersc:/go/to/my/maps_v2',
                        'productId': 1012
                    }
                },
                {
                    'node': {
                        'path': 'abcde:/path/to/the/maps_v2',
                        'productId': 1012
                    }
                },
                {
                    'node': {
                        'path': 'nersc:/go/to/my/maps_v3',
                        'productId': 1013
                    }
                }
            ]
        },
        'allMaps': {
            'edges': [
                {
                    'node': {
                        'name': 'lat20200120',
                        'productId': '1012'
                    }
                },
                {
                    'node': {
                        'name': 'lat20200201',
                        'productId': '1013'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[deleteMap-error] 1'] = {
    'data': {
        'deleteMap': None
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
                'deleteMap'
            ]
        }
    ]
}

snapshots['test_schema_error[deleteMap-error] 2'] = {
    'data': {
        'allMapFilePaths': {
            'edges': [
                {
                    'node': {
                        'path': 'nersc:/go/to/my/maps',
                        'productId': 1001
                    }
                },
                {
                    'node': {
                        'path': 'nersc:/go/to/my/maps_v2',
                        'productId': 1012
                    }
                },
                {
                    'node': {
                        'path': 'abcde:/path/to/the/maps_v2',
                        'productId': 1012
                    }
                },
                {
                    'node': {
                        'path': 'nersc:/go/to/my/maps_v3',
                        'productId': 1013
                    }
                }
            ]
        },
        'allMaps': {
            'edges': [
                {
                    'node': {
                        'name': 'lat20190213',
                        'productId': '1001'
                    }
                },
                {
                    'node': {
                        'name': 'lat20200120',
                        'productId': '1012'
                    }
                },
                {
                    'node': {
                        'name': 'lat20200201',
                        'productId': '1013'
                    }
                }
            ]
        }
    }
}
