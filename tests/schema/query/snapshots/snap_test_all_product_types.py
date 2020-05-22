# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[allProductTypes] 1'] = {
    'data': {
        'allProductTypes': {
            'edges': [
                {
                    'node': {
                        'icon': 'mdi-creation',
                        'indefArticle': 'a',
                        'name': 'simulation',
                        'order': 1,
                        'plural': 'simulations',
                        'products': {
                            'edges': [
                                {
                                    'node': {
                                        'name': 'xyz-s1234-20200101'
                                    }
                                }
                            ]
                        },
                        'singular': 'simulation',
                        'typeId': '3'
                    }
                },
                {
                    'node': {
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
                },
                {
                    'node': {
                        'icon': 'mdi-spotlight-beam',
                        'indefArticle': 'a',
                        'name': 'beam',
                        'order': 3,
                        'plural': 'beams',
                        'products': {
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
                                },
                                {
                                    'node': {
                                        'name': '20190607'
                                    }
                                },
                                {
                                    'node': {
                                        'name': '20200123'
                                    }
                                },
                                {
                                    'node': {
                                        'name': '20200207'
                                    }
                                }
                            ]
                        },
                        'singular': 'beam',
                        'typeId': '2'
                    }
                },
                {
                    'node': {
                        'icon': '',
                        'indefArticle': '',
                        'name': 'anchor',
                        'order': 4,
                        'plural': '',
                        'products': {
                            'edges': [
                            ]
                        },
                        'singular': '',
                        'typeId': '4'
                    }
                }
            ]
        }
    }
}