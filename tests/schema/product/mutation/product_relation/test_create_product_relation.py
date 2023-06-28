from typing import Any, Mapping
from unittest import mock

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from ....funcs import assert_mutation
from ...gql import (
    FRAGMENT_PRODUCT_RELATION_CONNECTION,
    MUTATION_CREATE_PRODUCT_RELATION,
)

QUERY = (
    '''
{
  allProductRelations {
    ...fragmentProductRelationConnection
  }
}
'''
    + FRAGMENT_PRODUCT_RELATION_CONNECTION
)

HEADERS = {
    'Authorization': 'Bearer 0fb8c9e16d6f7c4961c4c49212bf197d79f14080'  # dojocat
}


params = [
    pytest.param(
        {
            'query': MUTATION_CREATE_PRODUCT_RELATION,
            'variables': {
                'input': {'typeId': 1, 'selfProductId': 5, 'otherProductId': 1}
            },
        },
        {'query': QUERY},
        id='create',
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


params = [
    pytest.param(
        {
            'query': MUTATION_CREATE_PRODUCT_RELATION,
            'variables': {
                'input': {'typeId': 20, 'selfProductId': 5, 'otherProductId': 1}
            },
        },
        {'query': QUERY},
        id='error-type_id-nonexistent',
    ),
    pytest.param(
        {
            'query': MUTATION_CREATE_PRODUCT_RELATION,
            'variables': {
                'input': {'typeId': 1, 'selfProductId': 10, 'otherProductId': 1}
            },
        },
        {'query': QUERY},
        id='error-self_product_id-nonexistent',
    ),
    pytest.param(
        {
            'query': MUTATION_CREATE_PRODUCT_RELATION,
            'variables': {
                'input': {'typeId': 1, 'selfProductId': 5, 'otherProductId': 20}
            },
        },
        {'query': QUERY},
        id='error-otheer_product_id-nonexistent',
    ),
    pytest.param(
        {
            'query': MUTATION_CREATE_PRODUCT_RELATION,
            'variables': {
                'input': {'typeId': 2, 'selfProductId': 1, 'otherProductId': 4}
            },
        },
        {'query': QUERY},
        id='error-duplicate',
    ),
]


@pytest.mark.parametrize('data_mutation, data_query', params)
@pytest.mark.asyncio
async def test_schema_error(
    app: Flask,
    snapshot: PyTestSnapshotTest,
    data_mutation: Mapping[str, Any],
    data_query: Mapping[str, Any],
    mock_request_backup_db: mock.Mock,
) -> None:
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
