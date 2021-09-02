import pytest
import textwrap

from ...funcs import assert_query

from ..gql import FRAGMENT_PRODUCT_TYPE_CONNECTION

##__________________________________________________________________||
params = [
    pytest.param(
        [
            textwrap.dedent(
                """
          { allProductTypes(sort: ORDER_ASC) {
            ...fragmentProductTypeConnection
          }}
         """
                + FRAGMENT_PRODUCT_TYPE_CONNECTION
            )
        ],
        {},
        id="sort-order",
    ),
    pytest.param(
        [
            textwrap.dedent(
                """
          {
            allProductTypes {
              totalCount
            }
          }
        """
            ),
        ],
        {},
        id="total-count",
    ),
]


@pytest.mark.parametrize("args, kwargs", params)
def test_schema(app, snapshot, args, kwargs):
    assert_query(app, snapshot, [args, kwargs])


##__________________________________________________________________||
