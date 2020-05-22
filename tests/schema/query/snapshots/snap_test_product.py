# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[product_id] 1'] = {
    'data': {
        'product': {
            'name': 'lat20190213'
        }
    }
}

snapshots['test_schema[product_id-nonexistent] 1'] = {
    'data': {
        'product': None
    }
}

snapshots['test_schema[name] 1'] = {
    'data': {
        'product': {
            'productId': '1001'
        }
    }
}

snapshots['test_schema[product_id-name] 1'] = {
    'data': {
        'product': {
            'productId': '1001'
        }
    }
}

snapshots['test_schema[product_id-name-nonexistent] 1'] = {
    'data': {
        'product': None
    }
}

snapshots['test_schema[type_id-name] 1'] = {
    'data': {
        'product': {
            'productId': '1001'
        }
    }
}
