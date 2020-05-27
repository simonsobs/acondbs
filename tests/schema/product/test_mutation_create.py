import pytest

from ..funcs import assert_mutation

from ..gql import CREATE_PRODUCT

QEURY = '''
{
  allProducts {
    edges {
      node {
        productId
      }
    }
  }
  allProductRelations {
    edges {
      node {
        relationId
      }
    }
  }
  allProductFilePaths {
    edges {
      node {
        pathId
      }
    }
  }
}
'''


# __________________________________________________________________||
params = [
    pytest.param(
        [
            [CREATE_PRODUCT],
            {'variables': {
                'input': {
                    'typeId': 1,
                    'name': "product1",
                    'contact': "contact-person",
                    'dateProduced': "2020-02-20",
                    'producedBy': "producer",
                    'postedBy': "poster",
                    'note': "- Item 1",
                    'paths': [
                        "/path/to/new/product1",
                        "/another/location/of/product1"
                    ]
                }
            }},
        ],
        [[QEURY], {}],
        id='create'
    ),
    pytest.param(
        [
            [CREATE_PRODUCT],
            {'variables': {
                'input': {
                    'typeId': 1,
                    'name': "product1",
                }
            }},
        ],
        [[QEURY], {}],
        id='minimum'
    ),
    pytest.param(
        [
            [CREATE_PRODUCT],
            {'variables': {
                'input': {
                    'typeId': 2,
                    'name': "lat20190213",
                    'contact': "contact-person",
                    'producedBy': "pwg-pmn",
                    'paths': [
                        "/path/to/new/product1",
                        "/another/location/of/product1"
                    ]
                }
            }},
        ],
        [[QEURY], {}],
        id='the-same-name-different-type'
    ),
]

@ pytest.mark.parametrize('mutation, query', params)
def test_schema_success(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation(app, snapshot, mutation, query,
                    mock_request_backup_db, success=True)

# __________________________________________________________________||
params = [
    pytest.param(
        [
            [CREATE_PRODUCT],
            {'variables': {
                'input': {
                    'typeId': 1,
                    'contact': "contact-person",
                    'dateProduced': "2020-02-20",
                    'producedBy': "producer",
                    'postedBy': "poster",
                    'note': "- Item 1",
                    'paths': [
                        "/path/to/new/product1",
                        "/another/location/of/product1"
                    ]
                }
            }},
        ],
        [[QEURY], {}],
        id='error-no-name'
    ),
    pytest.param(
        [
            [CREATE_PRODUCT],
            {'variables': {
                'input': {
                    'typeId': 1,
                    'name': "lat20190213",
                    'contact': "contact-person",
                    'producedBy': "pwg-pmn",
                    'paths': [
                        "/path/to/new/product1",
                        "/another/location/of/product1"
                    ]
                }
            }},
        ],
        [[QEURY], {}],
        id='error-the-same-type-and-name'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation(app, snapshot, mutation, query,
                    mock_request_backup_db, success=False)

# __________________________________________________________________||
