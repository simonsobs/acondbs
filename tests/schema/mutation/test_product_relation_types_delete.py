import pytest

from .funcs import assert_mutation_success, assert_mutation_error

##__________________________________________________________________||
params = [
    pytest.param(
        '''
        mutation m {
          deleteProductRelationType(typeId: 3) { ok }
        }
         ''',
        '''
          {
            allProductRelationTypes {
              edges {
                node {
                  name
                  typeId
                }
              }
            }
          }
        ''',
        id='deleteProductRelationType'
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
          deleteProductRelationType(typeId: 512) { ok }
        }
         ''',
        '''
          {
            allProductRelationTypes {
              edges {
                node {
                  name
                  typeId
                }
              }
            }
          }
        ''',
        id='deleteProductRelationType-error-nonexistent'
    ),
    pytest.param(
        '''
        mutation m {
          deleteProductRelationType(typeId: 1) { ok }
        }
         ''',
        '''
          {
            allProductRelationTypes {
              edges {
                node {
                  name
                  typeId
                }
              }
            }
          }
        ''',
        id='deleteProductRelationType-error-unempty'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation_error(app, snapshot, mutation, query, mock_request_backup_db)

##__________________________________________________________________||
