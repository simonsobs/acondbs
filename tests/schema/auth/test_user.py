import textwrap
from graphene.test import Client

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

    query = textwrap.dedent('''
        query GitHubUsername($token: String!) {
          githubUsername(token: $token)
        }
    '''[1:])

    variables = { 'token': 'token0123' }

    mock_githubauth.get_username.return_value = 'UserNameABC'

    expected = {
        'githubUsername': 'UserNameABC'
    }

    with app.app_context():
        schema = create_schema()
        client = Client(schema)
        result = client.execute(query, variables=variables, context_value={})
        assert {'data': expected} == result

##__________________________________________________________________||
