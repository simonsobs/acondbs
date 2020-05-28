# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[update] 1'] = {
    'data': {
        'updateProductType': {
            'ok': True,
            'productType': {
                'icon': 'mdi-compass',
                'indefArticle': 'a',
                'name': 'map',
                'order': 5,
                'plural': 'compasses',
                'products': {
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
                        },
                        {
                            'node': {
                                'name': 'lat20200201'
                            }
                        }
                    ]
                },
                'singular': 'compass',
                'typeId': '1'
            }
        }
    }
}

snapshots['test_schema_success[update] 2'] = {
    'data': {
        'allProductTypes': {
            'edges': [
                {
                    'node': {
                        'name': 'map'
                    }
                },
                {
                    'node': {
                        'name': 'beam'
                    }
                },
                {
                    'node': {
                        'name': 'simulation'
                    }
                },
                {
                    'node': {
                        'name': 'anchor'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[error-nonexistent] 1'] = {
    'data': {
        'updateProductType': None
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
                'updateProductType'
            ]
        }
    ]
}

snapshots['test_schema_error[error-nonexistent] 2'] = {
    'data': {
        'allProductTypes': {
            'edges': [
                {
                    'node': {
                        'name': 'map'
                    }
                },
                {
                    'node': {
                        'name': 'beam'
                    }
                },
                {
                    'node': {
                        'name': 'simulation'
                    }
                },
                {
                    'node': {
                        'name': 'anchor'
                    }
                }
            ]
        }
    }
}
