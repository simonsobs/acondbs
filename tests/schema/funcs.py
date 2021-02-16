from graphene.test import Client

from acondbs.schema import create_schema

##__________________________________________________________________||
def assert_query(app, snapshot, query, error=False):

    # create test client
    # https://docs.graphene-python.org/en/latest/testing/
    schema = create_schema()
    client = Client(schema)

    # arguments to client.execute()
    args, kwargs = query

    if 'context_value' not in kwargs:
        # provide an empty dict to prevent errors
        # in graphene_sqlalchemy_filter.
        kwargs['context_value'] = {}

        # The detail is described in the commit message:
        #   https://github.com/simonsobs/acondbs/commit/0c65d5719129c4940eea0763ae7b9cc1bcddfe64
        # A related issue in graphene:
        #   https://github.com/graphql-python/graphene/issues/591

    # execute the query
    with app.app_context():
        result = client.execute(*args, **kwargs)

    # assert errors
    if error:
        assert 'errors' in result
        return

    assert 'errors' not in result

    # snapshot test
    #   https://github.com/syrusakbary/snapshottest/
    snapshot.assert_match(result)

def assert_mutation(app, snapshot, mutation, query, mock_request_backup_db, success=True):
    assert_query(app, snapshot, mutation, error=not success)
    assert_query(app, snapshot, query)
    if success:
        mock_request_backup_db.assert_called()

##__________________________________________________________________||
