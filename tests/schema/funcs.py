from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
def assert_query(app, snapshot, query, error=False):
    args, kwags = query
    if 'context_value' not in kwags:
        kwags['context_value'] = {}
    client = Client(schema)
    with app.app_context():
        result = client.execute(*args, **kwags)
    if error:
        assert 'errors' in result
    else:
        assert 'errors' not in result
    snapshot.assert_match(result)

def assert_mutation(app, snapshot, mutation, query, mock_request_backup_db, success=True):
    assert_query(app, snapshot, mutation, error=not success)
    assert_query(app, snapshot, query)

##__________________________________________________________________||
