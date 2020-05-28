import pytest

from ..funcs import assert_mutation

##__________________________________________________________________||
params = [
    pytest.param(
        [
            ['''
              mutation m {
                createProductType(input: {
                  name: "compass",
                  order: 5,
                  indefArticle: "a",
                  singular: "compass",
                  plural: "compasses",
                  icon: "mdi-compass"
                }) { productType { name } }
              }
            '''],
            {},
        ],
        [
            ['''
              {
                productType(name: "compass") {
                  typeId
                  name
                  indefArticle
                  singular
                  plural
                  icon
                  products {
                    edges {
                      node {
                        name
                      }
                    }
                  }
                }
              }
            '''],
            {},
        ],
        id='create'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_success(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation(app, snapshot, mutation, query,
                    mock_request_backup_db, success=True)

##__________________________________________________________________||
params = [
    pytest.param(
        [
            ['''
              mutation m {
                createProductType(input: {
                  name: "map",
                }) { productType { name } }
              }
            '''],
            {}
        ],
        [
            ['''
              {
                allProductTypes {
                  edges {
                    node {
                      name
                    }
                  }
                }
              }
            ''',],
            {}
        ],
        id='error-already-exist'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation(app, snapshot, mutation, query,
                    mock_request_backup_db, success=False)

##__________________________________________________________________||
