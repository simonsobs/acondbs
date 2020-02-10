import acondbs
from acondbs.schema import schema

import pytest

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
    )

]

@pytest.mark.parametrize('query, expected', params)
def test_schema(app, query, expected):
    with app.app_context():
        result = schema.execute(query)
        assert result.errors is None
        assert expected == result.data

##__________________________________________________________________||
