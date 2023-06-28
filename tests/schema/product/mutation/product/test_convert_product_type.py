from typing import Any, Mapping
from unittest import mock

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from ....funcs import assert_mutation
from ...gql import MUTATION_CONVERT_PRODUCT_TYPE, QUERY_ALL_PRODUCTS

HEADERS = {
    'Authorization': 'Bearer 39d86487d76a84087f1da599c872dac4473e5f07',  # user1
}


params = [
    pytest.param(
        {
            'query': MUTATION_CONVERT_PRODUCT_TYPE,
            'variables': {
                'productId': 1,
                'typeId': 2,
            },
        },
        {'query': QUERY_ALL_PRODUCTS},
        id='convert',
    ),
]


@pytest.mark.parametrize('data_mutation, data_query', params)
@pytest.mark.asyncio
async def test_schema_success(
    app: Flask,
    snapshot: PyTestSnapshotTest,
    data_mutation: Mapping[str, Any],
    data_query: Mapping[str, Any],
    mock_request_backup_db: mock.Mock,
) -> None:
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
