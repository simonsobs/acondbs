import pytest
import unittest.mock as mock

from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          mutation m {
            createBeam(input: {
              name: "beam1",
              contact: "contact-person",
              dateProduced: "2020-02-20",
              producedBy: "producer",
              postedBy: "poster",
              note: "- Item 1"
            }) { beam { name } }
          }
        ''',
        '''
          {
            beam(name: "beam1") {
              name contact
              datePosted postedBy
              dateProduced producedBy
              dateUpdated updatedBy
              note
              paths { edges { node { path } } }
            }
          }
        ''',
        id='createBeam-all-options'
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
            createBeam(input: {
              producedBy: "pwg-pmn"
            }) { beam { name } }
          }
        ''',
        '''
          {
            beam(name: "beam1") {
              name contact
              datePosted postedBy
              dateProduced producedBy
              dateUpdated updatedBy
              note
              paths { edges { node { path } } }
            }
          }
        ''',
        id='createBeam-error-no-name'
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
