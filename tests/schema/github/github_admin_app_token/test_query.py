import pytest

from ...funcs import assert_query

ALL_GITHUB_ADMIN_APP_TOKENS = '''
{
  allGitHubAdminAppTokens {
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

# __________________________________________________________________||
params = [
    pytest.param(
        [ALL_GITHUB_ADMIN_APP_TOKENS, ],
        {},
        id='simple'
    ),
]

# __________________________________________________________________||
@pytest.mark.parametrize('args, kwags', params)
def test_schema(app, snapshot, args, kwags):
    assert_query(app, snapshot, [args, kwags])

# __________________________________________________________________||
