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
                        'name': 'map',
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
                        'typeId': '1'
                    }
                },
                {
                    'node': {
                        'name': 'beam',
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
                        'typeId': '2'
                    }
                },
                {
                    'node': {
                        'name': 'simulation',
                        'products': {
                            'edges': [
                                {
                                    'node': {
                                        'name': 'xyz-s1234-20200101'
                                    }
                                }
                            ]
                        },
                        'typeId': '3'
                    }
                },
                {
                    'node': {
                        'name': 'anchor',
                        'products': {
                            'edges': [
                            ]
                        },
                        'typeId': '4'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema[productType-by-typeId-one)] 1'] = {
    'data': {
        'productType': {
            'name': 'map'
        }
    }
}
