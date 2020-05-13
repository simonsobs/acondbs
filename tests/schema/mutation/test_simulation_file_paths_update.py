import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          mutation m {
            updateSimulationFilePath(pathId: 1, input: {
              path: "nersc:/go/to/my/new_simulation_v2",
              note: "- Note 1 updated",
            }) { simulationFilePath { path } }
          }
        ''',
        '''
          {
            simulation(productId: 1001) {
              name datePosted producedBy note
              paths { edges { node { path note product { productId } } } }
            }
          }
        ''',
        id='updateSimulationFilePath'
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
            updateSimulationFilePath(pathId: 1, input: {
              productId: 1002
            }) { simulationFilePath { path } }
          }
        ''',
        '''
          {
            simulation(productId: 1001) {
              paths { edges { node { path note product { productId } } } }
            }
          }
        ''',
        id='updateSimulationFilePath-immutableField'
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
