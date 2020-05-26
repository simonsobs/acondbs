import pytest
import unittest.mock as mock

from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          mutation m {
            createProductRelationType(input: {
              name: "proctor",
              indefArticle: "a",
              singular: "proctor",
              plural: "proctors",
            }) { productRelationType { name } }
          }
        ''',
        '''
          {
            productRelationType(name: "proctor") {
              name
              indefArticle
              singular
              plural
            }
          }
        ''',
        id='createProductRelationType'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_success(app, snapshot, mutation, query, mock_request_backup_db):
    client = Client(schema)
    with app.app_context():
        result = client.execute(mutation, context_value={})
        assert 'errors' not in result
        snapshot.assert_match(result)
    with app.app_context():
        result = client.execute(query, context_value={})
        assert 'errors' not in result
        snapshot.assert_match(result)
    assert 1 == mock_request_backup_db.call_count

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          mutation m {
            createProductRelationType(input: {
              name: "parent",
            }) { productType { name } }
          }
        ''',
        '''
          {
            allProductRelationTypes {
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
        result = client.execute(mutation, context_value={})
        assert 'errors' in result
        snapshot.assert_match(result)
    with app.app_context():
        result = client.execute(query, context_value={})
        assert 'errors' not in result
        snapshot.assert_match(result)
    assert 0 == mock_request_backup_db.call_count

##__________________________________________________________________||
