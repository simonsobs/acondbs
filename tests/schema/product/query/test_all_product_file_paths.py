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

HEADERS = {
    "Authorization": "Bearer 0fb8c9e16d6f7c4961c4c49212bf197d79f14080"  # dojocat
}


##__________________________________________________________________||
params = [
    pytest.param(
        {"query": ALL_PRODUCT_FILE_PATHS},
        id="all",
    ),
]


##__________________________________________________________________||
@pytest.mark.parametrize("data", params)
@pytest.mark.asyncio
async def test_schema(app, snapshot, data):
    await assert_query(app, snapshot, data, HEADERS)

##__________________________________________________________________||
