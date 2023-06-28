from typing import Any, Mapping
from unittest import mock

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from ....funcs import assert_mutation
from ...gql import MUTATION_CREATE_LOG, QUERY_ALL_LOGS

HEADERS_MUTATION: dict[str, Any] = {}

HEADERS_QUERY = {
    'Authorization': 'Bearer 90b2ee5fed25506df04fd37343bb68d1803dd97f'  # octocat
}


params = [
    pytest.param(
        {
            'query': MUTATION_CREATE_LOG,
            'variables': {
                'input': {
                    'level': 'ERROR',
                    'message': 'An exception is raised',
                }
            },
        },
        {'query': QUERY_ALL_LOGS},
        id='one',
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
        HEADERS_MUTATION,
        data_query,
        HEADERS_QUERY,
        mock_request_backup_db,
        success,
    )
