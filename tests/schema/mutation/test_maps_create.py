import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          mutation m {
            createMap(input: {
              name: "map1",
              dateProduced: "2020-02-20",
              producedBy: "pwg-pmn",
              note: "- Item 1"
            }) { map { name } }
          }
        ''',
        '''
          {
            map(name: "map1") {
              name dateProduced producedBy note
              beams { edges { node { name } } }
              mapFilePaths { edges { node { path } } }
            }
          }
        ''',
        id='createMap-all-options'
    ),
    pytest.param(
        '''
          mutation m {
            createMap(input: {
              name: "map1",
              producedBy: "pwg-pmn"
            }) { map { name } }
          }
        ''',
        '''
          {
            map(name: "map1") {
              name dateProduced producedBy note
              beams { edges { node { name } } }
              mapFilePaths { edges { node { path } } }
            }
          }
        ''',
        id='createMap-selective-options'
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
            createMap(input: {
              producedBy: "pwg-pmn"
            }) { map { name } }
          }
        ''',
        '''
          {
            map(name: "map1") {
              name dateProduced producedBy note
              beams { edges { node { name } } }
              mapFilePaths { edges { node { path } } }
            }
          }
        ''',
        id='createMap-error-no-name'
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
