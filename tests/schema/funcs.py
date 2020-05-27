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
def assert_query_success(app, snapshot, query):
    '''deprecated. use assert_query() instead
    '''
    client = Client(schema)
    with app.app_context():
        result = client.execute(query, context_value={})
        assert 'errors' not in result
        snapshot.assert_match(result)

##__________________________________________________________________||
def assert_mutation_success(app, snapshot, mutation, query, mock_request_backup_db):
    '''deprecated. use assert_mutation() instead
    '''
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
    '''deprecated. use assert_mutation() instead
    '''
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
