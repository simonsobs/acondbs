import pytest
import unittest.mock as mock

from ...funcs import assert_mutation

ADD_GIT_HUB_ADMIN_APP_TOKEN = '''
mutation AddGitHubAdminAppToken($code: String!) {
  addGitHubAdminAppToken(code: $code) {
    ok
  }
}
'''

ALL_GITHUB_ADMIN_APP_TOKENS = '''
{
  allGitHubAdminAppTokens {
    totalCount
    edges {
      node {
        tokenId
        tokenMasked
      }
    }
  }
}
'''

##__________________________________________________________________||
@pytest.fixture()
def mock_auth_requests_success(monkeypatch):
    y = mock.Mock()
    monkeypatch.setattr("acondbs.github.auth.requests", y)
    response = {'access_token': 'token-xxx', 'token_type': 'bearer', 'scope': 'user'}
    r = mock.Mock()
    r.json.return_value = response
    y.post.return_value = r
    yield y

@pytest.fixture()
def mock_auth_requests_error(monkeypatch):
    y = mock.Mock()
    monkeypatch.setattr("acondbs.github.auth.requests", y)
    response = {
        'error': 'bad_verification_code',
        'error_description': 'The code passed is incorrect or expired.',
        'error_uri': 'https://docs.github.com/apps/managing-oauth-apps/troubleshooting-oauth-app-access-token-request-errors/#bad-verification-code'
    }
    r = mock.Mock()
    r.json.return_value = response
    y.post.return_value = r
    yield y

# __________________________________________________________________||
params = [
    pytest.param(
        [
            [ADD_GIT_HUB_ADMIN_APP_TOKEN],
            {'variables': {
                'code': 'code_01234'
            }},
        ],
        [[ALL_GITHUB_ADMIN_APP_TOKENS], {}],
        id='add'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_success(app, snapshot, mutation, query, mock_request_backup_db, mock_auth_requests_success):
    assert_mutation(app, snapshot, mutation, query,
                    mock_request_backup_db, success=True)
    snapshot.assert_match(mock_auth_requests_success.post.call_args_list)

# __________________________________________________________________||
params = [
    pytest.param(
        [
            [ADD_GIT_HUB_ADMIN_APP_TOKEN],
            {'variables': {
                'code': 'code_01234'
            }},
        ],
        [[ALL_GITHUB_ADMIN_APP_TOKENS], {}],
        id='add'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db, mock_auth_requests_error):
    assert_mutation(app, snapshot, mutation, query,
                    mock_request_backup_db, success=False)
    snapshot.assert_match(mock_auth_requests_error.post.call_args_list)

# __________________________________________________________________||