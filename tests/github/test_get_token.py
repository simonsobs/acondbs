import pytest
import unittest.mock as mock

from acondbs.github.auth import get_token

##__________________________________________________________________||
@pytest.fixture(autouse=True)
def mock_requests(monkeypatch):
    y = mock.Mock()
    monkeypatch.setattr("acondbs.github.auth.requests", y)
    yield y

##__________________________________________________________________||
def test_success(mock_requests, snapshot):

    code = 'code-xyz'

    token_url = 'https://github.com/login/oauth/access_token'
    client_id = 'client_id_0123'
    client_secret = 'client_secret_0123'
    redirect_uri = 'http://localhost/auth'

    r = {'access_token': 'token-xxx', 'token_type': 'bearer', 'scope': 'user'}
    mock_requests.post().json.return_value = r

    token = get_token(code, token_url, client_id, client_secret, redirect_uri)

    assert 'token-xxx' == token
    snapshot.assert_match(mock_requests.post.call_args_list)

##__________________________________________________________________||
def test_error(mock_requests, snapshot):

    code = 'code-xyz'

    token_url = 'https://github.com/login/oauth/access_token'
    client_id = 'client_id_0123'
    client_secret = 'client_secret_0123'
    redirect_uri = 'http://localhost/auth'

    response = {
        'error': 'bad_verification_code',
        'error_description': 'The code passed is incorrect or expired.',
        'error_uri': 'https://docs.github.com/apps/managing-oauth-apps/troubleshooting-oauth-app-access-token-request-errors/#bad-verification-code'
    }
    mock_requests.post().json.return_value = response

    with pytest.raises(Exception) as e:
        get_token(code, token_url, client_id, client_secret, redirect_uri)

    assert response == e.value.args[0]

    snapshot.assert_match(mock_requests.post.call_args_list)

##__________________________________________________________________||
