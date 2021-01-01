# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[one] 1'] = {
    'data': {
        'allGitHubUsers': {
            'edges': [
                {
                    'node': {
                        'login': 'user1',
                        'memberships': {
                            'edges': [
                                {
                                    'node': {
                                        'org': {
                                            'login': 'org1'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'org': {
                                            'login': 'org2'
                                        }
                                    }
                                }
                            ]
                        }
                    }
                },
                {
                    'node': {
                        'login': 'user2',
                        'memberships': {
                            'edges': [
                                {
                                    'node': {
                                        'org': {
                                            'login': 'org2'
                                        }
                                    }
                                }
                            ]
                        }
                    }
                },
                {
                    'node': {
                        'login': 'user3',
                        'memberships': {
                            'edges': [
                            ]
                        }
                    }
                }
            ],
            'totalCount': 3
        }
    }
}
