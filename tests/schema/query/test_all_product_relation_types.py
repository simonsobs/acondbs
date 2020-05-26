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
