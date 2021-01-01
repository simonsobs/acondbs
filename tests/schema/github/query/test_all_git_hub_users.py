import pytest

from ...funcs import assert_query

ALL_GITHUB_USERS = '''
{
  allGitHubUsers {
    totalCount
    edges {
      node {
        login
        name
        avatarUrl
        memberships {
          edges {
            node {
              org {
                login
              }
            }
          }
        }
      }
    }
  }
}
'''

# __________________________________________________________________||
params = [
    pytest.param(
        [ALL_GITHUB_USERS, ],
        {},
        id='one'
    ),
]

# __________________________________________________________________||
@pytest.mark.parametrize('args, kwags', params)
def test_schema(app, snapshot, args, kwags):
    assert_query(app, snapshot, [args, kwags])

# __________________________________________________________________||
