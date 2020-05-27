# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[deleteProduct] 1'] = {
    'data': {
        'deleteProduct': {
            'ok': True
        }
    }
}

snapshots['test_schema_success[deleteProduct] 2'] = {
    'data': {
        'allProductFilePaths': {
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
                },
                {
                    'node': {
                        'path': 'BEAM_DEPOT/Beams/20190304',
                        'productId': 1070
                    }
                },
                {
                    'node': {
                        'path': 'BEAM_DEPOT/Beams/20190607',
                        'productId': 1120
                    }
                },
                {
                    'node': {
                        'path': 'BEAM_DEPOT/Beams/20200123',
                        'productId': 1130
                    }
                },
                {
                    'node': {
                        'path': 'BEAM_DEPOT/Beams/20200207',
                        'productId': 1150
                    }
                },
                {
                    'node': {
                        'path': 'nersc:/go/to/my/simulations',
                        'productId': 1002
                    }
                },
                {
                    'node': {
                        'path': 'abcde:/path/to/the/simulations',
                        'productId': 1002
                    }
                }
            ]
        },
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'name': 'xyz-s1234-20200101',
                        'productId': '1002'
                    }
                },
                {
                    'node': {
                        'name': '20180101',
                        'productId': '1010'
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
                },
                {
                    'node': {
                        'name': '20190304',
                        'productId': '1070'
                    }
                },
                {
                    'node': {
                        'name': '20190607',
                        'productId': '1120'
                    }
                },
                {
                    'node': {
                        'name': '20200123',
                        'productId': '1130'
                    }
                },
                {
                    'node': {
                        'name': '20200207',
                        'productId': '1150'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[deleteProduct-error] 1'] = {
    'data': {
        'deleteProduct': None
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
                'deleteProduct'
            ]
        }
    ]
}

snapshots['test_schema_error[deleteProduct-error] 2'] = {
    'data': {
        'allProductFilePaths': {
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
                },
                {
                    'node': {
                        'path': 'BEAM_DEPOT/Beams/20190304',
                        'productId': 1070
                    }
                },
                {
                    'node': {
                        'path': 'BEAM_DEPOT/Beams/20190607',
                        'productId': 1120
                    }
                },
                {
                    'node': {
                        'path': 'BEAM_DEPOT/Beams/20200123',
                        'productId': 1130
                    }
                },
                {
                    'node': {
                        'path': 'BEAM_DEPOT/Beams/20200207',
                        'productId': 1150
                    }
                },
                {
                    'node': {
                        'path': 'nersc:/go/to/my/simulations',
                        'productId': 1002
                    }
                },
                {
                    'node': {
                        'path': 'abcde:/path/to/the/simulations',
                        'productId': 1002
                    }
                }
            ]
        },
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'name': 'lat20190213',
                        'productId': '1001'
                    }
                },
                {
                    'node': {
                        'name': 'xyz-s1234-20200101',
                        'productId': '1002'
                    }
                },
                {
                    'node': {
                        'name': '20180101',
                        'productId': '1010'
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
                },
                {
                    'node': {
                        'name': '20190304',
                        'productId': '1070'
                    }
                },
                {
                    'node': {
                        'name': '20190607',
                        'productId': '1120'
                    }
                },
                {
                    'node': {
                        'name': '20200123',
                        'productId': '1130'
                    }
                },
                {
                    'node': {
                        'name': '20200207',
                        'productId': '1150'
                    }
                }
            ]
        }
    }
}
