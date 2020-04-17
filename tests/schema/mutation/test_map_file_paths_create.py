import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          mutation m {
            createMapFilePath(input: {
              path: "nersc:/go/to/my/new_map_v1",
              note: "- Note 1",
              mapId: 1001
            }) { mapFilePath { path } }
          }
        ''',
        '''
          {
            map(mapId: 1001) {
              name datePosted mapper note
              beams { edges { node { name } } }
              mapFilePaths { edges { node { path note map { mapId } } } }
            }
          }
        ''',
        id='createMapFilePath'
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
