import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          { allProductTypes(sort: ORDER_ASC) {
            edges {
              node {
                typeId
                name
                order
                indefArticle
                singular
                plural
                icon
                products {
                  edges {
                    node {
                      name
                    }
                  }
                }
              }
            }
          }}
         ''',
        id='allProductTypes'
    ),
]

@pytest.mark.parametrize('query', params)
def test_schema(app, snapshot, query):
    client = Client(schema)
    with app.app_context():
        result = client.execute(query)
        assert 'errors' not in result
        snapshot.assert_match(result)

##__________________________________________________________________||
