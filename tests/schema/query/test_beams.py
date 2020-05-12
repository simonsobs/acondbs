import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
        { beam(productId: 1010) { name } }
         ''',
        id='beamByBeamID'
    ),
    pytest.param(
        '''
        { beam(productId: 2001) { name } }
         ''',
        id='beamByBeamID-nonexistent'
    ),
    pytest.param(
        '''
        { beam(name: "20180101") { productId } }
         ''',
        id='beamByName'
    ),
]

@pytest.mark.parametrize('query', params)
def test_schema(app, snapshot, query):
    client = Client(schema)
    with app.app_context():
        snapshot.assert_match(client.execute(query))

##__________________________________________________________________||
