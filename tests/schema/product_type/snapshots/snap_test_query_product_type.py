# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[productType-by-typeId-one] 1'] = {
    'data': {
        'productType': {
            'icon': 'mdi-map',
            'indefArticle': 'a',
            'name': 'map',
            'order': 2,
            'plural': 'maps',
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
            'singular': 'map',
            'typeId': '1'
        }
    }
}

snapshots['test_schema[productType-by-name-map] 1'] = {
    'data': {
        'productType': {
            'icon': 'mdi-map',
            'indefArticle': 'a',
            'name': 'map',
            'order': 2,
            'plural': 'maps',
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
            'singular': 'map',
            'typeId': '1'
        }
    }
}

snapshots['test_schema[productType-by-id-and-name-map] 1'] = {
    'data': {
        'productType': {
            'icon': 'mdi-map',
            'indefArticle': 'a',
            'name': 'map',
            'order': 2,
            'plural': 'maps',
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
            'singular': 'map',
            'typeId': '1'
        }
    }
}

snapshots['test_schema[productType-by-id-and-name-nonexistent] 1'] = {
    'data': {
        'productType': None
    }
}

snapshots['test_schema[productType-by-typeId-one-sort-products] 1'] = {
    'data': {
        'productType': {
            'icon': 'mdi-map',
            'indefArticle': 'a',
            'name': 'map',
            'order': 2,
            'plural': 'maps',
            'products': {
                'edges': [
                    {
                        'node': {
                            'name': 'lat20200201'
                        }
                    },
                    {
                        'node': {
                            'name': 'lat20200120'
                        }
                    },
                    {
                        'node': {
                            'name': 'lat20190213'
                        }
                    }
                ]
            },
            'singular': 'map',
            'typeId': '1'
        }
    }
}