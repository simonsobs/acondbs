# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_error[deleteProductType-error] 1'] = {
    'data': {
        'deleteProductType': None
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
                'deleteProductType'
            ]
        }
    ]
}

snapshots['test_schema_error[deleteProductType-error] 2'] = {
    'data': {
        'allProductTypes': {
            'edges': [
                {
                    'node': {
                        'name': 'map',
                        'productTypeId': '1'
                    }
                },
                {
                    'node': {
                        'name': 'beam',
                        'productTypeId': '2'
                    }
                },
                {
                    'node': {
                        'name': 'simulation',
                        'productTypeId': '3'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_success[deleteProductType] 1'] = {
    'data': {
        'deleteProductType': {
            'ok': True
        }
    }
}

snapshots['test_schema_success[deleteProductType] 2'] = {
    'data': {
        'allProductTypes': {
            'edges': [
                {
                    'node': {
                        'name': 'map',
                        'productTypeId': '1'
                    }
                },
                {
                    'node': {
                        'name': 'simulation',
                        'productTypeId': '3'
                    }
                }
            ]
        }
    }
}
