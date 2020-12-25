import textwrap
from graphene.test import Client

import pytest
import unittest.mock as mock

from acondbs.schema import create_schema

##__________________________________________________________________||
@pytest.fixture(autouse=True)
def mock_get_token(monkeypatch):
    y = mock.Mock()
    monkeypatch.setattr("acondbs.schema.github.auth.get_token", y)
    yield y

@pytest.fixture(autouse=True)
def mock_is_member(monkeypatch):
    y = mock.Mock()
    monkeypatch.setattr("acondbs.schema.github.auth.is_member", y)
    y.return_value = True
    yield y

##__________________________________________________________________||
def test_auth(app, mock_get_token, mock_is_member, snapshot):

    query = textwrap.dedent('''
        mutation AuthenticateWithGitHub($code: String!) {
          authenticateWithGitHub(code: $code) {
            authPayload {
              token
            }
          }
        }
    '''[1:])

    variables = { 'code': 'xyz' }

    mock_get_token.return_value = 'user_token_xyz'

    expected = {
        'authenticateWithGitHub': {
            'authPayload': {
                'token': 'user_token_xyz'
            }
        }
    }

    with app.app_context():
        schema = create_schema()
        client = Client(schema)
        result = client.execute(query, variables=variables, context_value={})
        assert {'data': expected} == result
        snapshot.assert_match(mock_get_token.call_args_list)
        snapshot.assert_match(mock_is_member.call_args_list)

##__________________________________________________________________||