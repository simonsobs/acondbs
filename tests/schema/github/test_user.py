from graphene.test import Client
from graphene import Context
from werkzeug.datastructures import Headers

import pytest
import unittest.mock as mock

from acondbs.schema import create_schema

##__________________________________________________________________||
@pytest.fixture(autouse=True)
def mock_get_user(monkeypatch):
    y = mock.Mock()
    monkeypatch.setattr("acondbs.schema.github.auth.get_user", y)
    yield y


##__________________________________________________________________||
def test_auth(app, mock_get_user):

    query = '{ githubUser { login name avatarUrl } }'

    viewer = {
        "login": "octocat",
        "name": "monalisa octocat",
        "avatarUrl": "https://github.com/images/error/octocat_happy.gif"
    }
    mock_get_user.return_value = viewer

    expected = {
        'githubUser': viewer
    }

    context = Context(headers=Headers({'Authorization': 'Bearer "token0123"'}))

    with app.app_context():
        schema = create_schema()
        client = Client(schema)
        result = client.execute(query, context_value=context)
        assert [mock.call('token0123')] == mock_get_user.call_args_list
        assert {'data': expected} == result

##__________________________________________________________________||