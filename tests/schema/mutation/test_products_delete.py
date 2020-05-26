import pytest

from .funcs import assert_mutation_success, assert_mutation_error

##__________________________________________________________________||
params = [
    pytest.param(
        '''
        mutation m {
          deleteProduct(productId: 1001) { ok }
        }
         ''',
        '''
          {
            allProducts {
              edges {
                node {
                  productId
                  name
                }
              }
            }
            allProductFilePaths {
              edges {
                node {
                  path
                  productId
                }
              }
            }
          }
        ''',
        id='deleteProduct'
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
          deleteProduct(productId: 512) { ok }
        }
         ''',
        '''
          {
            allProducts {
              edges {
                node {
                  productId
                  name
                }
              }
            }
            allProductFilePaths {
              edges {
                node {
                  path
                  productId
                }
              }
            }
          }
        ''',
        id='deleteProduct-error'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation_error(app, snapshot, mutation, query, mock_request_backup_db)

##__________________________________________________________________||
