from typing import Any, Mapping

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from ...funcs import assert_query

QUERY = '{ gitHubViewer { login name avatarUrl } }'


params = [
    pytest.param(
        {'query': QUERY},
        {'Authorization': 'Bearer token1'},
        id='one',
    ),
]


@pytest.mark.parametrize('data, headers', params)
@pytest.mark.asyncio
async def test_success(
    app: Flask,
    snapshot: PyTestSnapshotTest,
    data: Mapping[str, Any],
    headers: Mapping[str, Any],
) -> None:
    await assert_query(app, snapshot, data, headers)


params = [
    pytest.param(
        {'query': QUERY},
        {'Authorization': 'Bearer no-such-token'},
        id='wrong-token',
    ),
    pytest.param(
        {'query': QUERY},
        {},
        id='no-token',
    ),
]


@pytest.mark.parametrize('data, headers', params)
@pytest.mark.asyncio
async def test_error(
    app: Flask,
    snapshot: PyTestSnapshotTest,
    data: Mapping[str, Any],
    headers: Mapping[str, Any],
) -> None:
    await assert_query(app, snapshot, data, headers, error=True)
