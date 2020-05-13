# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

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
        'allBeams': {
            'edges': [
                {
                    'node': {
                        'productId': '1010'
                    }
                },
                {
                    'node': {
                        'productId': '1070'
                    }
                },
                {
                    'node': {
                        'productId': '1120'
                    }
                },
                {
                    'node': {
                        'productId': '1130'
                    }
                },
                {
                    'node': {
                        'productId': '1150'
                    }
                }
            ]
        }
    }
}

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
                ]
            },
            'postedBy': 'poster',
            'producedBy': 'producer',
            'updatedBy': None
        }
    }
}
