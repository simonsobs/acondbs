from typing import Any, Mapping, Optional
from unittest import mock

from a2wsgi import WSGIMiddleware
from async_asgi_testclient import TestClient
from snapshottest.pytest import PyTestSnapshotTest

HEADERS_DEFAULT = {'Content-Type:': 'application/json'}


async def assert_query(
    app: Any,
    snapshot: PyTestSnapshotTest,
    data: Mapping[str, Any],
    headers: Optional[Mapping[str, Any]] = None,
    error: bool = False,
) -> None:
    if not headers:
        headers = {}

    app = WSGIMiddleware(app)  # convert a wsgi app to an asgi app

    headers_custom = headers
    headers = HEADERS_DEFAULT.copy()
    headers.update(headers_custom)

    async with TestClient(app) as client:
        resp = await client.post('/graphql', json=data, headers=headers)

    resp_json = resp.json()

    # assert errors
    if error:
        assert 'errors' in resp_json
        return

    assert 'errors' not in resp_json

    # snapshot test
    #   https://github.com/syrusakbary/snapshottest/
    snapshot.assert_match(resp_json)


async def assert_mutation(
    app: Any,
    snapshot: PyTestSnapshotTest,
    data_mutation: Mapping[str, Any],
    headers_mutation: Mapping[str, Any],
    data_query: Mapping[str, Any],
    headers_query: Mapping[str, Any],
    mock_request_backup_db: mock.Mock,
    success: bool = True,
) -> None:
    if success:
        mock_request_backup_db.reset_mock()

    await assert_query(
        app, snapshot, data_mutation, headers_mutation, error=not success
    )

    if success:
        mock_request_backup_db.assert_called_once()

    await assert_query(app, snapshot, data_query, headers_query)
