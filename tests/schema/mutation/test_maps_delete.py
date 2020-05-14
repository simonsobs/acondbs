import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
        mutation m {
          deleteMap(productId: 1001) { ok }
        }
         ''',
        '''
          {
            allMaps {
              edges {
                node {
                  productId
                  name
                }
              }
            }
            allMapFilePaths {
              edges {
                node {
                  path
                  productId
                }
              }
            }
          }
        ''',
        id='deleteMap'
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
          deleteMap(productId: 512) { ok }
        }
         ''',
        '''
          {
            allMaps {
              edges {
                node {
                  productId
                  name
                }
              }
            }
            allMapFilePaths {
              edges {
                node {
                  path
                  productId
                }
              }
            }
          }
        ''',
        id='deleteMap-error'
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
