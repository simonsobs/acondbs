import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
        { allMaps(first: 2) {
             edges { node { name } }
           } }
         ''',
        id='allMapsFirstTwo'
    ),
    pytest.param(
        '''
        { allMaps(first: 2, sort: DATE_POSTED_DESC) {
             edges { node { name } }
           } }
         ''',
        id='allMapsFirstTwoSort'
    ),
    pytest.param(
        '''
        { map(productId: 1001) { name } }
         ''',
        id='mapByMapID'
    ),
    pytest.param(
        '''
        { map(productId: 2001) { name } }
         ''',
        id='mapByMapID-nonexistent'
    ),
    pytest.param(
        '''
        { map(name: "lat20190213") { productId } }
         ''',
        id='mapByName'
    ),
]

@pytest.mark.parametrize('query', params)
def test_schema(app, snapshot, query):
    client = Client(schema)
    with app.app_context():
        result = client.execute(query)
        assert 'errors' not in result
        snapshot.assert_match(result)

##__________________________________________________________________||
