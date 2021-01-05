import pytest

from ...funcs import assert_query

GITHUB_USER_FRAGMENT = '''
fragment GitHubUserFragment on GitHubUser {
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
'''

ALL_GITHUB_USERS = '''
{
  allGitHubUsers {
    totalCount
    edges {
      node {
        ...GitHubUserFragment
      }
    }
  }
}
''' + GITHUB_USER_FRAGMENT

ALL_GITHUB_USERS_WITH_FILTER = '''
query AllGitHubUsers($orgMember: Boolean){
  allGitHubUsers(filters: { orgMember: $orgMember }) {
    totalCount
    edges {
      node {
        ...GitHubUserFragment
      }
    }
  }
}
''' + GITHUB_USER_FRAGMENT

# __________________________________________________________________||
params = [
    pytest.param(
        [ALL_GITHUB_USERS, ],
        {},
        id='one'
    ),
    pytest.param(
        [ALL_GITHUB_USERS_WITH_FILTER, ],
        {'variables': {'orgMember': True}},
        id='filter-on'
    ),
    pytest.param(
        [ALL_GITHUB_USERS_WITH_FILTER, ],
        {'variables': {'orgMember': False}},
        id='filter-off'
    ),
]

# __________________________________________________________________||
@pytest.mark.parametrize('args, kwags', params)
def test_schema(app, snapshot, args, kwags):
    assert_query(app, snapshot, [args, kwags])

# __________________________________________________________________||
