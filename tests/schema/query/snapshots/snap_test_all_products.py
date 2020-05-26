# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[allProducts-filtes-typeId-one-first-two] 1'] = {
    'data': {
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2019-02-13',
                        'dateProduced': '2019-02-13',
                        'dateUpdated': '2019-02-13',
                        'name': 'lat20190213',
                        'note': '''- This is a dummy test with a lat map
- This should not depend on any beam''',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': '',
                                        'path': 'nersc:/go/to/my/maps',
                                        'pathId': '1'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1001',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'typeId': 1,
                        'type_': {
                            'name': 'map',
                            'typeId': '1'
                        },
                        'updatedBy': 'pwg-pmn'
                    }
                },
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2020-01-20',
                        'dateProduced': '2020-01-20',
                        'dateUpdated': '2020-01-20',
                        'name': 'lat20200120',
                        'note': '''- This is a dummy test with a lat map
- A beam depends on this map''',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': 'lat only',
                                        'path': 'nersc:/go/to/my/maps_v2',
                                        'pathId': '2'
                                    }
                                },
                                {
                                    'node': {
                                        'note': 'lat only',
                                        'path': 'abcde:/path/to/the/maps_v2',
                                        'pathId': '3'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1012',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200123',
                                            'productId': '1130',
                                            'typeId': 2,
                                            'type_': {
                                                'name': 'beam',
                                                'typeId': '2'
                                            }
                                        },
                                        'otherProductId': 1130,
                                        'relationId': '2',
                                        'reverse': {
                                            'relationId': '1',
                                            'typeId': 1,
                                            'type_': {
                                                'name': 'parent',
                                                'typeId': '1'
                                            }
                                        },
                                        'reverseRelationId': 1,
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
                        'updatedBy': 'pwg-pmn'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema[allProducts-filtes-typeName-beam-first-two] 1'] = {
    'data': {
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2018-01-01',
                        'dateProduced': '2018-01-01',
                        'dateUpdated': None,
                        'name': '20180101',
                        'note': '- test entry',
                        'paths': {
                            'edges': [
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1010',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'typeId': 2,
                        'type_': {
                            'name': 'beam',
                            'typeId': '2'
                        },
                        'updatedBy': ''
                    }
                },
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2019-03-04',
                        'dateProduced': '2019-03-04',
                        'dateUpdated': None,
                        'name': '20190304',
                        'note': '- test entry',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': '',
                                        'path': 'BEAM_DEPOT/Beams/20190304',
                                        'pathId': '5'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1070',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'typeId': 2,
                        'type_': {
                            'name': 'beam',
                            'typeId': '2'
                        },
                        'updatedBy': ''
                    }
                }
            ]
        }
    }
}

snapshots['test_schema[allProducts-first-two] 1'] = {
    'data': {
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2019-02-13',
                        'dateProduced': '2019-02-13',
                        'dateUpdated': '2019-02-13',
                        'name': 'lat20190213',
                        'note': '''- This is a dummy test with a lat map
- This should not depend on any beam''',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': '',
                                        'path': 'nersc:/go/to/my/maps',
                                        'pathId': '1'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1001',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'typeId': 1,
                        'type_': {
                            'name': 'map',
                            'typeId': '1'
                        },
                        'updatedBy': 'pwg-pmn'
                    }
                },
                {
                    'node': {
                        'contact': 'abc-def',
                        'datePosted': '2019-03-15',
                        'dateProduced': '2019-03-15',
                        'dateUpdated': None,
                        'name': 'xyz-s1234-20200101',
                        'note': '''- note 1
- note 2''',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': '',
                                        'path': 'nersc:/go/to/my/simulations',
                                        'pathId': '9'
                                    }
                                },
                                {
                                    'node': {
                                        'note': '',
                                        'path': 'abcde:/path/to/the/simulations',
                                        'pathId': '10'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'abc-def',
                        'producedBy': 'abc-def',
                        'productId': '1002',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'typeId': 3,
                        'type_': {
                            'name': 'simulation',
                            'typeId': '3'
                        },
                        'updatedBy': ''
                    }
                }
            ]
        }
    }
}

