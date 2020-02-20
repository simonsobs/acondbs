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
              datePosted: "2020-02-20",
              mapper: "pwg-pmn",
              note: "- Item 1"
            }) {
              map {
                name
                datePosted
                mapper
                note
              }
            }
          }
        ''',
        '''
        {
          map(name: "map325") {
            name
            datePosted
            mapper
            note
          }
        }
         ''',
        id='createMap'
    ),
    pytest.param(
        '''
        mutation m {
          updateMap(mapId: 1001, input: {name: "new-name"}) {
            map { mapId name } }
        }
         ''',
        '''
        { map(mapId: 1001) { mapId name } }
         ''',
        id='updateMap'
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
