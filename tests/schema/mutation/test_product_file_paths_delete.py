import pytest

from .funcs import assert_mutation_success, assert_mutation_error

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          mutation m {
            deleteProductFilePath(pathId: 1) { ok }
          }
        ''',
        '''
          {
            product(productId: 1001 ) {
              name datePosted producedBy note
              paths { edges { node { path note product { productId } } } }
            }
          }
        ''',
        id='deleteProductFilePath'
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
            deleteProductFilePath(pathId: 15) { ok }
          }
        ''',
        '''
          {
            allProductFilePaths {
              edges {
                node {
                  productId
                }
              }
            }
          }
        ''',
        id='deleteProductFilePath-error'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation_error(app, snapshot, mutation, query, mock_request_backup_db)

##__________________________________________________________________||
