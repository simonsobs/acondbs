# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[createProductRelationType] 1'] = {
    'data': {
        'createProductRelationType': {
            'productRelationType': {
                'name': 'proctor'
            }
        }
    }
}

snapshots['test_schema_success[createProductRelationType] 2'] = {
    'data': {
        'productRelationType': {
            'indefArticle': 'a',
            'name': 'proctor',
            'plural': 'proctors',
            'singular': 'proctor'
        }
    }
}

snapshots['test_schema_error[createProduct-error-already-exist] 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 18,
                    'line': 5
                }
            ],
            'message': 'Cannot query field "productType" on type "CreateProductRelationType". Did you mean "productRelationType"?'
        }
    ]
}

snapshots['test_schema_error[createProduct-error-already-exist] 2'] = {
    'data': {
        'allProductRelationTypes': {
            'edges': [
                {
                    'node': {
                        'name': 'parent'
                    }
                },
                {
                    'node': {
                        'name': 'child'
                    }
                },
                {
                    'node': {
                        'name': 'plaintiff'
                    }
                },
                {
                    'node': {
                        'name': 'defendant'
                    }
                }
            ]
        }
    }
}
