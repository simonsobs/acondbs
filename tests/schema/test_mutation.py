import pytest
from graphene.test import Client

from acondbs.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
        mutation m {
          createMap(name: "map1") {
            map { name } }
        }
         ''',
        '''
        { map(name: "map1") { name } }
         ''',
        id='createMap'
    ),
    pytest.param(
        '''
        mutation m {
          updateMap(mapId: 1001, name: "new-name") {
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
