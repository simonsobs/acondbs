import pytest

from .funcs import assert_query_success

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
                  indefArticle
                  singular
                  plural
                  reverse {
                    typeId
                    name
                  }
                  relations {
                    edges {
                      node {
                        self_ {
                          name
                          type_ {
                            name
                          }
                        }
                        other {
                          name
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
        id='allProductRelationTypes'
    ),
]

##__________________________________________________________________||
@pytest.mark.parametrize('query', params)
def test_schema(app, snapshot, query):
    assert_query_success(app, snapshot, query)

##__________________________________________________________________||
