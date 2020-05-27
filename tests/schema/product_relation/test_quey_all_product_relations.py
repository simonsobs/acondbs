import pytest
import textwrap

from ..funcs import assert_query_success

from ..gql import FRAGMENT_PRODUCT_RELATION_CONNECTION

##__________________________________________________________________||
params = [
    pytest.param(
        textwrap.dedent('''
          {
            allProductRelations {
              ...fragmentProductRelationConnection
            }
          }
        ''') + FRAGMENT_PRODUCT_RELATION_CONNECTION,
        id='query'
    ),
]

##__________________________________________________________________||
@pytest.mark.parametrize('query', params)
def test_schema(app, snapshot, query):
    assert_query_success(app, snapshot, query)

##__________________________________________________________________||
