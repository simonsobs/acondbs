from typing import Mapping

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from ...funcs import assert_query
from ..gql import QUERY_WEB_CONFIG

params = [
    pytest.param(
        {'query': QUERY_WEB_CONFIG},
        id='query',
    ),
]


@pytest.mark.parametrize("data", params)
@pytest.mark.asyncio
async def test_schema(
    app: Flask, snapshot: PyTestSnapshotTest, data: Mapping[str, str]
) -> None:
    await assert_query(app, snapshot, data)
