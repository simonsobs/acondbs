from typing import Any, Mapping

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from ...funcs import assert_query

QUERY = '{ isSignedIn }'


params = [
    pytest.param(
        {'query': QUERY},
        {'Authorization': 'Bearer 90b2ee5fed25506df04fd37343bb68d1803dd97f'},
        id='octocat',
    ),
    pytest.param(
        {'query': QUERY},
        {'Authorization': 'Bearer 0fb8c9e16d6f7c4961c4c49212bf197d79f14080'},
        id='dojocat',
    ),
    pytest.param(
        {'query': QUERY},
        {'Authorization': 'Bearer 1a2d18f270df3abacfb85c5413b668f97794b4ce'},
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
async def test_schema(
    app: Flask,
    snapshot: PyTestSnapshotTest,
    data: Mapping[str, Any],
    headers: Mapping[str, Any],
) -> None:
    await assert_query(app, snapshot, data, headers)
