# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[create] 1'] = {
    'data': {
        'createProductRelationType': {
            'productRelationType': {
                'name': 'plaintiff'
            }
        }
    }
}

snapshots['test_schema_success[create] 2'] = {
    'data': {
        'allProductRelationTypes': {
            'edges': [
                {
                    'node': {
                        'indefArticle': None,
                        'name': 'parent',
                        'plural': None,
                        'relations': {
                            'edges': [
                            ]
                        },
                        'reverse': {
                            'name': 'child',
                            'typeId': '2'
                        },
                        'singular': None,
                        'typeId': '1'
                    }
                },
                {
                    'node': {
                        'indefArticle': None,
                        'name': 'child',
                        'plural': None,
                        'relations': {
                            'edges': [
                            ]
                        },
                        'reverse': None,
                        'singular': None,
                        'typeId': '2'
                    }
                },
                {
                    'node': {
                        'indefArticle': 'a',
                        'name': 'plaintiff',
                        'plural': 'plaintiffs',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'reverse': None,
                        'singular': 'plaintiff',
                        'typeId': '3'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[error-already-exist] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 18,
                    'line': 5
                }
            ],
            'message': 'Cannot query field "productType" on type "CreateProductRelationType". Did you mean "productRelationType"?'
        }
    ]
}

snapshots['test_schema_error[error-already-exist] 2'] = {
    'data': {
        'allProductRelationTypes': {
            'edges': [
                {
                    'node': {
                        'indefArticle': None,
                        'name': 'parent',
                        'plural': None,
                        'relations': {
                            'edges': [
                            ]
                        },
                        'reverse': {
                            'name': 'child',
                            'typeId': '2'
                        },
                        'singular': None,
                        'typeId': '1'
                    }
                },
                {
                    'node': {
                        'indefArticle': None,
                        'name': 'child',
                        'plural': None,
                        'relations': {
                            'edges': [
                            ]
                        },
                        'reverse': None,
                        'singular': None,
                        'typeId': '2'
                    }
                }
            ]
        }
    }
}
