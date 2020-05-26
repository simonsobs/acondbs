import pytest
import textwrap

from .funcs import assert_query_success

from ..gql import FRAGMENT_PRODUCT_RELATION_TYPE

##__________________________________________________________________||
params = [
    pytest.param(
        textwrap.dedent('''
          {
            productRelationType(typeId: 1) {
              ...fragmentProductRelationType
            }
          }
        ''') + FRAGMENT_PRODUCT_RELATION_TYPE,
        id='type_id'
    ),
    pytest.param(
        textwrap.dedent('''
          {
            productRelationType(name: "parent") {
              ...fragmentProductRelationType
            }
          }
        ''') + FRAGMENT_PRODUCT_RELATION_TYPE,
        id='name'
    ),
    pytest.param(
        textwrap.dedent('''
          {
            productRelationType(typeId: 1, name: "parent") {
              ...fragmentProductRelationType
            }
          }
        ''') + FRAGMENT_PRODUCT_RELATION_TYPE,
        id='type_id-and-name'
    ),
    pytest.param(
        textwrap.dedent('''
          {
            productRelationType(typeId: 2, name: "parent") {
              ...fragmentProductRelationType
            }
          }
        ''') + FRAGMENT_PRODUCT_RELATION_TYPE,
        id='type_id-and-name-nonexistent)'
    ),
]

##__________________________________________________________________||
@pytest.mark.parametrize('query', params)
def test_schema(app, snapshot, query):
    assert_query_success(app, snapshot, query)

##__________________________________________________________________||
