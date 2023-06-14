import pytest

from ...funcs import assert_query
from ..gql import QUERY_WEB_CONFIG

params = [
    pytest.param(
        {"query": QUERY_WEB_CONFIG},
        id="query",
    ),
]


@pytest.mark.parametrize("data", params)
@pytest.mark.asyncio
async def test_schema(app, snapshot, data):
    await assert_query(app, snapshot, data)
