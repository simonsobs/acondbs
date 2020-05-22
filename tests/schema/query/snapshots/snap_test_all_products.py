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
                        'relations': {
                            'edges': [
                            ]
                        },
                        'type_': {
                            'name': 'map',
                            'typeId': '1'
                        }
                    }
                },
                {
                    'node': {
                        'name': 'xyz-s1234-20200101',
                        'productId': '1002',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'type_': {
                            'name': 'simulation',
                            'typeId': '3'
                        }
                    }
                },
                {
                    'node': {
                        'name': '20180101',
                        'productId': '1010',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'type_': {
                            'name': 'beam',
                            'typeId': '2'
                        }
                    }
                },
                {
                    'node': {
                        'name': 'lat20200120',
                        'productId': '1012',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200123',
                                            'type_': {
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
                        },
                        'type_': {
                            'name': 'map',
                            'typeId': '1'
                        }
                    }
                },
                {
                    'node': {
                        'name': 'lat20200201',
                        'productId': '1013',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200207',
                                            'type_': {
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
                        },
                        'type_': {
                            'name': 'map',
                            'typeId': '1'
                        }
                    }
                },
                {
                    'node': {
                        'name': '20190304',
                        'productId': '1070',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'type_': {
                            'name': 'beam',
                            'typeId': '2'
                        }
                    }
                },
                {
                    'node': {
                        'name': '20190607',
                        'productId': '1120',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'type_': {
                            'name': 'beam',
                            'typeId': '2'
                        }
                    }
                },
                {
                    'node': {
                        'name': '20200123',
                        'productId': '1130',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': 'lat20200120',
                                            'type_': {
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
                                            'type_': {
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
                        },
                        'type_': {
                            'name': 'beam',
                            'typeId': '2'
                        }
                    }
                },
                {
                    'node': {
                        'name': '20200207',
                        'productId': '1150',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': 'lat20200201',
                                            'type_': {
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
                                            'type_': {
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
                        },
                        'type_': {
                            'name': 'beam',
                            'typeId': '2'
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

snapshots['test_schema[allProducts-filtes-typeName-beam-first-two] 1'] = {
    'data': {
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'name': '20180101'
                    }
                },
                {
                    'node': {
                        'name': '20190304'
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
