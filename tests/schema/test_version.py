import pytest
from graphene.test import Client

import acondbs
from acondbs.schema import schema_admin

##__________________________________________________________________||
params = [
    pytest.param(
        '{ version }',
        {'version': acondbs.__version__},
        id='version'
    ),
]

@pytest.mark.parametrize('query, expected', params)
def test_schema(app, query, expected):
    with app.app_context():
        client = Client(schema_admin)
        result = client.execute(query, context_value={})
        assert {'data': expected} == result

##__________________________________________________________________||
