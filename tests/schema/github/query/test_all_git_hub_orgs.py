from typing import Any, Mapping

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

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

HEADERS = {'Authorization': 'Bearer token1'}  # user1


params = [
    pytest.param(
        {'query': ALL_GITHUB_ORGS},
        id='one',
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
