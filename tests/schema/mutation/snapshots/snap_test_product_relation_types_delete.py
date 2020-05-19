# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_error[deleteProductRelationType-error-nonexistent] 1'] = {
    'data': {
        'deleteProductRelationType': None
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
                'deleteProductRelationType'
            ]
        }
    ]
}

snapshots['test_schema_error[deleteProductRelationType-error-nonexistent] 2'] = {
    'data': {
        'allProductRelationTypes': {
            'edges': [
                {
                    'node': {
                        'name': 'parent',
                        'typeId': '1'
                    }
                },
                {
                    'node': {
                        'name': 'child',
                        'typeId': '2'
                    }
                },
                {
                    'node': {
                        'name': 'invigilator',
                        'typeId': '3'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[deleteProductRelationType-error-unempty] 1'] = {
    'data': {
        'deleteProductRelationType': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 11,
                    'line': 3
                }
            ],
            'message': 'Cannot delete the product relation type "parent". Products with this relation type exist',
            'path': [
                'deleteProductRelationType'
            ]
        }
    ]
}

snapshots['test_schema_error[deleteProductRelationType-error-unempty] 2'] = {
    'data': {
        'allProductRelationTypes': {
            'edges': [
                {
                    'node': {
                        'name': 'parent',
                        'typeId': '1'
                    }
                },
                {
                    'node': {
                        'name': 'child',
                        'typeId': '2'
                    }
                },
                {
                    'node': {
                        'name': 'invigilator',
                        'typeId': '3'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_success[deleteProductRelationType] 1'] = {
    'data': {
        'deleteProductRelationType': {
            'ok': True
        }
    }
}

snapshots['test_schema_success[deleteProductRelationType] 2'] = {
    'data': {
        'allProductRelationTypes': {
            'edges': [
                {
                    'node': {
                        'name': 'parent',
                        'typeId': '1'
                    }
                },
                {
                    'node': {
                        'name': 'child',
                        'typeId': '2'
                    }
                }
            ]
        }
    }
}
