# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[delete] 1'] = {
    'data': {
        'deleteProductRelationType': {
            'ok': True
        }
    }
}

snapshots['test_schema_success[delete] 2'] = {
    'data': {
        'allProductRelationTypes': {
            'edges': [
                {
                    'node': {
                        'indefArticle': 'a',
                        'name': 'parent',
                        'plural': 'parents',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': 'lat20200120',
                                            'productId': '1012'
                                        },
                                        'self_': {
                                            'name': '20200123',
                                            'productId': '1130'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': 'lat20200201',
                                            'productId': '1013'
                                        },
                                        'self_': {
                                            'name': '20200207',
                                            'productId': '1150'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200123',
                                            'productId': '1130'
                                        },
                                        'self_': {
                                            'name': '20200207',
                                            'productId': '1150'
                                        }
                                    }
                                }
                            ]
                        },
                        'reverse': {
                            'name': 'child',
                            'typeId': '2'
                        },
                        'singular': 'parent',
                        'typeId': '1'
                    }
                },
                {
                    'node': {
                        'indefArticle': 'a',
                        'name': 'child',
                        'plural': 'children',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200123',
                                            'productId': '1130'
                                        },
                                        'self_': {
                                            'name': 'lat20200120',
                                            'productId': '1012'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200207',
                                            'productId': '1150'
                                        },
                                        'self_': {
                                            'name': 'lat20200201',
                                            'productId': '1013'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200207',
                                            'productId': '1150'
                                        },
                                        'self_': {
                                            'name': '20200123',
                                            'productId': '1130'
                                        }
                                    }
                                }
                            ]
                        },
                        'reverse': {
                            'name': 'parent',
                            'typeId': '1'
                        },
                        'singular': 'child',
                        'typeId': '2'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[error-nonexistent] 1'] = {
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

snapshots['test_schema_error[error-nonexistent] 2'] = {
    'data': {
        'allProductRelationTypes': {
            'edges': [
                {
                    'node': {
                        'indefArticle': 'a',
                        'name': 'parent',
                        'plural': 'parents',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': 'lat20200120',
                                            'productId': '1012'
                                        },
                                        'self_': {
                                            'name': '20200123',
                                            'productId': '1130'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': 'lat20200201',
                                            'productId': '1013'
                                        },
                                        'self_': {
                                            'name': '20200207',
                                            'productId': '1150'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200123',
                                            'productId': '1130'
                                        },
                                        'self_': {
                                            'name': '20200207',
                                            'productId': '1150'
                                        }
                                    }
                                }
                            ]
                        },
                        'reverse': {
                            'name': 'child',
                            'typeId': '2'
                        },
                        'singular': 'parent',
                        'typeId': '1'
                    }
                },
                {
                    'node': {
                        'indefArticle': 'a',
                        'name': 'child',
                        'plural': 'children',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200123',
                                            'productId': '1130'
                                        },
                                        'self_': {
                                            'name': 'lat20200120',
                                            'productId': '1012'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200207',
                                            'productId': '1150'
                                        },
                                        'self_': {
                                            'name': 'lat20200201',
                                            'productId': '1013'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200207',
                                            'productId': '1150'
                                        },
                                        'self_': {
                                            'name': '20200123',
                                            'productId': '1130'
                                        }
                                    }
                                }
                            ]
                        },
                        'reverse': {
                            'name': 'parent',
                            'typeId': '1'
                        },
                        'singular': 'child',
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
                        'reverse': {
                            'name': 'defendant',
                            'typeId': '4'
                        },
                        'singular': 'plaintiff',
                        'typeId': '3'
                    }
                },
                {
                    'node': {
                        'indefArticle': 'a',
                        'name': 'defendant',
                        'plural': 'defendants',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'reverse': {
                            'name': 'plaintiff',
                            'typeId': '3'
                        },
                        'singular': 'defendant',
                        'typeId': '4'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[error-unempty] 1'] = {
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

snapshots['test_schema_error[error-unempty] 2'] = {
    'data': {
        'allProductRelationTypes': {
            'edges': [
                {
                    'node': {
                        'indefArticle': 'a',
                        'name': 'parent',
                        'plural': 'parents',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': 'lat20200120',
                                            'productId': '1012'
                                        },
                                        'self_': {
                                            'name': '20200123',
                                            'productId': '1130'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': 'lat20200201',
                                            'productId': '1013'
                                        },
                                        'self_': {
                                            'name': '20200207',
                                            'productId': '1150'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200123',
                                            'productId': '1130'
                                        },
                                        'self_': {
                                            'name': '20200207',
                                            'productId': '1150'
                                        }
                                    }
                                }
                            ]
                        },
                        'reverse': {
                            'name': 'child',
                            'typeId': '2'
                        },
                        'singular': 'parent',
                        'typeId': '1'
                    }
                },
                {
                    'node': {
                        'indefArticle': 'a',
                        'name': 'child',
                        'plural': 'children',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200123',
                                            'productId': '1130'
                                        },
                                        'self_': {
                                            'name': 'lat20200120',
                                            'productId': '1012'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200207',
                                            'productId': '1150'
                                        },
                                        'self_': {
                                            'name': 'lat20200201',
                                            'productId': '1013'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200207',
                                            'productId': '1150'
                                        },
                                        'self_': {
                                            'name': '20200123',
                                            'productId': '1130'
                                        }
                                    }
                                }
                            ]
                        },
                        'reverse': {
                            'name': 'parent',
                            'typeId': '1'
                        },
                        'singular': 'child',
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
                        'reverse': {
                            'name': 'defendant',
                            'typeId': '4'
                        },
                        'singular': 'plaintiff',
                        'typeId': '3'
                    }
                },
                {
                    'node': {
                        'indefArticle': 'a',
                        'name': 'defendant',
                        'plural': 'defendants',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'reverse': {
                            'name': 'plaintiff',
                            'typeId': '3'
                        },
                        'singular': 'defendant',
                        'typeId': '4'
                    }
                }
            ]
        }
    }
}
