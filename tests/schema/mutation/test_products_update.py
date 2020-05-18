import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

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
    client = Client(schema)
    with app.app_context():
        result = client.execute(mutation)
        assert 'errors' not in result
        snapshot.assert_match(result)
    with app.app_context():
        result = client.execute(query)
        assert 'errors' not in result
        snapshot.assert_match(result)
    assert 1 == mock_request_backup_db.call_count

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
    client = Client(schema)
    with app.app_context():
        result = client.execute(mutation)
        assert 'errors' in result
        snapshot.assert_match(result)
    with app.app_context():
        result = client.execute(query)
        assert 'errors' not in result
        snapshot.assert_match(result)
    assert 0 == mock_request_backup_db.call_count

##__________________________________________________________________||
