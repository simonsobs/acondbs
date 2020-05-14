import pytest
import unittest.mock as mock

from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          mutation m {
            createSimulation(input: {
              name: "simulation1",
              contact: "contact-person",
              dateProduced: "2020-02-20",
              producedBy: "producer",
              postedBy: "poster",
              note: "- Item 1"
              paths: [
                "/path/to/new/product1",
                "/another/location/of/product1"
              ]
            }) { simulation { name } }
          }
        ''',
        '''
          {
            simulation(name: "simulation1") {
              name contact
              datePosted postedBy
              dateProduced producedBy
              dateUpdated updatedBy
              note
              paths { edges { node { path } } }
            }
          }
        ''',
        id='createSimulation-all-options'
    ),
    pytest.param(
        '''
          mutation m {
            createSimulation(input: {
              name: "simulation1",
              producedBy: "pwg-pmn"
            }) { simulation { name } }
          }
        ''',
        '''
          {
            simulation(name: "simulation1") {
              name contact
              datePosted postedBy
              dateProduced producedBy
              dateUpdated updatedBy
              note
              paths { edges { node { path } } }
            }
          }
        ''',
        id='createSimulation-selective-options'
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
            createSimulation(input: {
              producedBy: "pwg-pmn"
              paths: [
                "/path/to/new/product1",
                "/another/location/of/product1"
              ]
            }) { simulation { name } }
          }
        ''',
        '''
          {
            allSimulations {
              edges {
                node {
                  productId
                  name
                }
              }
            }
            allSimulationFilePaths {
              edges {
                node {
                  path
                  productId
                }
              }
            }
          }
        ''',
        id='createSimulation-error-no-name'
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
