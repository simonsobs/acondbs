import pytest

from ..funcs import assert_mutation_success, assert_mutation_error

##__________________________________________________________________||
params = [
    pytest.param(
        '''
        mutation m {
          deleteProductType(typeId: 4) { ok }
        }
         ''',
        '''
          {
            allProductTypes {
              edges {
                node {
                  name
                  typeId
                }
              }
            }
          }
        ''',
        id='deleteProductType'
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
          deleteProductType(typeId: 12) { ok }
        }
         ''',
        '''
          {
            allProductTypes {
              edges {
                node {
                  name
                  typeId
                }
              }
            }
          }
        ''',
        id='deleteProductType-error-nonexistent'
    ),
    pytest.param(
        '''
        mutation m {
          deleteProductType(typeId: 1) { ok }
        }
         ''',
        '''
          {
            allProductTypes {
              edges {
                node {
                  name
                  typeId
                }
              }
            }
          }
        ''',
        id='deleteProductType-error-unempty'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation_error(app, snapshot, mutation, query, mock_request_backup_db)

##__________________________________________________________________||
