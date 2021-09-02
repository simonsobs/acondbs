import pytest

from ...funcs import assert_query

ALL_PRODUCT_FILE_PATHS = """
{
  allProductFilePaths {
    totalCount
    edges {
      node {
        pathId
        path
        note
        product {
          name
        }
      }
    }
  }
}
"""

##__________________________________________________________________||
params = [
    pytest.param(
        [
            ALL_PRODUCT_FILE_PATHS,
        ],
        {},
        id="all",
    ),
]


##__________________________________________________________________||
@pytest.mark.parametrize("args, kwargs", params)
def test_schema(app, snapshot, args, kwargs):
    assert_query(app, snapshot, [args, kwargs])


##__________________________________________________________________||
