from typing import Any, Mapping
from unittest import mock

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from ....funcs import assert_mutation
from ...gql import (
    FRAGMENT_PRODUCT_RELATION_TYPE_CONNECTION,
    MUTATION_CREATE_PRODUCT_RELATION_TYPES,
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
            'query': MUTATION_CREATE_PRODUCT_RELATION_TYPES,
            'variables': {
                'type': {
                    'name': 'doctor',
                    'indefArticle': 'a',
                    'singular': 'doctor',
                    'plural': 'doctors',
                },
                'reverse': {
                    'name': 'patient',
                    'indefArticle': 'a',
                    'singular': 'patient',
                    'plural': 'patients',
                },
            },
        },
        {'query': QUERY},
        id='reverse',
    ),
    pytest.param(
        {
            'query': MUTATION_CREATE_PRODUCT_RELATION_TYPES,
            'variables': {
                'type': {
                    'name': 'spouse',
                    'indefArticle': 'a',
                    'singular': 'spouse',
                    'plural': 'spouses',
                },
                'selfReverse': True,
            },
        },
        {'query': QUERY},
        id='self_reverse',
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
            'query': MUTATION_CREATE_PRODUCT_RELATION_TYPES,
            'variables': {
                'type': {
                    'name': 'parent',
                    'indefArticle': 'a',
                    'singular': 'parent',
                    'plural': 'parents',
                },
                'reverse': {
                    'name': 'child',
                    'indefArticle': 'a',
                    'singular': 'child',
                    'plural': 'children',
                },
            },
        },
        {'query': QUERY},
        id='error-already-exist',
    ),
    pytest.param(
        {
            'query': MUTATION_CREATE_PRODUCT_RELATION_TYPES,
            'variables': {
                'type': {
                    'name': 'doctor',
                    'indefArticle': 'a',
                    'singular': 'doctor',
                    'plural': 'doctors',
                },
                'reverse': {
                    'name': 'patient',
                    'indefArticle': 'a',
                    'singular': 'patient',
                    'plural': 'patients',
                },
                'selfReverse': True,
            },
        },
        {'query': QUERY},
        id='error-reverse-and-self_reverse',
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
