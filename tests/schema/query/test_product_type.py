import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          { allProductTypes {
            edges {
              node {
                typeId
                name
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
    pytest.param(
        '''
          {
            productType(typeId: 1) {
              name
            }
          }
         ''',
        id='productType-by-typeId-one)'
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
