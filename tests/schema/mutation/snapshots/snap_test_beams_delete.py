# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[deleteBeam] 1'] = {
    'data': {
        'deleteBeam': {
            'ok': True
        }
    }
}

snapshots['test_schema_success[deleteBeam] 2'] = {
    'data': {
        'allBeamFilePaths': {
            'edges': [
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
                }
            ]
        },
        'allBeams': {
            'edges': [
                {
                    'node': {
                        'name': '20180101',
                        'productId': '1010'
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

snapshots['test_schema_error[deleteBeam-error] 1'] = {
    'data': {
        'deleteBeam': None
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
                'deleteBeam'
            ]
        }
    ]
}

snapshots['test_schema_error[deleteBeam-error] 2'] = {
    'data': {
        'allBeamFilePaths': {
            'edges': [
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
                }
            ]
        },
        'allBeams': {
            'edges': [
                {
                    'node': {
                        'name': '20180101',
                        'productId': '1010'
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
