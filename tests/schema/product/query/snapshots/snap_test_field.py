# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[by-field-id] 1'] = {
    'data': {
        'field': {
            'fieldId': '1',
            'name': 'date_produced',
            'type_': 'DATE'
        }
    }
}

snapshots['test_schema[by-name] 1'] = {
    'data': {
        'field': {
            'fieldId': '2',
            'name': 'contact',
            'type_': 'UNICODE_TEXT'
        }
    }
}
