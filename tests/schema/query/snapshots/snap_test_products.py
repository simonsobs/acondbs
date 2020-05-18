# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[allProducts-first-two] 1'] = {
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

snapshots['test_schema[allProducts-first-two-sort] 1'] = {
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

snapshots['test_schema[allProducts] 1'] = {
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
                },
                {
                    'node': {
                        'name': '20180101'
                    }
                },
                {
                    'node': {
                        'name': 'lat20200120'
                    }
                },
                {
                    'node': {
                        'name': 'lat20200201'
                    }
                },
                {
                    'node': {
                        'name': '20190304'
                    }
                },
                {
                    'node': {
                        'name': '20190607'
                    }
                },
                {
                    'node': {
                        'name': '20200123'
                    }
                },
                {
                    'node': {
                        'name': '20200207'
                    }
                }
            ]
        }
    }
}

snapshots['test_schema[allProducts-filtes-productTypeId-one-first-two] 1'] = {
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
                        'name': 'lat20200120'
                    }
                }
            ]
        }
    }
}
