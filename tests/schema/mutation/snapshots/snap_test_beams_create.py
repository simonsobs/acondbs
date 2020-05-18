# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[createBeam-all-options] 1'] = {
    'data': {
        'createBeam': {
            'beam': {
                'name': 'beam1'
            }
        }
    }
}

snapshots['test_schema_success[createBeam-all-options] 2'] = {
    'data': {
        'beam': {
            'contact': 'contact-person',
            'datePosted': '2020-05-04',
            'dateProduced': '2020-02-20',
            'dateUpdated': None,
            'name': 'beam1',
            'note': '- Item 1',
            'paths': {
                'edges': [
                    {
                        'node': {
                            'path': '/path/to/new/product1'
                        }
                    },
                    {
                        'node': {
                            'path': '/another/location/of/product1'
                        }
                    }
                ]
            },
            'postedBy': 'poster',
            'producedBy': 'producer',
            'updatedBy': None
        }
    }
}

snapshots['test_schema_error[createBeam-error-no-name] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 31,
                    'line': 3
                }
            ],
            'message': '''Argument "input" has invalid value {producedBy: "pwg-pmn"}.
In field "name": Expected "String!", found null.'''
        }
    ]
}

snapshots['test_schema_error[createBeam-error-no-name] 2'] = {
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
