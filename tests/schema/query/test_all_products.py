import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
        {
          allProducts {
            edges {
              node {
                productId
                name
                type_ {
                  typeId
                  name
                }
                relations {
                  edges {
                    node {
                      type_ {
                        name
                      }
                      other {
                        name
                        type_ {
                          name
                        }
                      }
                      reverse {
                        type_ {
                          name
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
         ''',
        id='allProducts'
    ),
    pytest.param(
        '''
        { allProducts(filters: {typeId: 1}, first: 2) {
             edges { node { name } }
           } }
         ''',
        id='allProducts-filtes-typeId-one-first-two'
    ),
    pytest.param(
        '''
        { allProducts(filters: {typeName: "beam"}, first: 2) {
             edges { node { name } }
           } }
         ''',
        id='allProducts-filtes-typeName-beam-first-two'
    ),
    pytest.param(
        '''
        { allProducts(first: 2) {
             edges { node { name } }
           } }
         ''',
        id='allProducts-first-two'
    ),
    pytest.param(
        '''
        { allProducts(first: 2, sort: DATE_POSTED_DESC) {
             edges { node { name } }
           } }
         ''',
        id='allProducts-first-two-sort'
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
