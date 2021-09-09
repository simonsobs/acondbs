import pytest
import textwrap

from ...funcs import assert_query

from ..gql import FRAGMENT_PRODUCT_RELATION_TYPE

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
                  productRelationType(typeId: 1) {
                    ...fragmentProductRelationType
                  }
                }
              """
            )
            + FRAGMENT_PRODUCT_RELATION_TYPE,
        },
        id="type_id",
    ),
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                {
                  productRelationType(name: "parent") {
                    ...fragmentProductRelationType
                  }
                }
              """
            )
            + FRAGMENT_PRODUCT_RELATION_TYPE,
        },
        id="name",
    ),
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                {
                  productRelationType(typeId: 1, name: "parent") {
                    ...fragmentProductRelationType
                  }
                }
              """
            )
            + FRAGMENT_PRODUCT_RELATION_TYPE,
        },
        id="type_id-and-name",
    ),
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                {
                  productRelationType(typeId: 2, name: "parent") {
                    ...fragmentProductRelationType
                  }
                }
              """
            )
            + FRAGMENT_PRODUCT_RELATION_TYPE,
        },
        id="type_id-and-name-nonexistent)",
    ),
]


##__________________________________________________________________||
@pytest.mark.parametrize("data", params)
@pytest.mark.asyncio
async def test_schema(app, snapshot, data):
    await assert_query(app, snapshot, data, HEADERS)


##__________________________________________________________________||
