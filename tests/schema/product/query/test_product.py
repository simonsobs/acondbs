from typing import Mapping

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from ...funcs import assert_query
from ..gql import QUERY_PRODUCT, QUERY_PRODUCT_SHALLOW

HEADERS = {
    'Authorization': 'Bearer 0fb8c9e16d6f7c4961c4c49212bf197d79f14080'  # dojocat
}


params = [
    pytest.param(
        {
            #
            'query': QUERY_PRODUCT,
            'variables': {'productId': 1},
        },
        id='deep',
    ),
    pytest.param(
        {
            #
            'query': QUERY_PRODUCT,
            'variables': {'productId': 9899},
        },
        id='product_id-nonexistent',
    ),
    pytest.param(
        {
            #
            'query': QUERY_PRODUCT_SHALLOW,
            'variables': {'typeId': 1, 'name': 'map1'},
        },
        id='type_id-name',
    ),
    pytest.param(
        {
            #
            'query': QUERY_PRODUCT_SHALLOW,
            'variables': {'productId': 1, 'name': 'map1'},
        },
        id='product_id-name',
    ),
    pytest.param(
        {
            #
            'query': QUERY_PRODUCT_SHALLOW,
            'variables': {'productId': 1, 'name': 'map2'},
        },
        id='product_id-name-nonexistent',
    ),
]


@pytest.mark.parametrize('data', params)
@pytest.mark.asyncio
async def test_schema(
    app: Flask, snapshot: PyTestSnapshotTest, data: Mapping[str, str]
) -> None:
    await assert_query(app, snapshot, data, HEADERS)
