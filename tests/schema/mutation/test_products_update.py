import pytest

from .funcs import assert_mutation_success, assert_mutation_error

##__________________________________________________________________||
params = [
    pytest.param(
        '''
        mutation m {
          updateProduct(productId: 1001, input: {
              contact: "new-contact",
              updatedBy: "updater",
              note: "- updated note 123"
          }) {
            product { productId name } }
        }
         ''',
        '''
          {
            product(productId: 1001) {
              name contact
              datePosted postedBy
              dateProduced producedBy
              dateUpdated updatedBy
              note
              paths { edges { node { path } } }
            }
          }
        ''',
        id='updateProduct'
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
          updateProduct(productId: 1010, input: {
              name: "new-name"
          }) {
            product { productId name } }
        }
         ''',
        '''
          {
            product(productId: 1010) {
              name contact
              datePosted postedBy
              dateProduced producedBy
              dateUpdated updatedBy
              note
              paths { edges { node { path } } }
            }
          }
        ''',
        id='updateProduct-error-immutable-fields'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation_error(app, snapshot, mutation, query, mock_request_backup_db)

##__________________________________________________________________||
