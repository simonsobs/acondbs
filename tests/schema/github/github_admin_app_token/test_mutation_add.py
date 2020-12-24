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
@pytest.fixture(autouse=True)
def mock_get_token(monkeypatch):
    y = mock.Mock()
    monkeypatch.setattr("acondbs.schema.github.github_admin_app_token.get_token", y)
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
def test_schema_success(app, snapshot, mutation, query, mock_request_backup_db, mock_get_token):
    mock_get_token.return_value = 'token_0123'

    assert_mutation(app, snapshot, mutation, query,
                    mock_request_backup_db, success=True)

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
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db, mock_get_token):
    mock_get_token.return_value = None

    assert_mutation(app, snapshot, mutation, query,
                    mock_request_backup_db, success=False)

# __________________________________________________________________||
