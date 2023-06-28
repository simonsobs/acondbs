from typing import Any, Mapping
from unittest import mock

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from .funcs import assert_mutation
from .misc.gql import QUERY_ALL_LOGS

QUERY = '''
{
  noSuchField
}
'''.strip()

HEADERS = {
    'Authorization': 'Bearer 90b2ee5fed25506df04fd37343bb68d1803dd97f'  # octocat
}

HEADERS_QUERY = {
    'Authorization': 'Bearer 90b2ee5fed25506df04fd37343bb68d1803dd97f'  # octocat
}


@pytest.fixture
def app(app_users: Flask) -> Flask:
    y = app_users
    return y


params = [
    pytest.param(
        {
            'query': QUERY,
            'variables': {'var1': 100},
        },
        {'query': QUERY_ALL_LOGS},
        id='one',
    ),
]


@pytest.mark.parametrize('data_mutation, data_query', params)
@pytest.mark.asyncio
async def test_schema(
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
        HEADERS_QUERY,
        mock_request_backup_db,
        success,
    )
