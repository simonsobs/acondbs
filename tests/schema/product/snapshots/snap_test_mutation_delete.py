# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[delete] 1'] = {
    'data': {
        'deleteProduct': {
            'ok': True
        }
    }
}

snapshots['test_schema_success[delete] 2'] = {
    'data': {
        'allProductFilePaths': {
            'edges': [
                {
                    'node': {
                        'pathId': '2'
                    }
                },
                {
                    'node': {
                        'pathId': '3'
                    }
                },
                {
                    'node': {
                        'pathId': '4'
                    }
                },
                {
                    'node': {
                        'pathId': '5'
                    }
                },
                {
                    'node': {
                        'pathId': '6'
                    }
                },
                {
                    'node': {
                        'pathId': '7'
                    }
                },
                {
                    'node': {
                        'pathId': '8'
                    }
                },
                {
                    'node': {
                        'pathId': '9'
                    }
                },
                {
                    'node': {
                        'pathId': '10'
                    }
                }
            ]
        },
        'allProductRelations': {
            'edges': [
                {
                    'node': {
                        'relationId': '1'
                    }
                },
                {
                    'node': {
                        'relationId': '2'
                    }
                },
                {
                    'node': {
                        'relationId': '3'
                    }
                },
                {
                    'node': {
                        'relationId': '4'
                    }
                },
                {
                    'node': {
                        'relationId': '5'
                    }
                },
                {
                    'node': {
                        'relationId': '6'
                    }
                }
            ]
        },
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'productId': '1002'
                    }
                },
                {
                    'node': {
                        'productId': '1010'
                    }
                },
                {
                    'node': {
                        'productId': '1012'
                    }
                },
                {
                    'node': {
                        'productId': '1013'
                    }
                },
                {
                    'node': {
                        'productId': '1070'
                    }
                },
                {
                    'node': {
                        'productId': '1120'
                    }
                },
                {
                    'node': {
                        'productId': '1130'
                    }
                },
                {
                    'node': {
                        'productId': '1150'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema_error[error] 1'] = {
    'data': {
        'deleteProduct': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 3,
                    'line': 3
                }
            ],
            'message': "Class 'builtins.NoneType' is not mapped",
            'path': [
                'deleteProduct'
            ]
        }
    ]
}

snapshots['test_schema_error[error] 2'] = {
    'data': {
        'allProductFilePaths': {
            'edges': [
                {
                    'node': {
                        'pathId': '1'
                    }
                },
                {
                    'node': {
                        'pathId': '2'
                    }
                },
                {
                    'node': {
                        'pathId': '3'
                    }
                },
                {
                    'node': {
                        'pathId': '4'
                    }
                },
                {
                    'node': {
                        'pathId': '5'
                    }
                },
                {
                    'node': {
                        'pathId': '6'
                    }
                },
                {
                    'node': {
                        'pathId': '7'
                    }
                },
                {
                    'node': {
                        'pathId': '8'
                    }
                },
                {
                    'node': {
                        'pathId': '9'
                    }
                },
                {
                    'node': {
                        'pathId': '10'
                    }
                }
            ]
        },
        'allProductRelations': {
            'edges': [
                {
                    'node': {
                        'relationId': '1'
                    }
                },
                {
                    'node': {
                        'relationId': '2'
                    }
                },
                {
                    'node': {
                        'relationId': '3'
                    }
                },
                {
                    'node': {
                        'relationId': '4'
                    }
                },
                {
                    'node': {
                        'relationId': '5'
                    }
                },
                {
                    'node': {
                        'relationId': '6'
                    }
                }
            ]
        },
        'allProducts': {
            'edges': [
                {
                    'node': {
                        'productId': '1001'
                    }
                },
                {
                    'node': {
                        'productId': '1002'
                    }
                },
                {
                    'node': {
                        'productId': '1010'
                    }
                },
                {
                    'node': {
                        'productId': '1012'
                    }
                },
                {
                    'node': {
                        'productId': '1013'
                    }
                },
                {
                    'node': {
                        'productId': '1070'
                    }
                },
                {
                    'node': {
                        'productId': '1120'
                    }
                },
                {
                    'node': {
                        'productId': '1130'
                    }
                },
                {
                    'node': {
                        'productId': '1150'
                    }
                }
            ]
        }
    }
}
