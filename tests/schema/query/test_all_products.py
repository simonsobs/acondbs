import pytest
import textwrap

from .funcs import assert_query_success

from .gql import FRAGMENT_PRODUCT_CONNECTION_DEEP

##__________________________________________________________________||
params = [
    pytest.param(
        textwrap.dedent('''
        {
          allProducts {
            ...fragmentProductConnectionDeep
          }
        }
         ''') + FRAGMENT_PRODUCT_CONNECTION_DEEP,
        id='allProducts'
    ),
    pytest.param(
        textwrap.dedent('''
        {
          allProducts(first: 2) {
            ...fragmentProductConnectionDeep
          }
        }
         ''') + FRAGMENT_PRODUCT_CONNECTION_DEEP,
        id='allProducts-first-two'
    ),
    pytest.param(
        textwrap.dedent('''
        {
          allProducts(first: 2, sort: DATE_POSTED_DESC) {
            ...fragmentProductConnectionDeep
          }
        }
         ''') + FRAGMENT_PRODUCT_CONNECTION_DEEP,
        id='allProducts-first-two-sort'
    ),
    pytest.param(
        textwrap.dedent('''
        {
          allProducts(filters: {typeId: 1}, first: 2) {
            ...fragmentProductConnectionDeep
          }
        }
         ''') + FRAGMENT_PRODUCT_CONNECTION_DEEP,
        id='allProducts-filtes-typeId-one-first-two'
    ),
    pytest.param(
        textwrap.dedent('''
        {
          allProducts(filters: {typeName: "beam"}, first: 2) {
            ...fragmentProductConnectionDeep
          }
        }
         ''') + FRAGMENT_PRODUCT_CONNECTION_DEEP,
        id='allProducts-filtes-typeName-beam-first-two'
    ),
    pytest.param(
        textwrap.dedent('''
        {
          allProducts(filters: {typeId: 1}, sort: PRODUCT_ID_DESC) {
            ...fragmentProductConnectionDeep
          }
        }
         ''') + FRAGMENT_PRODUCT_CONNECTION_DEEP,
        id='allProducts-filtes-typeId-sort'
    ),
    pytest.param(
        textwrap.dedent('''
        {
          allProducts(filters: {typeName: "map"}, sort: PRODUCT_ID_DESC) {
            ...fragmentProductConnectionDeep
          }
        }
         ''') + FRAGMENT_PRODUCT_CONNECTION_DEEP,
        id='allProducts-filtes-typeName-sort'
    ),
]

##__________________________________________________________________||
@pytest.mark.parametrize('query', params)
def test_schema(app, snapshot, query):
    assert_query_success(app, snapshot, query)

##__________________________________________________________________||
