import pytest
import textwrap

from ...funcs import assert_query

from ..gql import FRAGMENT_PRODUCT_SHALLOW, FRAGMENT_PRODUCT

HEADERS = {
    "Authorization": "Bearer 0fb8c9e16d6f7c4961c4c49212bf197d79f14080"  # dojocat
}


##__________________________________________________________________||
params = [
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                query Product($productId: Int) {
                  product(productId: $productId) {
                    ...fragmentProduct
                  }
                }
                """
            )
            + FRAGMENT_PRODUCT,
            "variables": {"productId": 1},
        },
        id="deep",
    ),
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                query Product($productId: Int) {
                  product(productId: $productId) {
                    ...fragmentProduct
                  }
                }
                """
            )
            + FRAGMENT_PRODUCT,
            "variables": {"productId": 9899},
        },
        id="product_id-nonexistent",
    ),
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                query ProductByTypeIdAndName($typeId: Int!, $name: String!) {
                  product(typeId: $typeId, name: $name) {
                    ...fragmentProductShallow
                  }
                }
              """
            )
            + FRAGMENT_PRODUCT_SHALLOW,
            "variables": {"typeId": 1, "name": "map1"},
        },
        id="type_id-name",
    ),
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                { product(productId: 1, name: "map1") {
                    ...fragmentProductShallow
                  }
                }
                 """
            )
            + FRAGMENT_PRODUCT_SHALLOW,
        },
        id="product_id-name",
    ),
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                { product(productId: 1, name: "map2") {
                    ...fragmentProductShallow
                  }
                }
                 """
            )
            + FRAGMENT_PRODUCT_SHALLOW,
        },
        id="product_id-name-nonexistent",
    ),
]


##__________________________________________________________________||
@pytest.mark.parametrize("data", params)
@pytest.mark.asyncio
async def test_schema(app, snapshot, data):
    await assert_query(app, snapshot, data, HEADERS)


##__________________________________________________________________||
