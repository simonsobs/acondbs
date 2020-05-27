from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
def assert_query_success(app, snapshot, query):
    client = Client(schema)
    with app.app_context():
        result = client.execute(query, context_value={})
        assert 'errors' not in result
        snapshot.assert_match(result)

##__________________________________________________________________||
