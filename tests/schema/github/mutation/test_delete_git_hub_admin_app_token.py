import pytest
import unittest.mock as mock

from ...funcs import assert_mutation

DELETE_GIT_HUB_ADMIN_APP_TOKEN = '''
mutation DeleteGitHubAdminAppToken($tokenId: Int!) {
  deleteGitHubAdminAppToken(tokenId: $tokenId) {
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
params = [
    pytest.param(
        [
            [DELETE_GIT_HUB_ADMIN_APP_TOKEN],
            {'variables': {
                'tokenId': 1
            }},
        ],
        [[ALL_GITHUB_ADMIN_APP_TOKENS], {}],
        id='delete'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_success(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation(app, snapshot, mutation, query,
                    mock_request_backup_db, success=True)

##__________________________________________________________________||
params = [
    pytest.param(
        [
            [DELETE_GIT_HUB_ADMIN_APP_TOKEN],
            {'variables': {
                'tokenId': 999
            }},
        ],
        [[ALL_GITHUB_ADMIN_APP_TOKENS], {}],
        id='delete'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation(app, snapshot, mutation, query,
                    mock_request_backup_db, success=False)

##__________________________________________________________________||
