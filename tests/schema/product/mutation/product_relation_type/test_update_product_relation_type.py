from typing import Any, Mapping
from unittest import mock

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from ....funcs import assert_mutation
from ...gql import (
    FRAGMENT_PRODUCT_RELATION_TYPE_CONNECTION,
    MUTATION_UPDATE_PRODUCT_RELATION_TYPE,
)

QUERY = (
    '''
{
  allProductRelationTypes {
   ...fragmentProductRelationTypeConnection
  }
}
'''
    + FRAGMENT_PRODUCT_RELATION_TYPE_CONNECTION
)

HEADERS = {
    'Authorization': 'Bearer 0fb8c9e16d6f7c4961c4c49212bf197d79f14080'  # dojocat
}


params = [
    pytest.param(
        {
            'query': MUTATION_UPDATE_PRODUCT_RELATION_TYPE,
            'variables': {
                'typeId': 1,
                'input': {
                    'indefArticle': 'an',
                    'singular': 'mmap',
                    'plural': 'mmaps',
                },
            },
        },
        {'query': QUERY},
        id='update',
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
            'query': MUTATION_UPDATE_PRODUCT_RELATION_TYPE,
            'variables': {
                'typeId': 1,
                'input': {
                    'name': 'mmap',
                },
            },
        },
        {'query': QUERY},
        id='error-immutable-field',
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
