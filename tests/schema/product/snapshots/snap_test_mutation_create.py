# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[create] 1'] = {
    'data': {
        'createProduct': {
            'ok': True,
            'product': {
                'contact': 'contact-person',
                'datePosted': '2020-05-04',
                'dateProduced': '2020-02-20',
                'dateUpdated': None,
                'name': 'product1',
                'note': '- Item 1',
                'paths': {
                    'edges': [
                        {
                            'node': {
                                'note': None,
                                'path': '/path/to/new/product1',
                                'pathId': '11'
                            }
                        },
                        {
                            'node': {
                                'note': None,
                                'path': '/another/location/of/product1',
                                'pathId': '12'
                            }
                        }
                    ]
                },
                'postedBy': 'poster',
                'producedBy': 'producer',
                'productId': '1151',
                'relations': {
                    'edges': [
                    ]
                },
                'typeId': 1,
                'type_': {
                    'name': 'map',
                    'typeId': '1'
                },
                'updatedBy': None
            }
        }
    }
}

snapshots['test_schema_success[create] 2'] = {
    'data': {
        'allProductFilePaths': {
            'edges': [
                {
                    'node': {
                        'pathId': '1'
                    }
                },
                {
                    'node': {
                        'pathId': '2'
                    }
                },
                {
                    'node': {
                        'pathId': '3'
                    }
                },
                {
                    'node': {
                        'pathId': '4'
                    }
                },
                {
                    'node': {
                        'pathId': '5'
                    }
                },
                {
                    'node': {
                        'pathId': '6'
                    }
                },
                {
                    'node': {
                        'pathId': '7'
                    }
                },
                {
                    'node': {
                        'pathId': '8'
                    }
                },
                {
                    'node': {
                        'pathId': '9'
                    }
                },
                {
                    'node': {
                        'pathId': '10'
                    }
                },
                {
                    'node': {
                        'pathId': '11'
                    }
                },
                {
                    'node': {
                        'pathId': '12'
                    }
                }
            ]
        },
        'allProductRelations': {
            'edges': [
                {
                    'node': {
                        'relationId': '1'
                    }
                },
                {
                    'node': {
                        'relationId': '2'
                    }
                },
                {
                    'node': {
                        'relationId': '3'
                    }
                },
                {
                    'node': {
                        'relationId': '4'
                    }
                },
                {
                    'node': {
                        'relationId': '5'
                    }
                },
                {
                    'node': {
                        'relationId': '6'
                    }
                }
            ]
        },
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'productId': '1001'
                    }
                },
                {
                    'node': {
                        'productId': '1002'
                    }
                },
                {
                    'node': {
                        'productId': '1010'
                    }
                },
                {
                    'node': {
                        'productId': '1012'
                    }
                },
                {
                    'node': {
                        'productId': '1013'
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
                },
                {
                    'node': {
                        'productId': '1151'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[error-no-name] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 24,
                    'line': 2
                }
            ],
            'message': '''Variable "$input" got invalid value {"contact": "contact-person", "dateProduced": "2020-02-20", "note": "- Item 1", "paths": ["/path/to/new/product1", "/another/location/of/product1"], "postedBy": "poster", "producedBy": "producer", "typeId": 1}.
In field "name": Expected "String!", found null.'''
        }
    ]
}

