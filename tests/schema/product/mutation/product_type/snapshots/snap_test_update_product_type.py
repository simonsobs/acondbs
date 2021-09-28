# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_error[error-nonexistent] 1'] = {
    'data': {
        'allProductTypes': {
            'edges': [
                {
                    'node': {
                        'fields': {
                            'edges': [
                            ]
                        },
                        'icon': 'mdi-spotlight-beam',
                        'indefArticle': 'a',
                        'name': 'beam',
                        'order': 1,
                        'plural': 'beams',
                        'products': {
                            'edges': [
                            ]
                        },
                        'singular': 'beam',
                        'typeId': '2'
                    }
                },
                {
                    'node': {
                        'fields': {
                            'edges': [
                            ]
                        },
                        'icon': 'mdi-map',
                        'indefArticle': 'a',
                        'name': 'map',
                        'order': 2,
                        'plural': 'maps',
                        'products': {
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
                                }
                            ]
                        },
                        'singular': 'map',
                        'typeId': '1'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_success[update] 1'] = {
    'data': {
        'updateProductType': {
            'ok': True,
            'productType': {
                'fields': {
                    'edges': [
                    ]
                },
                'icon': 'mdi-compass',
                'indefArticle': 'a',
                'name': 'map',
                'order': 5,
                'plural': 'compasses',
                'products': {
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
                        'fields': {
                            'edges': [
                            ]
                        },
                        'icon': 'mdi-spotlight-beam',
                        'indefArticle': 'a',
                        'name': 'beam',
                        'order': 1,
                        'plural': 'beams',
                        'products': {
                            'edges': [
                            ]
                        },
                        'singular': 'beam',
                        'typeId': '2'
                    }
                },
                {
                    'node': {
                        'fields': {
                            'edges': [
                            ]
                        },
                        'icon': 'mdi-compass',
                        'indefArticle': 'a',
                        'name': 'map',
                        'order': 5,
                        'plural': 'compasses',
                        'products': {
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
                                }
                            ]
                        },
                        'singular': 'compass',
                        'typeId': '1'
                    }
                }
            ]
        }
    }
}
