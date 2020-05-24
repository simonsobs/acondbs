import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          {
            allProductRelationTypes {
              edges {
                node {
                  typeId
                  name
                }
              }
            }
          }
         ''',
        id='allProductRelationTypes'
    ),
]

@pytest.mark.parametrize('query', params)
def test_schema(app, snapshot, query):
    client = Client(schema)
    with app.app_context():
        result = client.execute(query, context_value={})
        assert 'errors' not in result
        snapshot.assert_match(result)

##__________________________________________________________________||
