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
  allGitHubTokens {
    totalCount
    edges {
      node {
        tokenId
        tokenMasked
        scope
      }
    }
  }
}
'''

##__________________________________________________________________||
@pytest.fixture(autouse=True)
def mock_store_token_for_code(monkeypatch):
    y = mock.Mock()
    monkeypatch.setattr("acondbs.schema.github.mutation.store_token_for_code", y)
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
        {
            "login": "user1",
            "name": "User One",
            "avatarUrl": "https://avatars0.githubusercontent.com/u/user1"
        },
        id='one'
    ),
]

@pytest.mark.parametrize('mutation, query, viewer', params)
def test_schema_success(app, snapshot, mutation, query, viewer, mock_request_backup_db, mock_store_token_for_code):
    assert_mutation(app, snapshot, mutation, query,
                    mock_request_backup_db, success=True)
    snapshot.assert_match(mock_store_token_for_code.call_args_list)

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
        id='one'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db, mock_store_token_for_code):
    mock_store_token_for_code.side_effect = Exception("error")
    assert_mutation(app, snapshot, mutation, query,
                    mock_request_backup_db, success=False)
    snapshot.assert_match(mock_store_token_for_code.call_args_list)

# __________________________________________________________________||
