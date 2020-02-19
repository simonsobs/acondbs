import pytest
from graphene.test import Client

import acondbs
from acondbs.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '{ version }',
        {'version': acondbs.__version__},
        id='version'
    ),
    pytest.param(
        '''
        { allMaps(first: 2) {
             edges { node { name } }
           } }
         ''',
        {'allMaps': {
            'edges': [
                {'node': {'name': 'lat20190213'}},
                {'node': {'name': 'lat20200120'}}
                ]
            }
        },
        id='allMapsFirstTwo'
    ),
    pytest.param(
        '''
        { allMaps(first: 2, sort: DATE_POSTED_DESC) {
             edges { node { name } }
           } }
         ''',
        {'allMaps': {
            'edges': [
                {'node': {'name': 'lat20200201'}},
                {'node': {'name': 'lat20200120'}}
                ]
            }
        },
        id='allMapsFirstTwoSort'
    ),
    pytest.param(
        '''
        { map(mapId: 1001) { name } }
         ''',
        {'map': { 'name': 'lat20190213' } },
        id='mapByMapID'
    ),
    pytest.param(
        '''
        { map(mapId: 2001) { name } }
         ''',
        {'map': None },
        id='mapByMapID-nonexistent'
    ),
    pytest.param(
        '''
        { map(name: "lat20190213") { mapId } }
         ''',
        {'map': { 'mapId': '1001' } },
        id='mapByName'
    ),
    pytest.param(
        '''
        { beam(beamId: 1010) { name } }
         ''',
        {'beam': { 'name': '20180101' } },
        id='beamByBeamID'
    ),
    pytest.param(
        '''
        { beam(beamId: 2001) { name } }
         ''',
        {'beam': None },
        id='beamByBeamID-nonexistent'
    ),
    pytest.param(
        '''
        { beam(name: "20180101") { beamId } }
         ''',
        {'beam': { 'beamId': '1010' } },
        id='beamByName'
    ),
]

@pytest.mark.parametrize('query, expected', params)
def test_schema(app, query, expected):
    with app.app_context():
        client = Client(schema)
        result = client.execute(query)
        assert {'data': expected} == result

##__________________________________________________________________||
