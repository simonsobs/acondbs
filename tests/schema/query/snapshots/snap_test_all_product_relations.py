# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[query] 1'] = {
    'data': {
        'allProductRelations': {
            'edges': [
                {
                    'node': {
                        'other': {
                            'name': 'lat20200120',
                            'productId': '1012'
                        },
                        'relationId': '1',
                        'reverse': {
                            'relationId': '2'
                        },
                        'self_': {
                            'name': '20200123',
                            'productId': '1130'
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
                            'name': '20200123',
                            'productId': '1130'
                        },
                        'relationId': '2',
                        'reverse': {
                            'relationId': '1'
                        },
                        'self_': {
                            'name': 'lat20200120',
                            'productId': '1012'
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
                            'name': 'lat20200201',
                            'productId': '1013'
                        },
                        'relationId': '3',
                        'reverse': {
                            'relationId': '4'
                        },
                        'self_': {
                            'name': '20200207',
                            'productId': '1150'
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
                            'name': '20200207',
                            'productId': '1150'
                        },
                        'relationId': '4',
                        'reverse': {
                            'relationId': '3'
                        },
                        'self_': {
                            'name': 'lat20200201',
                            'productId': '1013'
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
                            'name': '20200123',
                            'productId': '1130'
                        },
                        'relationId': '5',
                        'reverse': {
                            'relationId': '6'
                        },
                        'self_': {
                            'name': '20200207',
                            'productId': '1150'
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
                            'name': '20200207',
                            'productId': '1150'
                        },
                        'relationId': '6',
                        'reverse': {
                            'relationId': '5'
                        },
                        'self_': {
                            'name': '20200123',
                            'productId': '1130'
                        },
                        'type_': {
                            'name': 'child',
                            'typeId': '2'
                        }
                    }
                }
            ]
        }
    }
}
