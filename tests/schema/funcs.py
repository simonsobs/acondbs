from graphene.test import Client
from async_asgi_testclient import TestClient

from a2wsgi import WSGIMiddleware

from acondbs.schema import schema as default_schema

HEADERS_DEFAULT = {"Content-Type:": "application/json"}


##__________________________________________________________________||
async def assert_query(app, snapshot, data, headers=None, error=False):
    if not headers:
        headers = {}
    await assert_query_asgi_client(app, snapshot, data, headers, error=error)


async def assert_query_asgi_client(app, snapshot, data, headers, error=False):

    app = WSGIMiddleware(app)  # convert a wsgi app to an asgi app

    headers_custom = headers
    headers = HEADERS_DEFAULT.copy()
    headers.update(headers_custom)

    async with TestClient(app) as client:
        resp = await client.post("/graphql", json=data, headers=headers)

    resp_json = resp.json()

    # assert errors
    if error:
        assert "errors" in resp_json
        return

    assert "errors" not in resp_json

    # snapshot test
    #   https://github.com/syrusakbary/snapshottest/
    snapshot.assert_match(resp_json)


def assert_query_graphene_client(
    app, snapshot, query, error=False, schema=default_schema
):

    # create test client
    # https://docs.graphene-python.org/en/latest/testing/
    client = Client(schema)

    # arguments to client.execute()
    args, kwargs = query

    if "context_value" not in kwargs:
        # provide an empty dict to prevent errors
        # in graphene_sqlalchemy_filter.
        kwargs["context_value"] = {}

        # The detail is described in the commit message:
        #   https://github.com/simonsobs/acondbs/commit/0c65d5719129c4940eea0763ae7b9cc1bcddfe64
        # A related issue in graphene:
        #   https://github.com/graphql-python/graphene/issues/591

    # execute the query
    with app.app_context():
        result = client.execute(*args, **kwargs)

    # assert errors
    if error:
        assert "errors" in result
        return

    assert "errors" not in result

    # snapshot test
    #   https://github.com/syrusakbary/snapshottest/
    snapshot.assert_match(result)


async def assert_mutation(
    app,
    snapshot,
    data_mutation,
    headers_mutation,
    data_query,
    headers_query,
    mock_request_backup_db,
    success=True,
):
    await assert_query(
        app, snapshot, data_mutation, headers_mutation, error=not success
    )
    await assert_query(app, snapshot, data_query, headers_query)
    if success:
        mock_request_backup_db.assert_called()


##__________________________________________________________________||
