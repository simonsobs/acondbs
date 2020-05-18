# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[allProductsFirstTwo] 1'] = {
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

snapshots['test_schema[allProductsFirstTwoSort] 1'] = {
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

snapshots['test_schema[productByProductID] 1'] = {
    'data': {
        'product': {
            'name': 'lat20190213'
        }
    }
}

snapshots['test_schema[productByProductID-nonexistent] 1'] = {
    'data': {
        'product': None
    }
}

snapshots['test_schema[productByName] 1'] = {
    'data': {
        'product': {
            'productId': '1001'
        }
    }
}
