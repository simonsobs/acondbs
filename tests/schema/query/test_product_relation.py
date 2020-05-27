import pytest
import textwrap

from ..funcs import assert_query_success

from ..gql import FRAGMENT_PRODUCT_RELATION

##__________________________________________________________________||
params = [
    pytest.param(
        textwrap.dedent('''
          {
            productRelation(relationId: 1) {
              ...fragmentProductRelation
            }
          }
        ''') + FRAGMENT_PRODUCT_RELATION,
        id='type_id'
    ),
    pytest.param(
        textwrap.dedent('''
          {
            productRelation(relationId: 222) {
              ...fragmentProductRelation
            }
          }
        ''') + FRAGMENT_PRODUCT_RELATION,
        id='type_id-nonexistent'
    ),
]

##__________________________________________________________________||
@pytest.mark.parametrize('query', params)
def test_schema(app, snapshot, query):
    assert_query_success(app, snapshot, query)

##__________________________________________________________________||
