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
                productType {
                  productTypeId
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
                        productType {
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
        { allProducts(filters: {productTypeId: 1}, first: 2) {
             edges { node { name } }
           } }
         ''',
        id='allProducts-filtes-productTypeId-one-first-two'
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
    pytest.param(
        '''
        { product(productId: 1001) { name } }
         ''',
        id='product-by-ProductID'
    ),
    pytest.param(
        '''
        { product(productId: 2001) { name } }
         ''',
        id='product-by-ProductID-nonexistent'
    ),
    pytest.param(
        '''
        { product(name: "lat20190213") { productId } }
         ''',
        id='product-by-name'
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
