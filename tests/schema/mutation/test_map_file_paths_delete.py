import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          mutation m {
            deleteMapFilePath(mapFilePathId: 1) { ok }
          }
        ''',
        '''
          {
            map(mapId: 1001 ) {
              name datePosted mapper note
              beams { edges { node { name } } }
              mapFilePaths { edges { node { path note map { mapId } } } }
            }
          }
        ''',
        id='deleteMapFilePath'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema(app, snapshot, mutation, query):
    client = Client(schema)
    with app.app_context():
        snapshot.assert_match(client.execute(mutation))
    with app.app_context():
        snapshot.assert_match(client.execute(query))

##__________________________________________________________________||
