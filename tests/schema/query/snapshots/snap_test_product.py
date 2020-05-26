# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema[product_id] 1'] = {
    'data': {
        'product': {
            'contact': 'pwg-pmn',
            'datePosted': '2019-02-13',
            'dateProduced': '2019-02-13',
            'dateUpdated': '2019-02-13',
            'name': 'lat20190213',
            'note': '''- This is a dummy test with a lat map
- This should not depend on any beam''',
            'paths': {
                'edges': [
                    {
                        'node': {
                            'note': '',
                            'path': 'nersc:/go/to/my/maps',
                            'pathId': '1'
                        }
                    }
                ]
            },
            'postedBy': 'pwg-pmn',
            'producedBy': 'pwg-pmn',
            'productId': '1001',
            'relations': {
                'edges': [
                ]
            },
            'typeId': 1,
            'type_': {
                'name': 'map',
                'typeId': '1'
            },
            'updatedBy': 'pwg-pmn'
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
            'contact': 'pwg-pmn',
            'datePosted': '2019-02-13',
            'dateProduced': '2019-02-13',
            'dateUpdated': '2019-02-13',
            'name': 'lat20190213',
            'note': '''- This is a dummy test with a lat map
- This should not depend on any beam''',
            'paths': {
                'edges': [
                    {
                        'node': {
                            'note': '',
                            'path': 'nersc:/go/to/my/maps',
                            'pathId': '1'
                        }
                    }
                ]
            },
            'postedBy': 'pwg-pmn',
            'producedBy': 'pwg-pmn',
            'productId': '1001',
            'relations': {
                'edges': [
                ]
            },
            'typeId': 1,
            'type_': {
                'name': 'map',
                'typeId': '1'
            },
            'updatedBy': 'pwg-pmn'
        }
    }
}

snapshots['test_schema[product_id-name] 1'] = {
    'data': {
        'product': {
            'contact': 'pwg-pmn',
            'datePosted': '2019-02-13',
            'dateProduced': '2019-02-13',
            'dateUpdated': '2019-02-13',
            'name': 'lat20190213',
            'note': '''- This is a dummy test with a lat map
- This should not depend on any beam''',
            'paths': {
                'edges': [
                    {
                        'node': {
                            'note': '',
                            'path': 'nersc:/go/to/my/maps',
                            'pathId': '1'
                        }
                    }
                ]
            },
            'postedBy': 'pwg-pmn',
            'producedBy': 'pwg-pmn',
            'productId': '1001',
            'relations': {
                'edges': [
                ]
            },
            'typeId': 1,
            'type_': {
                'name': 'map',
                'typeId': '1'
            },
            'updatedBy': 'pwg-pmn'
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
            'contact': 'pwg-pmn',
            'datePosted': '2019-02-13',
            'dateProduced': '2019-02-13',
            'dateUpdated': '2019-02-13',
            'name': 'lat20190213',
            'note': '''- This is a dummy test with a lat map
- This should not depend on any beam''',
            'paths': {
                'edges': [
                    {
                        'node': {
                            'note': '',
                            'path': 'nersc:/go/to/my/maps',
                            'pathId': '1'
                        }
                    }
                ]
            },
            'postedBy': 'pwg-pmn',
            'producedBy': 'pwg-pmn',
            'productId': '1001',
            'relations': {
                'edges': [
                ]
            },
            'typeId': 1,
            'type_': {
                'name': 'map',
                'typeId': '1'
            },
            'updatedBy': 'pwg-pmn'
        }
    }
}
