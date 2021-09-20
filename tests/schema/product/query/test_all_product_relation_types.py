import pytest

from ...funcs import assert_query

from ..gql import (
    QUERY_ALL_PRODUCT_RELATION_TYPES,
    QUERY_ALL_PRODUCT_RELATION_TYPES_TOTAL_COUNT,
)

HEADERS = {
    "Authorization": "Bearer 0fb8c9e16d6f7c4961c4c49212bf197d79f14080"  # dojocat
}


##__________________________________________________________________||
params = [
    pytest.param(
        {"query": QUERY_ALL_PRODUCT_RELATION_TYPES},
        id="query",
    ),
    pytest.param(
        {"query": QUERY_ALL_PRODUCT_RELATION_TYPES_TOTAL_COUNT},
        id="total-count",
    ),
]


##__________________________________________________________________||
@pytest.mark.parametrize("data", params)
@pytest.mark.asyncio
async def test_schema(app, snapshot, data):
    await assert_query(app, snapshot, data, HEADERS)


##__________________________________________________________________||
