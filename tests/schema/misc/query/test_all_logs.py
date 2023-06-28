from typing import Any

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from ...funcs import assert_query
from ..gql import QUERY_ALL_LOGS

HEADERS = {
    'Authorization': 'Bearer 90b2ee5fed25506df04fd37343bb68d1803dd97f'  # octocat
}


params = [
    pytest.param(
        {
            #
            'query': QUERY_ALL_LOGS
        },
        id='one',
    ),
]


@pytest.mark.parametrize('data', params)
@pytest.mark.asyncio
async def test_schema(app: Flask, snapshot: PyTestSnapshotTest, data: Any) -> None:
    await assert_query(app, snapshot, data, HEADERS)
