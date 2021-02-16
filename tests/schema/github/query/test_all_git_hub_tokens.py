import pytest

from ...funcs import assert_query

GITHUB_TOKEN_FRAGMENT = '''
fragment GitHubTokenFragment on GitHubToken {
  tokenId
  tokenMasked
  scope
  timeCreated
  user {
    login
  }
}
'''

ALL_GITHUB_TOKENS = '''
{
  allGitHubTokens {
    totalCount
    edges {
      node {
        ...GitHubTokenFragment
      }
    }
  }
}
''' + GITHUB_TOKEN_FRAGMENT

ALL_GITHUB_TOKENS_WITH_ORG_ACCESS = '''
{
  allGitHubTokens(filters: { scopeIlike: "%read:org%" }) {
    totalCount
    edges {
      node {
        ...GitHubTokenFragment
      }
    }
  }
}
''' + GITHUB_TOKEN_FRAGMENT

##__________________________________________________________________||
params = [
    pytest.param(
        [ALL_GITHUB_TOKENS, ],
        {},
        id='simple'
    ),
    pytest.param(
        [ALL_GITHUB_TOKENS_WITH_ORG_ACCESS, ],
        {},
        id='filter'
    ),
]

##__________________________________________________________________||
@pytest.mark.parametrize('args, kwargs', params)
def test_schema(app, snapshot, args, kwargs):
    assert_query(app, snapshot, [args, kwargs])

##__________________________________________________________________||
