import unittest.mock as mock

import pytest
from snapshottest.pytest import PyTestSnapshotTest

from acondbs.github.call import exchange_code_for_token


@pytest.fixture(autouse=True)
def mock_requests(monkeypatch: pytest.MonkeyPatch) -> mock.Mock:
    from acondbs.github import call

    y = mock.Mock()
    monkeypatch.setattr(call, 'requests', y)
    return y


def test_success(mock_requests: mock.Mock, snapshot: PyTestSnapshotTest) -> None:
    code = 'code-xyz'

    token_url = 'https://github.com/login/oauth/access_token'
    client_id = 'client_id_0123'
    client_secret = 'client_secret_0123'
    redirect_uri = 'http://localhost/auth'

    return_value = {
        'access_token': 'token-xxx',
        'token_type': 'bearer',
        'scope': 'user',
    }
    mock_requests.post().json.return_value = dict(return_value)

    response = exchange_code_for_token(
        code, token_url, client_id, client_secret, redirect_uri
    )

    assert return_value == response
    snapshot.assert_match(mock_requests.post.call_args_list)


def test_error(mock_requests: mock.Mock, snapshot: PyTestSnapshotTest) -> None:
    code = 'code-xyz'

    token_url = 'https://github.com/login/oauth/access_token'
    client_id = 'client_id_0123'
    client_secret = 'client_secret_0123'
    redirect_uri = 'http://localhost/auth'

    response = {
        'error': 'bad_verification_code',
        'error_description': 'The code passed is incorrect or expired.',
        'error_uri': 'https://docs.github.com/apps/managing-oauth-apps/troubleshooting-oauth-app-access-token-request-errors/#bad-verification-code',
    }
    mock_requests.post().json.return_value = response

    with pytest.raises(Exception) as e:
        exchange_code_for_token(code, token_url, client_id, client_secret, redirect_uri)

    assert response == e.value.args[0]

    snapshot.assert_match(mock_requests.post.call_args_list)
