import pytest

from .funcs import assert_query_success

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
          {
            allProducts(filters: {typeId: 1}, sort: PRODUCT_ID_DESC) {
              edges {
                node {
                  id
                  productId
                }
              }
            }
          }
        ''',
        id='allProducts-filtes-typeId-sort'
    ),
    pytest.param(
        '''
          {
            allProducts(filters: {typeName: "map"}, sort: PRODUCT_ID_DESC) {
              edges {
                node {
                  id
                  productId
                }
              }
            }
          }
        ''',
        id='allProducts-filtes-typeName-sort'
    ),
]

##__________________________________________________________________||
@pytest.mark.parametrize('query', params)
def test_schema(app, snapshot, query):
    assert_query_success(app, snapshot, query)

##__________________________________________________________________||