snapshots['test_schema[allProducts-first-two-sort] 1'] = {
    'data': {
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2020-02-07',
                        'dateProduced': '2020-02-07',
                        'dateUpdated': None,
                        'name': '20200207',
                        'note': '- test entry',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': '',
                                        'path': 'BEAM_DEPOT/Beams/20200207',
                                        'pathId': '8'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1150',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': 'lat20200201',
                                            'productId': '1013',
                                            'typeId': 1,
                                            'type_': {
                                                'name': 'map',
                                                'typeId': '1'
                                            }
                                        },
                                        'otherProductId': 1013,
                                        'relationId': '3',
                                        'reverse': {
                                            'relationId': '4',
                                            'typeId': 2,
                                            'type_': {
                                                'name': 'child',
                                                'typeId': '2'
                                            }
                                        },
                                        'reverseRelationId': 4,
                                        'typeId': 1,
                                        'type_': {
                                            'name': 'parent',
                                            'typeId': '1'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200123',
                                            'productId': '1130',
                                            'typeId': 2,
                                            'type_': {
                                                'name': 'beam',
                                                'typeId': '2'
                                            }
                                        },
                                        'otherProductId': 1130,
                                        'relationId': '5',
                                        'reverse': {
                                            'relationId': '6',
                                            'typeId': 2,
                                            'type_': {
                                                'name': 'child',
                                                'typeId': '2'
                                            }
                                        },
                                        'reverseRelationId': 6,
                                        'typeId': 1,
                                        'type_': {
                                            'name': 'parent',
                                            'typeId': '1'
                                        }
                                    }
                                }
                            ]
                        },
                        'typeId': 2,
                        'type_': {
                            'name': 'beam',
                            'typeId': '2'
                        },
                        'updatedBy': ''
                    }
                },
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2020-02-01',
                        'dateProduced': '2020-02-01',
                        'dateUpdated': '2020-02-01',
                        'name': 'lat20200201',
                        'note': '''- This is a dummy test with a lat map
- A beam depends on this map''',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': 'lat only',
                                        'path': 'nersc:/go/to/my/maps_v3',
                                        'pathId': '4'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1013',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200207',
                                            'productId': '1150',
                                            'typeId': 2,
                                            'type_': {
                                                'name': 'beam',
                                                'typeId': '2'
                                            }
                                        },
                                        'otherProductId': 1150,
                                        'relationId': '4',
                                        'reverse': {
                                            'relationId': '3',
                                            'typeId': 1,
                                            'type_': {
                                                'name': 'parent',
                                                'typeId': '1'
                                            }
                                        },
                                        'reverseRelationId': 3,
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
                        'updatedBy': 'pwg-pmn'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema[allProducts] 1'] = {
    'data': {
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2019-02-13',
                        'dateProduced': '2019-02-13',
                        'dateUpdated': '2019-02-13',
                        'name': 'lat20190213',
                        'note': '''- This is a dummy test with a lat map
- This should not depend on any beam''',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': '',
                                        'path': 'nersc:/go/to/my/maps',
                                        'pathId': '1'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1001',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'typeId': 1,
                        'type_': {
                            'name': 'map',
                            'typeId': '1'
                        },
                        'updatedBy': 'pwg-pmn'
                    }
                },
                {
                    'node': {
                        'contact': 'abc-def',
                        'datePosted': '2019-03-15',
                        'dateProduced': '2019-03-15',
                        'dateUpdated': None,
                        'name': 'xyz-s1234-20200101',
                        'note': '''- note 1
- note 2''',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': '',
                                        'path': 'nersc:/go/to/my/simulations',
                                        'pathId': '9'
                                    }
                                },
                                {
                                    'node': {
                                        'note': '',
                                        'path': 'abcde:/path/to/the/simulations',
                                        'pathId': '10'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'abc-def',
                        'producedBy': 'abc-def',
                        'productId': '1002',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'typeId': 3,
                        'type_': {
                            'name': 'simulation',
                            'typeId': '3'
                        },
                        'updatedBy': ''
                    }
                },
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2018-01-01',
                        'dateProduced': '2018-01-01',
                        'dateUpdated': None,
                        'name': '20180101',
                        'note': '- test entry',
                        'paths': {
                            'edges': [
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1010',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'typeId': 2,
                        'type_': {
                            'name': 'beam',
                            'typeId': '2'
                        },
                        'updatedBy': ''
                    }
                },
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2020-01-20',
                        'dateProduced': '2020-01-20',
                        'dateUpdated': '2020-01-20',
                        'name': 'lat20200120',
                        'note': '''- This is a dummy test with a lat map
- A beam depends on this map''',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': 'lat only',
                                        'path': 'nersc:/go/to/my/maps_v2',
                                        'pathId': '2'
                                    }
                                },
                                {
                                    'node': {
                                        'note': 'lat only',
                                        'path': 'abcde:/path/to/the/maps_v2',
                                        'pathId': '3'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1012',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200123',
                                            'productId': '1130',
                                            'typeId': 2,
                                            'type_': {
                                                'name': 'beam',
                                                'typeId': '2'
                                            }
                                        },
                                        'otherProductId': 1130,
                                        'relationId': '2',
                                        'reverse': {
                                            'relationId': '1',
                                            'typeId': 1,
                                            'type_': {
                                                'name': 'parent',
                                                'typeId': '1'
                                            }
                                        },
                                        'reverseRelationId': 1,
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
                        'updatedBy': 'pwg-pmn'
                    }
                },
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2020-02-01',
                        'dateProduced': '2020-02-01',
                        'dateUpdated': '2020-02-01',
                        'name': 'lat20200201',
                        'note': '''- This is a dummy test with a lat map
- A beam depends on this map''',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': 'lat only',
                                        'path': 'nersc:/go/to/my/maps_v3',
                                        'pathId': '4'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1013',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200207',
                                            'productId': '1150',
                                            'typeId': 2,
                                            'type_': {
                                                'name': 'beam',
                                                'typeId': '2'
                                            }
                                        },
                                        'otherProductId': 1150,
                                        'relationId': '4',
                                        'reverse': {
                                            'relationId': '3',
                                            'typeId': 1,
                                            'type_': {
                                                'name': 'parent',
                                                'typeId': '1'
                                            }
                                        },
                                        'reverseRelationId': 3,
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
                        'updatedBy': 'pwg-pmn'
                    }
                },
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2019-03-04',
                        'dateProduced': '2019-03-04',
                        'dateUpdated': None,
                        'name': '20190304',
                        'note': '- test entry',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': '',
                                        'path': 'BEAM_DEPOT/Beams/20190304',
                                        'pathId': '5'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1070',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'typeId': 2,
                        'type_': {
                            'name': 'beam',
                            'typeId': '2'
                        },
                        'updatedBy': ''
                    }
                },
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2019-06-07',
                        'dateProduced': '2019-06-07',
                        'dateUpdated': None,
                        'name': '20190607',
                        'note': '- test entry',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': '',
                                        'path': 'BEAM_DEPOT/Beams/20190607',
                                        'pathId': '6'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1120',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'typeId': 2,
                        'type_': {
                            'name': 'beam',
                            'typeId': '2'
                        },
                        'updatedBy': ''
                    }
                },
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2020-01-23',
                        'dateProduced': '2020-01-23',
                        'dateUpdated': None,
                        'name': '20200123',
                        'note': '- test entry',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': '',
                                        'path': 'BEAM_DEPOT/Beams/20200123',
                                        'pathId': '7'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1130',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': 'lat20200120',
                                            'productId': '1012',
                                            'typeId': 1,
                                            'type_': {
                                                'name': 'map',
                                                'typeId': '1'
                                            }
                                        },
                                        'otherProductId': 1012,
                                        'relationId': '1',
                                        'reverse': {
                                            'relationId': '2',
                                            'typeId': 2,
                                            'type_': {
                                                'name': 'child',
                                                'typeId': '2'
                                            }
                                        },
                                        'reverseRelationId': 2,
                                        'typeId': 1,
                                        'type_': {
                                            'name': 'parent',
                                            'typeId': '1'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200207',
                                            'productId': '1150',
                                            'typeId': 2,
                                            'type_': {
                                                'name': 'beam',
                                                'typeId': '2'
                                            }
                                        },
                                        'otherProductId': 1150,
                                        'relationId': '6',
                                        'reverse': {
                                            'relationId': '5',
                                            'typeId': 1,
                                            'type_': {
                                                'name': 'parent',
                                                'typeId': '1'
                                            }
                                        },
                                        'reverseRelationId': 5,
                                        'typeId': 2,
                                        'type_': {
                                            'name': 'child',
                                            'typeId': '2'
                                        }
                                    }
                                }
                            ]
                        },
                        'typeId': 2,
                        'type_': {
                            'name': 'beam',
                            'typeId': '2'
                        },
                        'updatedBy': ''
                    }
                },
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2020-02-07',
                        'dateProduced': '2020-02-07',
                        'dateUpdated': None,
                        'name': '20200207',
                        'note': '- test entry',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': '',
                                        'path': 'BEAM_DEPOT/Beams/20200207',
                                        'pathId': '8'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1150',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': 'lat20200201',
                                            'productId': '1013',
                                            'typeId': 1,
                                            'type_': {
                                                'name': 'map',
                                                'typeId': '1'
                                            }
                                        },
                                        'otherProductId': 1013,
                                        'relationId': '3',
                                        'reverse': {
                                            'relationId': '4',
                                            'typeId': 2,
                                            'type_': {
                                                'name': 'child',
                                                'typeId': '2'
                                            }
                                        },
                                        'reverseRelationId': 4,
                                        'typeId': 1,
                                        'type_': {
                                            'name': 'parent',
                                            'typeId': '1'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200123',
                                            'productId': '1130',
                                            'typeId': 2,
                                            'type_': {
                                                'name': 'beam',
                                                'typeId': '2'
                                            }
                                        },
                                        'otherProductId': 1130,
                                        'relationId': '5',
                                        'reverse': {
                                            'relationId': '6',
                                            'typeId': 2,
                                            'type_': {
                                                'name': 'child',
                                                'typeId': '2'
                                            }
                                        },
                                        'reverseRelationId': 6,
                                        'typeId': 1,
                                        'type_': {
                                            'name': 'parent',
                                            'typeId': '1'
                                        }
                                    }
                                }
                            ]
                        },
                        'typeId': 2,
                        'type_': {
                            'name': 'beam',
                            'typeId': '2'
                        },
                        'updatedBy': ''
                    }
                }
            ]
        }
    }
}

