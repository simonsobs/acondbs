from typing import Any, Mapping

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from .funcs import assert_query

ALEMBIC_VERSION = '''
{
  alembicVersion
}
'''

HEADERS = {'Authorization': 'Bearer token123'}  # octocat


params = [
    pytest.param(
        {'query': ALEMBIC_VERSION},
        id='alembicVersion',
    ),
]


@pytest.mark.parametrize('data', params)
@pytest.mark.asyncio
async def test_schema(
    app: Flask, snapshot: PyTestSnapshotTest, data: Mapping[str, Any]
) -> None:
    await assert_query(app, snapshot, data, HEADERS)

    # Note: the result is None, i.e., {'data': {'alembicVersion': None }}
    # because the migration is not applied in the tests.
