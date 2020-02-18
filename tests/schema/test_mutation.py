import acondbs
from acondbs.schema import schema

import pytest

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
]

@pytest.mark.parametrize('mutation, expected1, query, expected2', params)
def test_schema(app, mutation, expected1, query, expected2):
    with app.app_context():
        result = schema.execute(mutation)
        assert result.errors is None
        assert expected1 == result.data
    with app.app_context():
        result = schema.execute(query)
        assert result.errors is None
        assert expected2 == result.data

##__________________________________________________________________||
