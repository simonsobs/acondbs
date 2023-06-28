from typing import Any, Mapping
from unittest import mock

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from ...funcs import assert_mutation

ADD_GIT_HUB_ADMIN_APP_TOKEN = '''
mutation AddGitHubAdminAppToken($code: String!) {
  addGitHubAdminAppToken(code: $code) {
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

HEADERS = {'Authorization': 'Bearer token1'}  # user1


@pytest.fixture(autouse=True)
def mock_store_token_for_code(monkeypatch: pytest.MonkeyPatch) -> mock.Mock:
    from acondbs.schema.github import mutation

    y = mock.Mock()
    monkeypatch.setattr(mutation, 'store_token_for_code', y)
    return y


params = [
    pytest.param(
        {'query': ADD_GIT_HUB_ADMIN_APP_TOKEN, 'variables': {'code': 'code_01234'}},
        {'query': ALL_GITHUB_ADMIN_APP_TOKENS},
        id='one',
    ),
]


@pytest.mark.parametrize('data_mutation, data_query', params)
@pytest.mark.asyncio
async def test_schema_success(
    app: Flask,
    snapshot: PyTestSnapshotTest,
    data_mutation: Mapping[str, Any],
    data_query: Mapping[str, Any],
    mock_request_backup_db: mock.Mock,
    mock_store_token_for_code: mock.Mock,
) -> None:
    await assert_mutation(
        app,
        snapshot,
        data_mutation,
        HEADERS,
        data_query,
        HEADERS,
        mock_request_backup_db,
        success=True,
    )
    snapshot.assert_match(mock_store_token_for_code.call_args_list)


params = [
    pytest.param(
        {'query': ADD_GIT_HUB_ADMIN_APP_TOKEN, 'variables': {'code': 'code_01234'}},
        {'query': ALL_GITHUB_ADMIN_APP_TOKENS},
        id='one',
    ),
]


@pytest.mark.parametrize('data_mutation, data_query', params)
@pytest.mark.asyncio
async def test_schema_error(
    app: Flask,
    snapshot: PyTestSnapshotTest,
    data_mutation: Mapping[str, Any],
    data_query: Mapping[str, Any],
    mock_request_backup_db: mock.Mock,
    mock_store_token_for_code: mock.Mock,
) -> None:
    mock_store_token_for_code.side_effect = Exception('error')
    await assert_mutation(
        app,
        snapshot,
        data_mutation,
        HEADERS,
        data_query,
        HEADERS,
        mock_request_backup_db,
        success=False,
    )
    snapshot.assert_match(mock_store_token_for_code.call_args_list)
