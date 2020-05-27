# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[query] 1'] = {
    'data': {
        'allProductRelationTypes': {
            'edges': [
                {
                    'node': {
                        'indefArticle': 'a',
                        'name': 'parent',
                        'plural': 'parents',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': 'lat20200120',
                                            'productId': '1012'
                                        },
                                        'self_': {
                                            'name': '20200123',
                                            'productId': '1130'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': 'lat20200201',
                                            'productId': '1013'
                                        },
                                        'self_': {
                                            'name': '20200207',
                                            'productId': '1150'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200123',
                                            'productId': '1130'
                                        },
                                        'self_': {
                                            'name': '20200207',
                                            'productId': '1150'
                                        }
                                    }
                                }
                            ]
                        },
                        'reverse': {
                            'name': 'child',
                            'typeId': '2'
                        },
                        'singular': 'parent',
                        'typeId': '1'
                    }
                },
                {
                    'node': {
                        'indefArticle': 'a',
                        'name': 'child',
                        'plural': 'children',
                        'relations': {
                            'edges': [
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200123',
                                            'productId': '1130'
                                        },
                                        'self_': {
                                            'name': 'lat20200120',
                                            'productId': '1012'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200207',
                                            'productId': '1150'
                                        },
                                        'self_': {
                                            'name': 'lat20200201',
                                            'productId': '1013'
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200207',
                                            'productId': '1150'
                                        },
                                        'self_': {
                                            'name': '20200123',
                                            'productId': '1130'
                                        }
                                    }
                                }
                            ]
                        },
                        'reverse': {
                            'name': 'parent',
                            'typeId': '1'
                        },
                        'singular': 'child',
                        'typeId': '2'
                    }
                },
                {
                    'node': {
                        'indefArticle': 'a',
                        'name': 'plaintiff',
                        'plural': 'plaintiffs',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'reverse': {
                            'name': 'defendant',
                            'typeId': '4'
                        },
                        'singular': 'plaintiff',
                        'typeId': '3'
                    }
                },
                {
                    'node': {
                        'indefArticle': 'a',
                        'name': 'defendant',
                        'plural': 'defendants',
                        'relations': {
                            'edges': [
                            ]
                        },
                        'reverse': {
                            'name': 'plaintiff',
                            'typeId': '3'
                        },
                        'singular': 'defendant',
                        'typeId': '4'
                    }
                }
            ]
        }
    }
}
