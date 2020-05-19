import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
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
        id='deleteProductRelationType'
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
#    pytest.param(
#        '''
#        mutation m {
#          deleteProductRelationType(typeId: 1) { ok }
#        }
#         ''',
#        '''
#          {
#            allProductRelationTypes {
#              edges {
#                node {
#                  name
#                  typeId
#                }
#              }
#            }
#          }
#        ''',
#        id='deleteProductRelationType-error-unempty'
#    ),
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
