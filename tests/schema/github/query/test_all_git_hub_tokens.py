from typing import Any, Mapping

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

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

ALL_GITHUB_TOKENS = (
    '''
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
'''
    + GITHUB_TOKEN_FRAGMENT
)

ALL_GITHUB_TOKENS_WITH_ORG_ACCESS = (
    '''
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
'''
    + GITHUB_TOKEN_FRAGMENT
)

HEADERS = {'Authorization': 'Bearer token1'}  # user1


params = [
    pytest.param(
        {'query': ALL_GITHUB_TOKENS},
        id='simple',
    ),
    pytest.param(
        {'query': ALL_GITHUB_TOKENS_WITH_ORG_ACCESS},
        id='filter',
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
