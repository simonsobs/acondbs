# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

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
                        'typeId': '1'
                    }
                },
                {
                    'node': {
                        'name': 'beam',
                        'typeId': '2'
                    }
                },
                {
                    'node': {
                        'name': 'simulation',
                        'typeId': '3'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[deleteProductType-error-nonexistent] 1'] = {
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

snapshots['test_schema_error[deleteProductType-error-nonexistent] 2'] = {
    'data': {
        'allProductTypes': {
            'edges': [
                {
                    'node': {
                        'name': 'map',
                        'typeId': '1'
                    }
                },
                {
                    'node': {
                        'name': 'beam',
                        'typeId': '2'
                    }
                },
                {
                    'node': {
                        'name': 'simulation',
                        'typeId': '3'
                    }
                },
                {
                    'node': {
                        'name': 'anchor',
                        'typeId': '4'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[deleteProductType-error-unempty] 1'] = {
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
            'message': 'Cannot delete the product type "map". Products of this type exist',
            'path': [
                'deleteProductType'
            ]
        }
    ]
}

snapshots['test_schema_error[deleteProductType-error-unempty] 2'] = {
    'data': {
        'allProductTypes': {
            'edges': [
                {
                    'node': {
                        'name': 'map',
                        'typeId': '1'
                    }
                },
                {
                    'node': {
                        'name': 'beam',
                        'typeId': '2'
                    }
                },
                {
                    'node': {
                        'name': 'simulation',
                        'typeId': '3'
                    }
                },
                {
                    'node': {
                        'name': 'anchor',
                        'typeId': '4'
                    }
                }
            ]
        }
    }
}
