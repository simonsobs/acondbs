# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

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
                        'name': 'plaintiff',
                        'typeId': '3'
                    }
                },
                {
                    'node': {
                        'name': 'defendant',
                        'typeId': '4'
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
            'message': '''(sqlite3.IntegrityError) NOT NULL constraint failed: product_relations.type_id
[SQL: UPDATE product_relations SET type_id=? WHERE product_relations.relation_id = ?]
[parameters: ((None, 1), (None, 2), (None, 3), (None, 4), (None, 5), (None, 6))]
(Background on this error at: http://sqlalche.me/e/gkpj)''',
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
                        'name': 'plaintiff',
                        'typeId': '3'
                    }
                },
                {
                    'node': {
                        'name': 'defendant',
                        'typeId': '4'
                    }
                }
            ]
        }
    }
}
