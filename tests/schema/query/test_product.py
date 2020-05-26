import pytest
import textwrap

from .funcs import assert_query_success

from .gql import FRAGMENT_PRODUCT_DEEP

##__________________________________________________________________||
params = [
    pytest.param(
        textwrap.dedent('''
        {
          product(productId: 1001) {
            ...fragmentProductDeep
          }
        }
         ''') + FRAGMENT_PRODUCT_DEEP,
        id='product_id'
    ),
    pytest.param(
        textwrap.dedent('''
        { product(productId: 2001) {
            ...fragmentProductDeep
          }
        }
         ''') + FRAGMENT_PRODUCT_DEEP,
        id='product_id-nonexistent'
    ),
    pytest.param(
        textwrap.dedent('''
        { product(name: "lat20190213") {
            ...fragmentProductDeep
          }
        }
         ''') + FRAGMENT_PRODUCT_DEEP,
        id='name'
    ),
    pytest.param(
        textwrap.dedent('''
        { product(productId: 1001, name: "lat20190213") {
            ...fragmentProductDeep
          }
        }
         ''') + FRAGMENT_PRODUCT_DEEP,
        id='product_id-name'
    ),
    pytest.param(
        textwrap.dedent('''
        { product(productId: 1002, name: "lat20190213") {
            ...fragmentProductDeep
          }
        }
         ''') + FRAGMENT_PRODUCT_DEEP,
        id='product_id-name-nonexistent'
    ),
    pytest.param(
        textwrap.dedent('''
        { product(typeId: 1, name: "lat20190213") {
            ...fragmentProductDeep
          }
        }
         ''') + FRAGMENT_PRODUCT_DEEP,
        id='type_id-name'
    ),
]

##__________________________________________________________________||
@pytest.mark.parametrize('query', params)
def test_schema(app, snapshot, query):
    assert_query_success(app, snapshot, query)

##__________________________________________________________________||
