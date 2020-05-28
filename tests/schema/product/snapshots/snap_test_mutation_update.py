# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_error[error-immutable-fields] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 28,
                    'line': 2
                }
            ],
            'message': '''Variable "$input" got invalid value {"name": "new-name"}.
In field "name": Unknown field.'''
        }
    ]
}

snapshots['test_schema_error[error-immutable-fields] 2'] = {
    'data': {
        'allProductFilePaths': {
            'edges': [
                {
                    'node': {
                        'path': 'site1:/path/to/map1'
                    }
                },
                {
                    'node': {
                        'path': 'site2:/another/way/map1'
                    }
                },
                {
                    'node': {
                        'path': 'site1:/path/to/beam2'
                    }
                },
                {
                    'node': {
                        'path': 'site1:/path/to/beam1'
                    }
                },
                {
                    'node': {
                        'path': 'site2:/another/way/beam1'
                    }
                },
                {
                    'node': {
                        'path': 'site1:/path/to/map2'
                    }
                },
                {
                    'node': {
                        'path': 'site1:/path/to/map3'
                    }
                },
                {
                    'node': {
                        'path': 'site2:/another/way/map3'
                    }
                }
            ]
        },
        'allProductRelations': {
            'edges': [
                {
                    'node': {
                        'other': {
                            'name': 'beam1'
                        },
                        'self_': {
                            'name': 'map1'
                        },
                        'type_': {
                            'name': 'child'
                        }
                    }
                },
                {
                    'node': {
                        'other': {
                            'name': 'map1'
                        },
                        'self_': {
                            'name': 'beam1'
                        },
                        'type_': {
                            'name': 'parent'
                        }
                    }
                },
                {
                    'node': {
                        'other': {
                            'name': 'beam2'
                        },
                        'self_': {
                            'name': 'beam1'
                        },
                        'type_': {
                            'name': 'child'
                        }
                    }
                },
                {
                    'node': {
                        'other': {
                            'name': 'map1'
                        },
                        'self_': {
                            'name': 'beam2'
                        },
                        'type_': {
                            'name': 'parent'
                        }
                    }
                },
                {
                    'node': {
                        'other': {
                            'name': 'beam1'
                        },
                        'self_': {
                            'name': 'beam2'
                        },
                        'type_': {
                            'name': 'parent'
                        }
                    }
                },
                {
                    'node': {
                        'other': {
                            'name': 'beam2'
                        },
                        'self_': {
                            'name': 'map1'
                        },
                        'type_': {
                            'name': 'child'
                        }
                    }
                }
            ]
        },
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'name': 'map1'
                    }
                },
                {
                    'node': {
                        'name': 'map2'
                    }
                },
                {
                    'node': {
                        'name': 'map3'
                    }
                },
                {
                    'node': {
                        'name': 'beam1'
                    }
                },
                {
                    'node': {
                        'name': 'beam2'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_success[update] 1'] = {
    'data': {
        'updateProduct': {
            'ok': True,
            'product': {
                'contact': 'new-contact',
                'datePosted': None,
                'dateProduced': '2020-02-01',
                'dateUpdated': '2020-05-04',
                'name': 'map1',
                'note': '- updated note 123',
                'paths': {
                    'edges': [
                        {
                            'node': {
                                'note': None,
                                'path': 'site1:/path/to/map1',
                                'pathId': '1'
                            }
                        },
                        {
                            'node': {
                                'note': None,
                                'path': 'site2:/another/way/map1',
                                'pathId': '2'
                            }
                        }
                    ]
                },
                'postedBy': None,
                'producedBy': None,
                'productId': '1',
                'relations': {
                    'edges': [
                        {
                            'node': {
                                'other': {
                                    'name': 'beam1',
                                    'productId': '4',
                                    'typeId': 2,
                                    'type_': {
                                        'name': 'beam',
                                        'typeId': '2'
                                    }
                                },
                                'otherProductId': 4,
                                'relationId': '1',
                                'reverse': {
                                    'relationId': '2',
                                    'typeId': 1,
                                    'type_': {
                                        'name': 'parent',
                                        'typeId': '1'
                                    }
                                },
                                'reverseRelationId': 2,
                                'typeId': 2,
                                'type_': {
                                    'name': 'child',
                                    'typeId': '2'
                                }
                            }
                        },
                        {
                            'node': {
                                'other': {
                                    'name': 'beam2',
                                    'productId': '5',
                                    'typeId': 2,
                                    'type_': {
                                        'name': 'beam',
                                        'typeId': '2'
                                    }
                                },
                                'otherProductId': 5,
                                'relationId': '6',
                                'reverse': {
                                    'relationId': '4',
                                    'typeId': 1,
                                    'type_': {
                                        'name': 'parent',
                                        'typeId': '1'
                                    }
                                },
                                'reverseRelationId': 4,
                                'typeId': 2,
                                'type_': {
                                    'name': 'child',
                                    'typeId': '2'
                                }
                            }
                        }
                    ]
                },
                'typeId': 1,
                'type_': {
                    'name': 'map',
                    'typeId': '1'
                },
                'updatedBy': 'updater'
            }
        }
    }
}

snapshots['test_schema_success[update] 2'] = {
    'data': {
        'allProductFilePaths': {
            'edges': [
                {
                    'node': {
                        'path': 'site1:/path/to/map1'
                    }
                },
                {
                    'node': {
                        'path': 'site2:/another/way/map1'
                    }
                },
                {
                    'node': {
                        'path': 'site1:/path/to/beam2'
                    }
                },
                {
                    'node': {
                        'path': 'site1:/path/to/beam1'
                    }
                },
                {
                    'node': {
                        'path': 'site2:/another/way/beam1'
                    }
                },
                {
                    'node': {
                        'path': 'site1:/path/to/map2'
                    }
                },
                {
                    'node': {
                        'path': 'site1:/path/to/map3'
                    }
                },
                {
                    'node': {
                        'path': 'site2:/another/way/map3'
                    }
                }
            ]
        },
        'allProductRelations': {
            'edges': [
                {
                    'node': {
                        'other': {
                            'name': 'beam1'
                        },
                        'self_': {
                            'name': 'map1'
                        },
                        'type_': {
                            'name': 'child'
                        }
                    }
                },
                {
                    'node': {
                        'other': {
                            'name': 'map1'
                        },
                        'self_': {
                            'name': 'beam1'
                        },
                        'type_': {
                            'name': 'parent'
                        }
                    }
                },
                {
                    'node': {
                        'other': {
                            'name': 'beam2'
                        },
                        'self_': {
                            'name': 'beam1'
                        },
                        'type_': {
                            'name': 'child'
                        }
                    }
                },
                {
                    'node': {
                        'other': {
                            'name': 'map1'
                        },
                        'self_': {
                            'name': 'beam2'
                        },
                        'type_': {
                            'name': 'parent'
                        }
                    }
                },
                {
                    'node': {
                        'other': {
                            'name': 'beam1'
                        },
                        'self_': {
                            'name': 'beam2'
                        },
                        'type_': {
                            'name': 'parent'
                        }
                    }
                },
                {
                    'node': {
                        'other': {
                            'name': 'beam2'
                        },
                        'self_': {
                            'name': 'map1'
                        },
                        'type_': {
                            'name': 'child'
                        }
                    }
                }
            ]
        },
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'name': 'map1'
                    }
                },
                {
                    'node': {
                        'name': 'map2'
                    }
                },
                {
                    'node': {
                        'name': 'map3'
                    }
                },
                {
                    'node': {
                        'name': 'beam1'
                    }
                },
                {
                    'node': {
                        'name': 'beam2'
                    }
                }
            ]
        }
    }
}
