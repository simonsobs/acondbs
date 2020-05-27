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
    assert ('errors' in result) == error
    snapshot.assert_match(result)

##__________________________________________________________________||
def assert_query_success(app, snapshot, query):
    client = Client(schema)
    with app.app_context():
        result = client.execute(query, context_value={})
        assert 'errors' not in result
        snapshot.assert_match(result)

##__________________________________________________________________||
def assert_mutation_success(app, snapshot, mutation, query, mock_request_backup_db):
    client = Client(schema)
    with app.app_context():
        result = client.execute(mutation, context_value={})
        assert 'errors' not in result
        snapshot.assert_match(result)
    with app.app_context():
        result = client.execute(query, context_value={})
        assert 'errors' not in result
        snapshot.assert_match(result)
    assert 1 == mock_request_backup_db.call_count

def assert_mutation_error(app, snapshot, mutation, query, mock_request_backup_db):
    client = Client(schema)
    with app.app_context():
        result = client.execute(mutation, context_value={})
        assert 'errors' in result
        snapshot.assert_match(result)
    with app.app_context():
        result = client.execute(query, context_value={})
        assert 'errors' not in result
        snapshot.assert_match(result)
    assert 0 == mock_request_backup_db.call_count

##__________________________________________________________________||
