# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[product-by-ProductID] 1'] = {
    'data': {
        'product': {
            'name': 'lat20190213'
        }
    }
}

snapshots['test_schema[product-by-ProductID-nonexistent] 1'] = {
    'data': {
        'product': None
    }
}

snapshots['test_schema[product-by-name] 1'] = {
    'data': {
        'product': {
            'productId': '1001'
        }
    }
}
