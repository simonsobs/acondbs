import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          {
            productType(typeId: 1) {
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
         ''',
        id='productType-by-typeId-one)'
    ),
    pytest.param(
        '''
          {
            productType(name: "map") {
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
         ''',
        id='productType-by-name-map)'
    ),
    pytest.param(
        '''
          {
            productType(typeId: 1, name: "map") {
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
         ''',
        id='productType-by-id-and-name-map)'
    ),
    pytest.param(
        '''
          {
            productType(typeId: 2, name: "map") {
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
         ''',
        id='productType-by-id-and-name-nonexistent)'
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
