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
                        'productTypeId': '1',
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
                        }
                    }
                },
                {
                    'node': {
                        'name': 'beam',
                        'productTypeId': '2',
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
                        }
                    }
                },
                {
                    'node': {
                        'name': 'simulation',
                        'productTypeId': '3',
                        'products': {
                            'edges': [
                                {
                                    'node': {
                                        'name': 'xyz-s1234-20200101'
                                    }
                                }
                            ]
                        }
                    }
                },
                {
                    'node': {
                        'name': 'anchor',
                        'productTypeId': '4',
                        'products': {
                            'edges': [
                            ]
                        }
                    }
                }
            ]
        }
    }
}

snapshots['test_schema[productType-by-productTypeId-one)] 1'] = {
    'data': {
        'productType': {
            'name': 'map'
        }
    }
}
