import textwrap
from graphene.test import Client

import pytest
import unittest.mock as mock

from acondbs.schema import create_schema

##__________________________________________________________________||
@pytest.fixture(autouse=True)
def mock_exchange_code_for_token(monkeypatch):
    y = mock.Mock()
    monkeypatch.setattr("acondbs.schema.github.mutation.exchange_code_for_token", y)
    yield y

@pytest.fixture(autouse=True)
def mock_is_member(monkeypatch):
    y = mock.Mock()
    monkeypatch.setattr("acondbs.schema.github.mutation.is_member", y)
    y.return_value = True
    yield y

##__________________________________________________________________||
def test_auth(app, mock_exchange_code_for_token, mock_is_member, snapshot):

    query = textwrap.dedent('''
        mutation AuthenticateWithGitHub($code: String!) {
          authenticateWithGitHub(code: $code) {
            authPayload {
              token
            }
          }
        }
    '''[1:])

    variables = { 'code': 'h443xg9c' }

    return_value = {'access_token': 'jpdq74xt', 'token_type': 'bearer', 'scope': ''}
    mock_exchange_code_for_token.return_value = dict(return_value)

    expected = {
        'authenticateWithGitHub': {
            'authPayload': {
                'token': 'jpdq74xt'
            }
        }
    }

    with app.app_context():
        schema = create_schema()
        client = Client(schema)
        result = client.execute(query, variables=variables, context_value={})
        assert {'data': expected} == result
        assert [mock.call('h443xg9c')] == mock_exchange_code_for_token.call_args_list
        snapshot.assert_match(mock_is_member.call_args_list)

##__________________________________________________________________||
