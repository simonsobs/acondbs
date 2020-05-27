# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[createProduct-all-options] 1'] = {
    'data': {
        'createProduct': {
            'product': {
                'name': 'product1'
            }
        }
    }
}

snapshots['test_schema_success[createProduct-all-options] 2'] = {
    'data': {
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
                            'path': '/path/to/new/product1'
                        }
                    },
                    {
                        'node': {
                            'path': '/another/location/of/product1'
                        }
                    }
                ]
            },
            'postedBy': 'poster',
            'producedBy': 'producer',
            'type_': {
                'name': 'map'
            },
            'updatedBy': None
        }
    }
}

snapshots['test_schema_success[createProduct-selective-options] 1'] = {
    'data': {
        'createProduct': {
            'product': {
                'name': 'product1'
            }
        }
    }
}

snapshots['test_schema_success[createProduct-selective-options] 2'] = {
    'data': {
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
            'producedBy': 'pwg-pmn',
            'type_': {
                'name': 'map'
            },
            'updatedBy': None
        }
    }
}

snapshots['test_schema_success[createProduct-error-the-same-name-different-type] 1'] = {
    'data': {
        'createProduct': {
            'product': {
                'name': 'lat20190213'
            }
        }
    }
}

snapshots['test_schema_success[createProduct-error-the-same-name-different-type] 2'] = {
    'data': {
        'product': {
            'contact': None,
            'datePosted': '2020-05-04',
            'dateProduced': None,
            'dateUpdated': None,
            'name': 'lat20190213',
            'note': None,
            'paths': {
                'edges': [
                    {
                        'node': {
                            'path': '/path/to/new/product1'
                        }
                    },
                    {
                        'node': {
                            'path': '/another/location/of/product1'
                        }
                    }
                ]
            },
            'postedBy': None,
            'producedBy': 'pwg-pmn',
            'type_': {
                'name': 'beam'
            },
            'updatedBy': None
        }
    }
}

snapshots['test_schema_error[createProduct-error-no-name] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 34,
                    'line': 3
                }
            ],
            'message': '''Argument "input" has invalid value {typeId: 1, producedBy: "pwg-pmn", paths: ["/path/to/new/product1", "/another/location/of/product1"]}.
In field "name": Expected "String!", found null.'''
        }
    ]
}

snapshots['test_schema_error[createProduct-error-no-name] 2'] = {
    'data': {
        'allProductFilePaths': {
            'edges': [
                {
                    'node': {
                        'path': 'nersc:/go/to/my/maps',
                        'productId': 1001
                    }
                },
                {
                    'node': {
                        'path': 'nersc:/go/to/my/maps_v2',
                        'productId': 1012
                    }
                },
                {
                    'node': {
                        'path': 'abcde:/path/to/the/maps_v2',
                        'productId': 1012
                    }
                },
                {
                    'node': {
                        'path': 'nersc:/go/to/my/maps_v3',
                        'productId': 1013
                    }
                },
                {
                    'node': {
                        'path': 'BEAM_DEPOT/Beams/20190304',
                        'productId': 1070
                    }
                },
                {
                    'node': {
                        'path': 'BEAM_DEPOT/Beams/20190607',
                        'productId': 1120
                    }
                },
                {
                    'node': {
                        'path': 'BEAM_DEPOT/Beams/20200123',
                        'productId': 1130
                    }
                },
                {
                    'node': {
                        'path': 'BEAM_DEPOT/Beams/20200207',
                        'productId': 1150
                    }
                },
                {
                    'node': {
                        'path': 'nersc:/go/to/my/simulations',
                        'productId': 1002
                    }
                },
                {
                    'node': {
                        'path': 'abcde:/path/to/the/simulations',
                        'productId': 1002
                    }
                }
            ]
        },
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'name': 'lat20190213',
                        'productId': '1001'
                    }
                },
                {
                    'node': {
                        'name': 'xyz-s1234-20200101',
                        'productId': '1002'
                    }
                },
                {
                    'node': {
                        'name': '20180101',
                        'productId': '1010'
                    }
                },
                {
                    'node': {
                        'name': 'lat20200120',
                        'productId': '1012'
                    }
                },
                {
                    'node': {
                        'name': 'lat20200201',
                        'productId': '1013'
                    }
                },
                {
                    'node': {
                        'name': '20190304',
                        'productId': '1070'
                    }
                },
                {
                    'node': {
                        'name': '20190607',
                        'productId': '1120'
                    }
                },
                {
                    'node': {
                        'name': '20200123',
                        'productId': '1130'
                    }
                },
                {
                    'node': {
                        'name': '20200207',
                        'productId': '1150'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[createProduct-error-the-same-type-and-name] 1'] = {
    'data': {
        'createProduct': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': '''(sqlite3.IntegrityError) UNIQUE constraint failed: products.type_id, products.name
[SQL: INSERT INTO products (type_id, name, contact, date_produced, produced_by, date_posted, posted_by, date_updated, updated_by, note) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)]
[parameters: (1, 'lat20190213', None, None, 'pwg-pmn', '2020-05-04', None, None, None, None)]
(Background on this error at: http://sqlalche.me/e/gkpj)''',
            'path': [
                'createProduct'
            ]
        }
    ]
}

snapshots['test_schema_error[createProduct-error-the-same-type-and-name] 2'] = {
    'data': {
        'allProductFilePaths': {
            'edges': [
                {
                    'node': {
                        'path': 'nersc:/go/to/my/maps',
                        'productId': 1001
                    }
                },
                {
                    'node': {
                        'path': 'nersc:/go/to/my/maps_v2',
                        'productId': 1012
                    }
                },
                {
                    'node': {
                        'path': 'abcde:/path/to/the/maps_v2',
                        'productId': 1012
                    }
                },
                {
                    'node': {
                        'path': 'nersc:/go/to/my/maps_v3',
                        'productId': 1013
                    }
                },
                {
                    'node': {
                        'path': 'BEAM_DEPOT/Beams/20190304',
                        'productId': 1070
                    }
                },
                {
                    'node': {
                        'path': 'BEAM_DEPOT/Beams/20190607',
                        'productId': 1120
                    }
                },
                {
                    'node': {
                        'path': 'BEAM_DEPOT/Beams/20200123',
                        'productId': 1130
                    }
                },
                {
                    'node': {
                        'path': 'BEAM_DEPOT/Beams/20200207',
                        'productId': 1150
                    }
                },
                {
                    'node': {
                        'path': 'nersc:/go/to/my/simulations',
                        'productId': 1002
                    }
                },
                {
                    'node': {
                        'path': 'abcde:/path/to/the/simulations',
                        'productId': 1002
                    }
                }
            ]
        },
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'name': 'lat20190213',
                        'productId': '1001'
                    }
                },
                {
                    'node': {
                        'name': 'xyz-s1234-20200101',
                        'productId': '1002'
                    }
                },
                {
                    'node': {
                        'name': '20180101',
                        'productId': '1010'
                    }
                },
                {
                    'node': {
                        'name': 'lat20200120',
                        'productId': '1012'
                    }
                },
                {
                    'node': {
                        'name': 'lat20200201',
                        'productId': '1013'
                    }
                },
                {
                    'node': {
                        'name': '20190304',
                        'productId': '1070'
                    }
                },
                {
                    'node': {
                        'name': '20190607',
                        'productId': '1120'
                    }
                },
                {
                    'node': {
                        'name': '20200123',
                        'productId': '1130'
                    }
                },
                {
                    'node': {
                        'name': '20200207',
                        'productId': '1150'
                    }
                }
            ]
        }
    }
}
