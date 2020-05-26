import pytest
import textwrap

from .funcs import assert_query_success

from .gql import (
    FRAGMENT_PRODUCT_CONNECTION_SHALLOW,
    FRAGMENT_PRODUCT_CONNECTION_DEEP
    )

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
        id='deep'
    ),
    pytest.param(
        textwrap.dedent('''
        {
          allProducts(first: 2) {
            ...fragmentProductConnectionShallow
          }
        }
         ''') + FRAGMENT_PRODUCT_CONNECTION_SHALLOW,
        id='first-two'
    ),
    pytest.param(
        textwrap.dedent('''
        {
          allProducts(first: 2, sort: DATE_POSTED_DESC) {
            ...fragmentProductConnectionShallow
          }
        }
         ''') + FRAGMENT_PRODUCT_CONNECTION_SHALLOW,
        id='first-two-sort'
    ),
    pytest.param(
        textwrap.dedent('''
        {
          allProducts(filters: {typeId: 1}, first: 2) {
            ...fragmentProductConnectionShallow
          }
        }
         ''') + FRAGMENT_PRODUCT_CONNECTION_SHALLOW,
        id='filtes-typeId-first-two'
    ),
    pytest.param(
        textwrap.dedent('''
        {
          allProducts(filters: {typeName: "beam"}, first: 2) {
            ...fragmentProductConnectionShallow
          }
        }
         ''') + FRAGMENT_PRODUCT_CONNECTION_SHALLOW,
        id='filtes-typeName-first-two'
    ),
    pytest.param(
        textwrap.dedent('''
        {
          allProducts(filters: {typeId: 1}, sort: PRODUCT_ID_DESC) {
            ...fragmentProductConnectionShallow
          }
        }
         ''') + FRAGMENT_PRODUCT_CONNECTION_SHALLOW,
        id='filtes-typeId-sort'
    ),
    pytest.param(
        textwrap.dedent('''
        {
          allProducts(filters: {typeName: "map"}, sort: PRODUCT_ID_DESC) {
            ...fragmentProductConnectionShallow
          }
        }
         ''') + FRAGMENT_PRODUCT_CONNECTION_SHALLOW,
        id='filtes-typeName-sort'
    ),
]

##__________________________________________________________________||
@pytest.mark.parametrize('query', params)
def test_schema(app, snapshot, query):
    assert_query_success(app, snapshot, query)

##__________________________________________________________________||