snapshots['test_schema_error[error-no-name] 2'] = {
    'data': {
        'allProductFilePaths': {
            'edges': [
                {
                    'node': {
                        'pathId': '1'
                    }
                },
                {
                    'node': {
                        'pathId': '2'
                    }
                },
                {
                    'node': {
                        'pathId': '3'
                    }
                },
                {
                    'node': {
                        'pathId': '4'
                    }
                },
                {
                    'node': {
                        'pathId': '5'
                    }
                },
                {
                    'node': {
                        'pathId': '6'
                    }
                },
                {
                    'node': {
                        'pathId': '7'
                    }
                },
                {
                    'node': {
                        'pathId': '8'
                    }
                },
                {
                    'node': {
                        'pathId': '9'
                    }
                },
                {
                    'node': {
                        'pathId': '10'
                    }
                }
            ]
        },
        'allProductRelations': {
            'edges': [
                {
                    'node': {
                        'relationId': '1'
                    }
                },
                {
                    'node': {
                        'relationId': '2'
                    }
                },
                {
                    'node': {
                        'relationId': '3'
                    }
                },
                {
                    'node': {
                        'relationId': '4'
                    }
                },
                {
                    'node': {
                        'relationId': '5'
                    }
                },
                {
                    'node': {
                        'relationId': '6'
                    }
                }
            ]
        },
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'productId': '1001'
                    }
                },
                {
                    'node': {
                        'productId': '1002'
                    }
                },
                {
                    'node': {
                        'productId': '1010'
                    }
                },
                {
                    'node': {
                        'productId': '1012'
                    }
                },
                {
                    'node': {
                        'productId': '1013'
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

snapshots['test_schema_success[minimum] 1'] = {
    'data': {
        'createProduct': {
            'ok': True,
            'product': {
                'contact': None,
                'datePosted': '2020-05-04',
                'dateProduced': None,
                'dateUpdated': None,
                'name': 'product1',
                'note': None,
                'paths': {
                    'edges': [
                    ]
                },
                'postedBy': None,
                'producedBy': None,
                'productId': '1151',
                'relations': {
                    'edges': [
                    ]
                },
                'typeId': 1,
                'type_': {
                    'name': 'map',
                    'typeId': '1'
                },
                'updatedBy': None
            }
        }
    }
}

snapshots['test_schema_success[minimum] 2'] = {
    'data': {
        'allProductFilePaths': {
            'edges': [
                {
                    'node': {
                        'pathId': '1'
                    }
                },
                {
                    'node': {
                        'pathId': '2'
                    }
                },
                {
                    'node': {
                        'pathId': '3'
                    }
                },
                {
                    'node': {
                        'pathId': '4'
                    }
                },
                {
                    'node': {
                        'pathId': '5'
                    }
                },
                {
                    'node': {
                        'pathId': '6'
                    }
                },
                {
                    'node': {
                        'pathId': '7'
                    }
                },
                {
                    'node': {
                        'pathId': '8'
                    }
                },
                {
                    'node': {
                        'pathId': '9'
                    }
                },
                {
                    'node': {
                        'pathId': '10'
                    }
                }
            ]
        },
        'allProductRelations': {
            'edges': [
                {
                    'node': {
                        'relationId': '1'
                    }
                },
                {
                    'node': {
                        'relationId': '2'
                    }
                },
                {
                    'node': {
                        'relationId': '3'
                    }
                },
                {
                    'node': {
                        'relationId': '4'
                    }
                },
                {
                    'node': {
                        'relationId': '5'
                    }
                },
                {
                    'node': {
                        'relationId': '6'
                    }
                }
            ]
        },
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'productId': '1001'
                    }
                },
                {
                    'node': {
                        'productId': '1002'
                    }
                },
                {
                    'node': {
                        'productId': '1010'
                    }
                },
                {
                    'node': {
                        'productId': '1012'
                    }
                },
                {
                    'node': {
                        'productId': '1013'
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
                },
                {
                    'node': {
                        'productId': '1151'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_success[the-same-name-different-type] 1'] = {
    'data': {
        'createProduct': {
            'ok': True,
            'product': {
                'contact': 'contact-person',
                'datePosted': '2020-05-04',
                'dateProduced': None,
                'dateUpdated': None,
                'name': 'lat20190213',
                'note': None,
                'paths': {
                    'edges': [
                        {
                            'node': {
                                'note': None,
                                'path': '/path/to/new/product1',
                                'pathId': '11'
                            }
                        },
                        {
                            'node': {
                                'note': None,
                                'path': '/another/location/of/product1',
                                'pathId': '12'
                            }
                        }
                    ]
                },
                'postedBy': None,
                'producedBy': 'pwg-pmn',
                'productId': '1151',
                'relations': {
                    'edges': [
                    ]
                },
                'typeId': 2,
                'type_': {
                    'name': 'beam',
                    'typeId': '2'
                },
                'updatedBy': None
            }
        }
    }
}

snapshots['test_schema_success[the-same-name-different-type] 2'] = {
    'data': {
        'allProductFilePaths': {
            'edges': [
                {
                    'node': {
                        'pathId': '1'
                    }
                },
                {
                    'node': {
                        'pathId': '2'
                    }
                },
                {
                    'node': {
                        'pathId': '3'
                    }
                },
                {
                    'node': {
                        'pathId': '4'
                    }
                },
                {
                    'node': {
                        'pathId': '5'
                    }
                },
                {
                    'node': {
                        'pathId': '6'
                    }
                },
                {
                    'node': {
                        'pathId': '7'
                    }
                },
                {
                    'node': {
                        'pathId': '8'
                    }
                },
                {
                    'node': {
                        'pathId': '9'
                    }
                },
                {
                    'node': {
                        'pathId': '10'
                    }
                },
                {
                    'node': {
                        'pathId': '11'
                    }
                },
                {
                    'node': {
                        'pathId': '12'
                    }
                }
            ]
        },
        'allProductRelations': {
            'edges': [
                {
                    'node': {
                        'relationId': '1'
                    }
                },
                {
                    'node': {
                        'relationId': '2'
                    }
                },
                {
                    'node': {
                        'relationId': '3'
                    }
                },
                {
                    'node': {
                        'relationId': '4'
                    }
                },
                {
                    'node': {
                        'relationId': '5'
                    }
                },
                {
                    'node': {
                        'relationId': '6'
                    }
                }
            ]
        },
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'productId': '1001'
                    }
                },
                {
                    'node': {
                        'productId': '1002'
                    }
                },
                {
                    'node': {
                        'productId': '1010'
                    }
                },
                {
                    'node': {
                        'productId': '1012'
                    }
                },
                {
                    'node': {
                        'productId': '1013'
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
                },
                {
                    'node': {
                        'productId': '1151'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[error-the-same-type-and-name] 1'] = {
    'data': {
        'createProduct': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 3
                }
            ],
            'message': '''(sqlite3.IntegrityError) UNIQUE constraint failed: products.type_id, products.name
[SQL: INSERT INTO products (type_id, name, contact, date_produced, produced_by, date_posted, posted_by, date_updated, updated_by, note) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)]
[parameters: (1, 'lat20190213', 'contact-person', None, 'pwg-pmn', '2020-05-04', None, None, None, None)]
(Background on this error at: http://sqlalche.me/e/gkpj)''',
            'path': [
                'createProduct'
            ]
        }
    ]
}

snapshots['test_schema_error[error-the-same-type-and-name] 2'] = {
    'data': {
        'allProductFilePaths': {
            'edges': [
                {
                    'node': {
                        'pathId': '1'
                    }
                },
                {
                    'node': {
                        'pathId': '2'
                    }
                },
                {
                    'node': {
                        'pathId': '3'
                    }
                },
                {
                    'node': {
                        'pathId': '4'
                    }
                },
                {
                    'node': {
                        'pathId': '5'
                    }
                },
                {
                    'node': {
                        'pathId': '6'
                    }
                },
                {
                    'node': {
                        'pathId': '7'
                    }
                },
                {
                    'node': {
                        'pathId': '8'
                    }
                },
                {
                    'node': {
                        'pathId': '9'
                    }
                },
                {
                    'node': {
                        'pathId': '10'
                    }
                }
            ]
        },
        'allProductRelations': {
            'edges': [
                {
                    'node': {
                        'relationId': '1'
                    }
                },
                {
                    'node': {
                        'relationId': '2'
                    }
                },
                {
                    'node': {
                        'relationId': '3'
                    }
                },
                {
                    'node': {
                        'relationId': '4'
                    }
                },
                {
                    'node': {
                        'relationId': '5'
                    }
                },
                {
                    'node': {
                        'relationId': '6'
                    }
                }
            ]
        },
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'productId': '1001'
                    }
                },
                {
                    'node': {
                        'productId': '1002'
                    }
                },
                {
                    'node': {
                        'productId': '1010'
                    }
                },
                {
                    'node': {
                        'productId': '1012'
                    }
                },
                {
                    'node': {
                        'productId': '1013'
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
