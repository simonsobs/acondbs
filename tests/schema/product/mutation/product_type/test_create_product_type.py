from typing import Any, Mapping
from unittest import mock

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from ....funcs import assert_mutation
from ...gql import MUTATION_CREATE_PRODUCT_TYPE, QUERY_ALL_PRODUCT_TYPES

HEADERS = {
    'Authorization': 'Bearer 0fb8c9e16d6f7c4961c4c49212bf197d79f14080'  # dojocat
}


params = [
    pytest.param(
        {
            'query': MUTATION_CREATE_PRODUCT_TYPE,
            'variables': {
                'input': {
                    'name': 'compass',
                    'order': 5,
                    'indefArticle': 'a',
                    'singular': 'compass',
                    'plural': 'compasses',
                    'icon': 'mdi-compass',
                    'fieldIds': [1, 2, 3],
                }
            },
        },
        {'query': QUERY_ALL_PRODUCT_TYPES},
        id='create',
    ),
    pytest.param(
        {
            'query': MUTATION_CREATE_PRODUCT_TYPE,
            'variables': {
                'input': {
                    'name': 'compass',
                    'order': 5,
                    'indefArticle': 'a',
                    'singular': 'compass',
                    'plural': 'compasses',
                    'icon': 'mdi-compass',
                    'fieldIds': [2, 3, 3, 1, 2, 3, 1, 1],
                }
            },
        },
        {'query': QUERY_ALL_PRODUCT_TYPES},
        id='field-ids-unsorted-duplicate',
    ),
    pytest.param(
        {
            'query': MUTATION_CREATE_PRODUCT_TYPE,
            'variables': {
                'input': {
                    'name': 'compass',
                    'order': 5,
                    'indefArticle': 'a',
                    'singular': 'compass',
                    'plural': 'compasses',
                    'icon': 'mdi-compass',
                }
            },
        },
        {'query': QUERY_ALL_PRODUCT_TYPES},
        id='no-fields',
    ),
    pytest.param(
        {
            'query': MUTATION_CREATE_PRODUCT_TYPE,
            'variables': {
                'input': {
                    'name': 'compass',
                    'order': 5,
                    'indefArticle': 'a',
                    'singular': 'compass',
                    'plural': 'compasses',
                    'icon': 'mdi-compass',
                    'fieldIds': [],
                }
            },
        },
        {'query': QUERY_ALL_PRODUCT_TYPES},
        id='empty-fields',
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
            'query': MUTATION_CREATE_PRODUCT_TYPE,
            'variables': {
                'input': {
                    'name': 'map',
                    'order': 5,
                    'indefArticle': 'a',
                    'singular': 'map',
                    'plural': 'maps',
                    'icon': 'mdi-map',
                }
            },
        },
        {'query': QUERY_ALL_PRODUCT_TYPES},
        id='error-already-exist',
    ),
    pytest.param(
        {
            'query': MUTATION_CREATE_PRODUCT_TYPE,
            'variables': {
                'input': {
                    'name': 'compass',
                    'order': 5,
                    'indefArticle': 'a',
                    'singular': 'compass',
                    'plural': 'compasses',
                    'icon': 'mdi-compass',
                    'fieldIds': [1, 2, 3, 88],
                }
            },
        },
        {'query': QUERY_ALL_PRODUCT_TYPES},
        id='non-existent-field',
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
