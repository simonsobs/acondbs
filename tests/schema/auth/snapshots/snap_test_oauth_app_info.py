# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[args0-kwags0] 1'] = {
    'data': {
        'oauthAppInfo': {
            'authorizeUrl': 'https://github.com/login/oauth/authorize',
            'clientId': '0123456789abcdefghij',
            'redirectUri': 'http://localhost:8080/signin',
            'tokenUrl': 'https://github.com/login/oauth/access_token'
        }
    }
}
