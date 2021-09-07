import pytest

from ....funcs import assert_mutation

from ...gql import CREATE_PRODUCT_TYPE

QEURY = """
{
  allProductTypes {
    edges {
      node {
        name
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
        {
            "query": CREATE_PRODUCT_TYPE,
            "variables": {
                "input": {
                    "name": "compass",
                    "order": 5,
                    "indefArticle": "a",
                    "singular": "compass",
                    "plural": "compasses",
                    "icon": "mdi-compass",
                }
            },
        },
        {"query": QEURY},
        id="create",
    ),
]


@pytest.mark.parametrize("data_mutation, data_query", params)
@pytest.mark.asyncio
async def test_schema_success(
    app, snapshot, data_mutation, data_query, mock_request_backup_db
):

    success = True
    await assert_mutation(
        app,
        snapshot,
        data_mutation,
        HEADERS,
        data_query,
        HEADERS,
        mock_request_backup_db,
        success,
    )


##__________________________________________________________________||
params = [
    pytest.param(
        {
            "query": CREATE_PRODUCT_TYPE,
            "variables": {
                "input": {
                    "name": "map",
                    "order": 5,
                    "indefArticle": "a",
                    "singular": "map",
                    "plural": "maps",
                    "icon": "mdi-map",
                }
            },
        },
        {"query": QEURY},
        id="error-already-exist",
    ),
]


@pytest.mark.parametrize("data_mutation, data_query", params)
@pytest.mark.asyncio
async def test_schema_error(
    app, snapshot, data_mutation, data_query, mock_request_backup_db
):
    success = False
    await assert_mutation(
        app,
        snapshot,
        data_mutation,
        HEADERS,
        data_query,
        HEADERS,
        mock_request_backup_db,
        success,
    )


##__________________________________________________________________||
