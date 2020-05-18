import pytest
import unittest.mock as mock

from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          mutation m {
            createProductType(input: {
              name: "compass",
            }) { productType { name } }
          }
        ''',
        '''
          {
            productType(name: "compass") {
              name
            }
          }
        ''',
        id='createProduct'
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
