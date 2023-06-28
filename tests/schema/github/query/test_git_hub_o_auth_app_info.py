from typing import Any, Mapping

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from ...funcs import assert_query

GITHUB_OAUTH_APP_INFO = '''
{
  gitHubOAuthAppInfo {
    clientId
    authorizeUrl
    redirectUri
  }
}
'''


params = [
    pytest.param(
        {'query': GITHUB_OAUTH_APP_INFO},
        id='query',
    ),
]


@pytest.mark.parametrize("data", params)
@pytest.mark.asyncio
async def test_schema(
    app: Flask,
    snapshot: PyTestSnapshotTest,
    data: Mapping[str, Any],
) -> None:
    await assert_query(app, snapshot, data)
