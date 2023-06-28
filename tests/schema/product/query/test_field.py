from typing import Mapping

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from ...funcs import assert_query
from ..gql import QUERY_FIELD

HEADERS = {
    'Authorization': 'Bearer 0fb8c9e16d6f7c4961c4c49212bf197d79f14080'  # dojocat
}


params = [
    pytest.param(
        {
            #
            'query': QUERY_FIELD,
            'variables': {'fieldId': 1},
        },
        id='by-field-id',
    ),
    pytest.param(
        {
            #
            'query': QUERY_FIELD,
            'variables': {'name': 'contact'},
        },
        id='by-name',
    ),
]


@pytest.mark.parametrize('data', params)
@pytest.mark.asyncio
async def test_schema(
    app: Flask, snapshot: PyTestSnapshotTest, data: Mapping[str, str]
) -> None:
    await assert_query(app, snapshot, data, HEADERS)
