# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[allProducts] 1'] = {
    'data': {
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'name': 'lat20190213',
                        'productId': '1001',
                        'productType': {
                            'name': 'map',
                            'typeId': '1'
                        },
                        'relations': {
                            'edges': [
                            ]
                        }
                    }
                },
                {
                    'node': {
                        'name': 'xyz-s1234-20200101',
                        'productId': '1002',
                        'productType': {
                            'name': 'simulation',
                            'typeId': '3'
                        },
                        'relations': {
                            'edges': [
                            ]
                        }
                    }
                },
                {
                    'node': {
                        'name': '20180101',
                        'productId': '1010',
                        'productType': {
                            'name': 'beam',
                            'typeId': '2'
                        },
                        'relations': {
                            'edges': [
                            ]
                        }
                    }
                },
                {
                    'node': {
                        'name': 'lat20200120',
                        'productId': '1012',
                        'productType': {
                            'name': 'map',
                            'typeId': '1'
                        },
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200123',
                                            'productType': {
                                                'name': 'beam'
                                            }
                                        },
                                        'reverse': {
                                            'type_': {
                                                'name': 'parent'
                                            }
                                        },
                                        'type_': {
                                            'name': 'child'
                                        }
                                    }
                                }
                            ]
                        }
                    }
                },
                {
                    'node': {
                        'name': 'lat20200201',
                        'productId': '1013',
                        'productType': {
                            'name': 'map',
                            'typeId': '1'
                        },
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200207',
                                            'productType': {
                                                'name': 'beam'
                                            }
                                        },
                                        'reverse': {
                                            'type_': {
                                                'name': 'parent'
                                            }
                                        },
                                        'type_': {
                                            'name': 'child'
                                        }
                                    }
                                }
                            ]
                        }
                    }
                },
                {
                    'node': {
                        'name': '20190304',
                        'productId': '1070',
                        'productType': {
                            'name': 'beam',
                            'typeId': '2'
                        },
                        'relations': {
                            'edges': [
                            ]
                        }
                    }
                },
                {
                    'node': {
                        'name': '20190607',
                        'productId': '1120',
                        'productType': {
                            'name': 'beam',
                            'typeId': '2'
                        },
                        'relations': {
                            'edges': [
                            ]
                        }
                    }
                },
                {
                    'node': {
                        'name': '20200123',
                        'productId': '1130',
                        'productType': {
                            'name': 'beam',
                            'typeId': '2'
                        },
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': 'lat20200120',
                                            'productType': {
                                                'name': 'map'
                                            }
                                        },
                                        'reverse': {
                                            'type_': {
                                                'name': 'child'
                                            }
                                        },
                                        'type_': {
                                            'name': 'parent'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200207',
                                            'productType': {
                                                'name': 'beam'
                                            }
                                        },
                                        'reverse': {
                                            'type_': {
                                                'name': 'parent'
                                            }
                                        },
                                        'type_': {
                                            'name': 'child'
                                        }
                                    }
                                }
                            ]
                        }
                    }
                },
                {
                    'node': {
                        'name': '20200207',
                        'productId': '1150',
                        'productType': {
                            'name': 'beam',
                            'typeId': '2'
                        },
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': 'lat20200201',
                                            'productType': {
                                                'name': 'map'
                                            }
                                        },
                                        'reverse': {
                                            'type_': {
                                                'name': 'child'
                                            }
                                        },
                                        'type_': {
                                            'name': 'parent'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200123',
                                            'productType': {
                                                'name': 'beam'
                                            }
                                        },
                                        'reverse': {
                                            'type_': {
                                                'name': 'child'
                                            }
                                        },
                                        'type_': {
                                            'name': 'parent'
                                        }
                                    }
                                }
                            ]
                        }
                    }
                }
            ]
        }
    }
}

snapshots['test_schema[allProducts-filtes-typeId-one-first-two] 1'] = {
    'data': {
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'name': 'lat20190213'
                    }
                },
                {
                    'node': {
                        'name': 'lat20200120'
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
                        'name': 'lat20190213'
                    }
                },
                {
                    'node': {
                        'name': 'xyz-s1234-20200101'
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
                        'name': '20200207'
                    }
                },
                {
                    'node': {
                        'name': 'lat20200201'
                    }
                }
            ]
        }
    }
}