snapshots['test_schema[allProducts-filtes-typeId-sort] 1'] = {
    'data': {
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2020-02-01',
                        'dateProduced': '2020-02-01',
                        'dateUpdated': '2020-02-01',
                        'name': 'lat20200201',
                        'note': '''- This is a dummy test with a lat map
- A beam depends on this map''',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': 'lat only',
                                        'path': 'nersc:/go/to/my/maps_v3',
                                        'pathId': '4'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1013',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200207',
                                            'productId': '1150',
                                            'typeId': 2,
                                            'type_': {
                                                'name': 'beam',
                                                'typeId': '2'
                                            }
                                        },
                                        'otherProductId': 1150,
                                        'relationId': '4',
                                        'reverse': {
                                            'relationId': '3',
                                            'typeId': 1,
                                            'type_': {
                                                'name': 'parent',
                                                'typeId': '1'
                                            }
                                        },
                                        'reverseRelationId': 3,
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
                        'updatedBy': 'pwg-pmn'
                    }
                },
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2020-01-20',
                        'dateProduced': '2020-01-20',
                        'dateUpdated': '2020-01-20',
                        'name': 'lat20200120',
                        'note': '''- This is a dummy test with a lat map
- A beam depends on this map''',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': 'lat only',
                                        'path': 'nersc:/go/to/my/maps_v2',
                                        'pathId': '2'
                                    }
                                },
                                {
                                    'node': {
                                        'note': 'lat only',
                                        'path': 'abcde:/path/to/the/maps_v2',
                                        'pathId': '3'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1012',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200123',
                                            'productId': '1130',
                                            'typeId': 2,
                                            'type_': {
                                                'name': 'beam',
                                                'typeId': '2'
                                            }
                                        },
                                        'otherProductId': 1130,
                                        'relationId': '2',
                                        'reverse': {
                                            'relationId': '1',
                                            'typeId': 1,
                                            'type_': {
                                                'name': 'parent',
                                                'typeId': '1'
                                            }
                                        },
                                        'reverseRelationId': 1,
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
                        'updatedBy': 'pwg-pmn'
                    }
                },
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2019-02-13',
                        'dateProduced': '2019-02-13',
                        'dateUpdated': '2019-02-13',
                        'name': 'lat20190213',
                        'note': '''- This is a dummy test with a lat map
- This should not depend on any beam''',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': '',
                                        'path': 'nersc:/go/to/my/maps',
                                        'pathId': '1'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1001',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'typeId': 1,
                        'type_': {
                            'name': 'map',
                            'typeId': '1'
                        },
                        'updatedBy': 'pwg-pmn'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema[allProducts-filtes-typeName-sort] 1'] = {
    'data': {
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2020-02-01',
                        'dateProduced': '2020-02-01',
                        'dateUpdated': '2020-02-01',
                        'name': 'lat20200201',
                        'note': '''- This is a dummy test with a lat map
- A beam depends on this map''',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': 'lat only',
                                        'path': 'nersc:/go/to/my/maps_v3',
                                        'pathId': '4'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1013',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200207',
                                            'productId': '1150',
                                            'typeId': 2,
                                            'type_': {
                                                'name': 'beam',
                                                'typeId': '2'
                                            }
                                        },
                                        'otherProductId': 1150,
                                        'relationId': '4',
                                        'reverse': {
                                            'relationId': '3',
                                            'typeId': 1,
                                            'type_': {
                                                'name': 'parent',
                                                'typeId': '1'
                                            }
                                        },
                                        'reverseRelationId': 3,
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
                        'updatedBy': 'pwg-pmn'
                    }
                },
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2020-01-20',
                        'dateProduced': '2020-01-20',
                        'dateUpdated': '2020-01-20',
                        'name': 'lat20200120',
                        'note': '''- This is a dummy test with a lat map
- A beam depends on this map''',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': 'lat only',
                                        'path': 'nersc:/go/to/my/maps_v2',
                                        'pathId': '2'
                                    }
                                },
                                {
                                    'node': {
                                        'note': 'lat only',
                                        'path': 'abcde:/path/to/the/maps_v2',
                                        'pathId': '3'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1012',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200123',
                                            'productId': '1130',
                                            'typeId': 2,
                                            'type_': {
                                                'name': 'beam',
                                                'typeId': '2'
                                            }
                                        },
                                        'otherProductId': 1130,
                                        'relationId': '2',
                                        'reverse': {
                                            'relationId': '1',
                                            'typeId': 1,
                                            'type_': {
                                                'name': 'parent',
                                                'typeId': '1'
                                            }
                                        },
                                        'reverseRelationId': 1,
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
                        'updatedBy': 'pwg-pmn'
                    }
                },
                {
                    'node': {
                        'contact': 'pwg-pmn',
                        'datePosted': '2019-02-13',
                        'dateProduced': '2019-02-13',
                        'dateUpdated': '2019-02-13',
                        'name': 'lat20190213',
                        'note': '''- This is a dummy test with a lat map
- This should not depend on any beam''',
                        'paths': {
                            'edges': [
                                {
                                    'node': {
                                        'note': '',
                                        'path': 'nersc:/go/to/my/maps',
                                        'pathId': '1'
                                    }
                                }
                            ]
                        },
                        'postedBy': 'pwg-pmn',
                        'producedBy': 'pwg-pmn',
                        'productId': '1001',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'typeId': 1,
                        'type_': {
                            'name': 'map',
                            'typeId': '1'
                        },
                        'updatedBy': 'pwg-pmn'
                    }
                }
            ]
        }
    }
}
