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
        {'createMap': {'map': {'name': 'map1'}}},
        '''
        { map(name: "map1") { name } }
         ''',
        {'map': { 'name': 'map1' } },
        id='createMap'
    ),
    pytest.param(
        '''
        mutation m {
          updateMap(mapId: 1001, name: "new-name") {
            map { mapId name } }
        }
         ''',
        {'updateMap': {'map': {'mapId': '1001', 'name': 'new-name'}}},
        '''
        { map(mapId: 1001) { mapId name } }
         ''',
        {'map': {'mapId': '1001', 'name': 'new-name'} },
        id='updateMap'
    ),
]

@pytest.mark.parametrize('mutation, expected1, query, expected2', params)
def test_schema(app, mutation, expected1, query, expected2):
    with app.app_context():
        client = Client(schema)
        result = client.execute(mutation)
        assert {'data': expected1} == result
    with app.app_context():
        client = Client(schema)
        result = client.execute(query)
        assert {'data': expected2} == result

##__________________________________________________________________||
