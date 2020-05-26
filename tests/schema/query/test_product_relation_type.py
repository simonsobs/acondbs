import pytest

from .funcs import assert_query_success

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          {
            productRelationType(typeId: 1) {
              typeId
              name
            }
          }
         ''',
        id='productRelationType-by-TypeId-one)'
    ),
    pytest.param(
        '''
          {
            productRelationType(name: "parent") {
              typeId
              name
            }
          }
         ''',
        id='productRelationType-by-name-parent)'
    ),
    pytest.param(
        '''
          {
            productRelationType(typeId: 1, name: "parent") {
              typeId
              name
            }
          }
         ''',
        id='productRelationType-by-id-and-name-parent)'
    ),
    pytest.param(
        '''
          {
            productRelationType(typeId: 2, name: "parent") {
              typeId
              name
            }
          }
         ''',
        id='productRelationType-by-id-and-name-nonexistent)'
    ),
]

##__________________________________________________________________||
@pytest.mark.parametrize('query', params)
def test_schema(app, snapshot, query):
    assert_query_success(app, snapshot, query)

##__________________________________________________________________||
