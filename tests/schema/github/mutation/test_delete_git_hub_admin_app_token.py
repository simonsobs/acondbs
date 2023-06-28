from typing import Any, Mapping
from unittest import mock

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

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


params = [
    pytest.param(
        {'query': DELETE_GIT_HUB_ADMIN_APP_TOKEN, 'variables': {'tokenId': 1}},
        {'Authorization': 'Bearer token1'},
        {'query': ALL_GITHUB_ADMIN_APP_TOKENS},
        {'Authorization': 'Bearer token4'},
        id='delete',
    ),
]


@pytest.mark.parametrize(
    'data_mutation, headers_mutation, data_query, headers_query', params
)
@pytest.mark.asyncio
async def test_schema_success(
    app: Flask,
    snapshot: PyTestSnapshotTest,
    data_mutation: Mapping[str, Any],
    headers_mutation: Mapping[str, Any],
    data_query: Mapping[str, Any],
    headers_query: Mapping[str, Any],
    mock_request_backup_db: mock.Mock,
) -> None:
    await assert_mutation(
        app,
        snapshot,
        data_mutation,
        headers_mutation,
        data_query,
        headers_query,
        mock_request_backup_db,
        success=True,
    )


params = [
    pytest.param(
        {'query': DELETE_GIT_HUB_ADMIN_APP_TOKEN, 'variables': {'tokenId': 999}},
        {'Authorization': 'Bearer token1'},
        {'query': ALL_GITHUB_ADMIN_APP_TOKENS},
        {'Authorization': 'Bearer token4'},
        id='delete',
    ),
]


@pytest.mark.parametrize(
    'data_mutation, headers_mutation, data_query, headers_query', params
)
@pytest.mark.asyncio
async def test_schema_error(
    app: Flask,
    snapshot: PyTestSnapshotTest,
    data_mutation: Mapping[str, Any],
    headers_mutation: Mapping[str, Any],
    data_query: Mapping[str, Any],
    headers_query: Mapping[str, Any],
    mock_request_backup_db: mock.Mock,
) -> None:
    await assert_mutation(
        app,
        snapshot,
        data_mutation,
        headers_mutation,
        data_query,
        headers_query,
        mock_request_backup_db,
        success=False,
    )
