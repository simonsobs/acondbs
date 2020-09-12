from graphene.test import Client
from graphene import Context
from werkzeug.datastructures import Headers

import pytest
import unittest.mock as mock

from acondbs.schema.schema import create_schema

##__________________________________________________________________||
@pytest.fixture(autouse=True)
def mock_githubauth(monkeypatch):
    y = mock.Mock()
    monkeypatch.setattr("acondbs.schema.query.githubauth", y)
    yield y


##__________________________________________________________________||
def test_auth(app, mock_githubauth):

    query = '{ githubUsername }'

    mock_githubauth.get_username.return_value = 'UserNameABC'

    expected = {
        'githubUsername': 'UserNameABC'
    }

    context = Context(headers=Headers({'Authorization': 'token token0123'}))

    with app.app_context():
        schema = create_schema()
        client = Client(schema)
        result = client.execute(query, context_value=context)
        assert {'data': expected} == result

##__________________________________________________________________||