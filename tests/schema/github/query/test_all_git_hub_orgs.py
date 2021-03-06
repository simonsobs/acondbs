import pytest

from ...funcs import assert_query

ALL_GITHUB_ORGS = '''
{
  allGitHubOrgs {
    totalCount
    edges {
      node {
        login
        memberships {
          totalCount
          edges {
            node {
              member {
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
        [ALL_GITHUB_ORGS, ],
        {},
        id='one'
    ),
]

# __________________________________________________________________||
@pytest.mark.parametrize('args, kwags', params)
def test_schema(app, snapshot, args, kwags):
    assert_query(app, snapshot, [args, kwags])

# __________________________________________________________________||
