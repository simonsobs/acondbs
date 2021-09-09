import pytest
import textwrap

from ...funcs import assert_query

from ..gql import FRAGMENT_PRODUCT_RELATION_CONNECTION

HEADERS = {
    "Authorization": "Bearer 0fb8c9e16d6f7c4961c4c49212bf197d79f14080"  # dojocat
}


##__________________________________________________________________||
params = [
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                {
                  allProductRelations {
                    ...fragmentProductRelationConnection
                  }
                }
              """
            )
            + FRAGMENT_PRODUCT_RELATION_CONNECTION,
        },
        id="query",
    ),
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                {
                  allProductRelations {
                    totalCount
                  }
                }
              """
            ),
        },
        id="total-count",
    ),
]


##__________________________________________________________________||
@pytest.mark.parametrize("data", params)
@pytest.mark.asyncio
async def test_schema(app, snapshot, data):
    await assert_query(app, snapshot, data, HEADERS)


##__________________________________________________________________||
