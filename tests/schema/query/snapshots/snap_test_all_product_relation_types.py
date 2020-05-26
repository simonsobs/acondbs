# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[allProductRelationTypes] 1'] = {
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
                                            'type_': {
                                                'name': 'map'
                                            }
                                        },
                                        'self_': {
                                            'name': '20200123',
                                            'type_': {
                                                'name': 'beam'
                                            }
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': 'lat20200201',
                                            'type_': {
                                                'name': 'map'
                                            }
                                        },
                                        'self_': {
                                            'name': '20200207',
                                            'type_': {
                                                'name': 'beam'
                                            }
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200123',
                                            'type_': {
                                                'name': 'beam'
                                            }
                                        },
                                        'self_': {
                                            'name': '20200207',
                                            'type_': {
                                                'name': 'beam'
                                            }
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
                                            'type_': {
                                                'name': 'beam'
                                            }
                                        },
                                        'self_': {
                                            'name': 'lat20200120',
                                            'type_': {
                                                'name': 'map'
                                            }
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200207',
                                            'type_': {
                                                'name': 'beam'
                                            }
                                        },
                                        'self_': {
                                            'name': 'lat20200201',
                                            'type_': {
                                                'name': 'map'
                                            }
                                        }
                                    }
                                },
                                {
                                    'node': {
                                        'other': {
                                            'name': '20200207',
                                            'type_': {
                                                'name': 'beam'
                                            }
                                        },
                                        'self_': {
                                            'name': '20200123',
                                            'type_': {
                                                'name': 'beam'
                                            }
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
