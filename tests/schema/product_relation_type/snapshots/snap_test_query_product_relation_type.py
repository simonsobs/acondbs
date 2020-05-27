# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[type_id] 1'] = {
    'data': {
        'productRelationType': {
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
    }
}

snapshots['test_schema[name] 1'] = {
    'data': {
        'productRelationType': {
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
    }
}

snapshots['test_schema[type_id-and-name] 1'] = {
    'data': {
        'productRelationType': {
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
    }
}

snapshots['test_schema[type_id-and-name-nonexistent)] 1'] = {
    'data': {
        'productRelationType': None
    }
}
