import pytest

from ..funcs import assert_query_success

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
        id='productType-by-typeId-one'
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
        id='productType-by-name-map'
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
        id='productType-by-id-and-name-map'
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
        id='productType-by-id-and-name-nonexistent'
    ),
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
              products(sort: DATE_PRODUCED_DESC) {
                edges {
                  node {
                    name
                  }
                }
              }
            }
          }
         ''',
        id='productType-by-typeId-one-sort-products'
    ),
]

##__________________________________________________________________||
@pytest.mark.parametrize('query', params)
def test_schema(app, snapshot, query):
    assert_query_success(app, snapshot, query)

##__________________________________________________________________||
