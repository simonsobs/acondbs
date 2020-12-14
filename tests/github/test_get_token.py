
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
def test_success(app, mock_requests):

    code = 'code-xyz'

    r = {'access_token': 'token-xxx', 'token_type': 'bearer', 'scope': 'user'}
    mock_requests.post().json.return_value = r
    with app.app_context():
        token = get_token(code)

    assert 'token-xxx' == token

##__________________________________________________________________||
def test_error(app, mock_requests):

    code = 'code-xyz'

    r = {
        'error': 'bad_verification_code',
        'error_description': 'The code passed is incorrect or expired.',
        'error_uri': 'https://docs.github.com/apps/managing-oauth-apps/troubleshooting-oauth-app-access-token-request-errors/#bad-verification-code'
    }
    mock_requests.post().json.return_value = r
    with app.app_context():
        token = get_token(code)

    assert token is None

##__________________________________________________________________||
