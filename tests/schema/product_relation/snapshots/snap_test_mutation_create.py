# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[create] 1'] = {
    'data': {
        'createProductRelation': {
            'ok': True,
            'productRelation': {
                'other': {
                    'name': 'child1',
                    'productId': '2'
                },
                'relationId': '3',
                'reverse': {
                    'relationId': '4'
                },
                'self_': {
                    'name': 'parent1',
                    'productId': '1'
                },
                'type_': {
                    'name': 'child',
                    'typeId': '2'
                }
            }
        }
    }
}

snapshots['test_schema_success[create] 2'] = {
    'data': {
        'allProductRelations': {
            'edges': [
                {
                    'node': {
                        'other': {
                            'name': 'child12',
                            'productId': '4'
                        },
                        'relationId': '1',
                        'reverse': {
                            'relationId': '2'
                        },
                        'self_': {
                            'name': 'parent2',
                            'productId': '3'
                        },
                        'type_': {
                            'name': 'child',
                            'typeId': '2'
                        }
                    }
                },
                {
                    'node': {
                        'other': {
                            'name': 'parent2',
                            'productId': '3'
                        },
                        'relationId': '2',
                        'reverse': {
                            'relationId': '1'
                        },
                        'self_': {
                            'name': 'child12',
                            'productId': '4'
                        },
                        'type_': {
                            'name': 'parent',
                            'typeId': '1'
                        }
                    }
                },
                {
                    'node': {
                        'other': {
                            'name': 'child1',
                            'productId': '2'
                        },
                        'relationId': '3',
                        'reverse': {
                            'relationId': '4'
                        },
                        'self_': {
                            'name': 'parent1',
                            'productId': '1'
                        },
                        'type_': {
                            'name': 'child',
                            'typeId': '2'
                        }
                    }
                },
                {
                    'node': {
                        'other': {
                            'name': 'parent1',
                            'productId': '1'
                        },
                        'relationId': '4',
                        'reverse': {
                            'relationId': '3'
                        },
                        'self_': {
                            'name': 'child1',
                            'productId': '2'
                        },
                        'type_': {
                            'name': 'parent',
                            'typeId': '1'
                        }
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[error-type_id-nonexistent] 1'] = {
    'data': {
        'createProductRelation': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 3
                }
            ],
            'message': 'No row was found for one()',
            'path': [
                'createProductRelation'
            ]
        }
    ]
}

snapshots['test_schema_error[error-type_id-nonexistent] 2'] = {
    'data': {
        'allProductRelations': {
            'edges': [
                {
                    'node': {
                        'other': {
                            'name': 'child12',
                            'productId': '4'
                        },
                        'relationId': '1',
                        'reverse': {
                            'relationId': '2'
                        },
                        'self_': {
                            'name': 'parent2',
                            'productId': '3'
                        },
                        'type_': {
                            'name': 'child',
                            'typeId': '2'
                        }
                    }
                },
                {
                    'node': {
                        'other': {
                            'name': 'parent2',
                            'productId': '3'
                        },
                        'relationId': '2',
                        'reverse': {
                            'relationId': '1'
                        },
                        'self_': {
                            'name': 'child12',
                            'productId': '4'
                        },
                        'type_': {
                            'name': 'parent',
                            'typeId': '1'
                        }
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[error-self_product_id-nonexistent] 1'] = {
    'data': {
        'createProductRelation': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 3
                }
            ],
            'message': 'No row was found for one()',
            'path': [
                'createProductRelation'
            ]
        }
    ]
}

snapshots['test_schema_error[error-self_product_id-nonexistent] 2'] = {
    'data': {
        'allProductRelations': {
            'edges': [
                {
                    'node': {
                        'other': {
                            'name': 'child12',
                            'productId': '4'
                        },
                        'relationId': '1',
                        'reverse': {
                            'relationId': '2'
                        },
                        'self_': {
                            'name': 'parent2',
                            'productId': '3'
                        },
                        'type_': {
                            'name': 'child',
                            'typeId': '2'
                        }
                    }
                },
                {
                    'node': {
                        'other': {
                            'name': 'parent2',
                            'productId': '3'
                        },
                        'relationId': '2',
                        'reverse': {
                            'relationId': '1'
                        },
                        'self_': {
                            'name': 'child12',
                            'productId': '4'
                        },
                        'type_': {
                            'name': 'parent',
                            'typeId': '1'
                        }
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[error-otheer_product_id-nonexistent] 1'] = {
    'data': {
        'createProductRelation': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 3
                }
            ],
            'message': 'No row was found for one()',
            'path': [
                'createProductRelation'
            ]
        }
    ]
}

snapshots['test_schema_error[error-otheer_product_id-nonexistent] 2'] = {
    'data': {
        'allProductRelations': {
            'edges': [
                {
                    'node': {
                        'other': {
                            'name': 'child12',
                            'productId': '4'
                        },
                        'relationId': '1',
                        'reverse': {
                            'relationId': '2'
                        },
                        'self_': {
                            'name': 'parent2',
                            'productId': '3'
                        },
                        'type_': {
                            'name': 'child',
                            'typeId': '2'
                        }
                    }
                },
                {
                    'node': {
                        'other': {
                            'name': 'parent2',
                            'productId': '3'
                        },
                        'relationId': '2',
                        'reverse': {
                            'relationId': '1'
                        },
                        'self_': {
                            'name': 'child12',
                            'productId': '4'
                        },
                        'type_': {
                            'name': 'parent',
                            'typeId': '1'
                        }
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[error-duplicate] 1'] = {
    'data': {
        'createProductRelation': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 3
                }
            ],
            'message': '''(sqlite3.IntegrityError) UNIQUE constraint failed: product_relations.type_id, product_relations.self_product_id, product_relations.other_product_id
[SQL: INSERT INTO product_relations (type_id, self_product_id, other_product_id, reverse_relation_id) VALUES (?, ?, ?, ?)]
[parameters: (2, 3, 4, None)]
(Background on this error at: http://sqlalche.me/e/gkpj)''',
            'path': [
                'createProductRelation'
            ]
        }
    ]
}

snapshots['test_schema_error[error-duplicate] 2'] = {
    'data': {
        'allProductRelations': {
            'edges': [
                {
                    'node': {
                        'other': {
                            'name': 'child12',
                            'productId': '4'
                        },
                        'relationId': '1',
                        'reverse': {
                            'relationId': '2'
                        },
                        'self_': {
                            'name': 'parent2',
                            'productId': '3'
                        },
                        'type_': {
                            'name': 'child',
                            'typeId': '2'
                        }
                    }
                },
                {
                    'node': {
                        'other': {
                            'name': 'parent2',
                            'productId': '3'
                        },
                        'relationId': '2',
                        'reverse': {
                            'relationId': '1'
                        },
                        'self_': {
                            'name': 'child12',
                            'productId': '4'
                        },
                        'type_': {
                            'name': 'parent',
                            'typeId': '1'
                        }
                    }
                }
            ]
        }
    }
}
