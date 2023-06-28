from typing import Any, Mapping

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

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

ALL_GITHUB_USERS = (
    '''
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
'''
    + GITHUB_USER_FRAGMENT
)

ALL_GITHUB_USERS_WITH_FILTER = (
    '''
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
'''
    + GITHUB_USER_FRAGMENT
)

HEADERS = {'Authorization': 'Bearer token1'}  # user1


params = [
    pytest.param({'query': ALL_GITHUB_USERS}, id='one'),
    pytest.param(
        {'query': ALL_GITHUB_USERS_WITH_FILTER, 'variables': {'orgMember': True}},
        id='filter-on',
    ),
    pytest.param(
        {'query': ALL_GITHUB_USERS_WITH_FILTER, 'variables': {'orgMember': False}},
        id='filter-off',
    ),
]


@pytest.mark.parametrize('data', params)
@pytest.mark.asyncio
async def test_schema(
    app: Flask,
    snapshot: PyTestSnapshotTest,
    data: Mapping[str, Any],
) -> None:
    await assert_query(app, snapshot, data, HEADERS)
