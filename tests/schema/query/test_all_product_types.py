import pytest

from .funcs import assert_query_success

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
    assert_query_success(app, snapshot, query)

##__________________________________________________________________||
