import pytest
import textwrap

from ...funcs import assert_query

from ..gql import FRAGMENT_PRODUCT_CONNECTION_SHALLOW, FRAGMENT_PRODUCT_CONNECTION_DEEP

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
                  allProducts {
                    ...fragmentProductConnectionDeep
                  }
                }
              """
            )
            + FRAGMENT_PRODUCT_CONNECTION_DEEP,
        },
        id="deep",
    ),
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                {
                  allProducts(first: 2) {
                    ...fragmentProductConnectionShallow
                  }
                }
              """
            )
            + FRAGMENT_PRODUCT_CONNECTION_SHALLOW,
        },
        id="first-two",
    ),
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                {
                  allProducts(first: 2, sort: DATE_PRODUCED_DESC) {
                    ...fragmentProductConnectionShallow
                  }
                }
               """
            )
            + FRAGMENT_PRODUCT_CONNECTION_SHALLOW,
        },
        id="first-two-sort",
    ),
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                {
                  allProducts(filters: {typeId: 1}, first: 2) {
                    ...fragmentProductConnectionShallow
                  }
                }
               """
            )
            + FRAGMENT_PRODUCT_CONNECTION_SHALLOW,
        },
        id="filters-type_id-first-two",
    ),
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                {
                  allProducts(filters: {typeName: "map"}, first: 2) {
                    ...fragmentProductConnectionShallow
                  }
                }
               """
            )
            + FRAGMENT_PRODUCT_CONNECTION_SHALLOW,
        },
        id="filters-type_name-first-two",
    ),
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                {
                  allProducts(filters: {typeId: 1}, sort: DATE_PRODUCED_DESC) {
                    ...fragmentProductConnectionShallow
                  }
                }
               """
            )
            + FRAGMENT_PRODUCT_CONNECTION_SHALLOW,
        },
        id="filters-type_id-sort",
    ),
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                {
                  allProducts(filters: {typeName: "map"}, sort: DATE_PRODUCED_DESC) {
                    ...fragmentProductConnectionShallow
                  }
                }
               """
            )
            + FRAGMENT_PRODUCT_CONNECTION_SHALLOW,
        },
        id="filters-type_name-sort",
    ),
    pytest.param(
        {
            "query": textwrap.dedent(
                """
                {
                  allProducts(filters: {typeName: "map"}, first: 2) {
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
