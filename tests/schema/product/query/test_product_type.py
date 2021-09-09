import pytest
import textwrap

from ...funcs import assert_query

from ..gql import FRAGMENT_PRODUCT_TYPE

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
                  productType(typeId: 1) {
                    ...fragmentProductType
                  }
                }
               """
            )
            + FRAGMENT_PRODUCT_TYPE,
        },
        id="type_id",
    ),
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                {
                  productType(name: "map") {
                    ...fragmentProductType
                  }
                }
               """
            )
            + FRAGMENT_PRODUCT_TYPE,
        },
        id="name",
    ),
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                {
                  productType(typeId: 1, name: "map") {
                    ...fragmentProductType
                  }
                }
               """
            )
            + FRAGMENT_PRODUCT_TYPE,
        },
        id="type_id-and-name",
    ),
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                {
                  productType(typeId: 2, name: "map") {
                    ...fragmentProductType
                  }
                }
               """
            )
            + FRAGMENT_PRODUCT_TYPE,
        },
        id="type_id-and-name-nonexistent",
    ),
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                {
                  productType(typeId: 1) {
                    typeId
                    name
                    order
                    indefArticle
                    singular
                    plural
                    icon
                    products(sort: DATE_PRODUCED_DESC) {
                      edges {
                        node {
                          name
                        }
                      }
                    }
                  }
                }
               """
            )
        },
        id="type_id-sort-products",
    ),
]


##__________________________________________________________________||
@pytest.mark.parametrize("data", params)
@pytest.mark.asyncio
async def test_schema(app, snapshot, data):
    await assert_query(app, snapshot, data, HEADERS)


##__________________________________________________________________||
