import pytest

from ..funcs import assert_mutation_success, assert_mutation_error

##__________________________________________________________________||
params = [
    pytest.param(
        '''
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
        ''',
        '''
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
        ''',
        id='createProduct'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_success(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation_success(app, snapshot, mutation, query, mock_request_backup_db)

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          mutation m {
            createProductType(input: {
              name: "map",
            }) { productType { name } }
          }
        ''',
        '''
          {
            allProductTypes {
              edges {
                node {
                  name
                }
              }
            }
          }
        ''',
        id='createProduct-error-already-exist'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation_error(app, snapshot, mutation, query, mock_request_backup_db)

##__________________________________________________________________||
