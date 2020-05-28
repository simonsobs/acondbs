# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[reverse] 1'] = {
    'data': {
        'createProductRelationTypes': {
            'ok': True,
            'productRelationType': {
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
        }
    }
}

snapshots['test_schema_success[reverse] 2'] = {
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
                        'reverse': {
                            'name': 'parent',
                            'typeId': '1'
                        },
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

snapshots['test_schema_success[self_reverse] 1'] = {
    'data': {
        'createProductRelationTypes': {
            'ok': True,
            'productRelationType': {
                'indefArticle': 'a',
                'name': 'plaintiff',
                'plural': 'plaintiffs',
                'relations': {
                    'edges': [
                    ]
                },
                'reverse': {
                    'name': 'plaintiff',
                    'typeId': '3'
                },
                'singular': 'plaintiff',
                'typeId': '3'
            }
        }
    }
}

snapshots['test_schema_success[self_reverse] 2'] = {
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
                        'reverse': {
                            'name': 'parent',
                            'typeId': '1'
                        },
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
                        'reverse': {
                            'name': 'plaintiff',
                            'typeId': '3'
                        },
                        'singular': 'plaintiff',
                        'typeId': '3'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[error-already-exist] 1'] = {
    'data': {
        'createProductRelationTypes': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 6
                }
            ],
            'message': '''(sqlite3.IntegrityError) UNIQUE constraint failed: product_relation_types.name
[SQL: INSERT INTO product_relation_types (name, reverse_type_id, indef_article, singular, plural) VALUES (?, ?, ?, ?, ?)]
[parameters: ('parent', None, 'a', 'parent', 'parents')]
(Background on this error at: http://sqlalche.me/e/gkpj)''',
            'path': [
                'createProductRelationTypes'
            ]
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
                        'reverse': {
                            'name': 'parent',
                            'typeId': '1'
                        },
                        'singular': None,
                        'typeId': '2'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[error-reverse-and-self_reverse] 1'] = {
    'data': {
        'createProductRelationTypes': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 6
                }
            ],
            'message': '"reverse" is given when "self_reverse" is True',
            'path': [
                'createProductRelationTypes'
            ]
        }
    ]
}

snapshots['test_schema_error[error-reverse-and-self_reverse] 2'] = {
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
                        'reverse': {
                            'name': 'parent',
                            'typeId': '1'
                        },
                        'singular': None,
                        'typeId': '2'
                    }
                }
            ]
        }
    }
}
