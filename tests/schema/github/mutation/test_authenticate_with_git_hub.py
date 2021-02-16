import textwrap
from graphene.test import Client

import pytest
import unittest.mock as mock

from acondbs.schema import schema_public

##__________________________________________________________________||
@pytest.fixture(autouse=True)
def mock_authenticate(monkeypatch):
    y = mock.Mock()
    monkeypatch.setattr("acondbs.schema.github.mutation.authenticate", y)
    yield y

##__________________________________________________________________||
def test_auth(app, mock_authenticate):

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
    mock_authenticate.return_value = dict(return_value)

    expected = {
        'authenticateWithGitHub': {
            'authPayload': {
                'token': 'jpdq74xt'
            }
        }
    }

    with app.app_context():
        client = Client(schema_public)
        result = client.execute(query, variables=variables, context_value={})
        assert {'data': expected} == result
        assert [mock.call('h443xg9c')] == mock_authenticate.call_args_list

##__________________________________________________________________||
