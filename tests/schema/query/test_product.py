import pytest
import textwrap

from .funcs import assert_query_success

productFragment = '''
fragment productFragment on Product {
  productId
  typeId
  type_ {
    typeId
    name
  }
  name
  contact
  dateProduced
  producedBy
  datePosted
  postedBy
  dateUpdated
  updatedBy
  paths {
    edges {
      node {
        pathId
        path
        note
      }
    }
  }
  relations {
    edges {
      node {
        relationId
        typeId
        type_ {
          typeId
          name
        }
        otherProductId
        other {
          productId
          typeId
          type_ {
            typeId
            name
          }
          name
        }
        reverseRelationId
        reverse {
          relationId
          typeId
          type_ {
            typeId
            name
          }
        }
      }
    }
  }
  note
}
'''

print(productFragment)

##__________________________________________________________________||
params = [
    pytest.param(
        textwrap.dedent('''
        {
          product(productId: 1001) {
            ...productFragment
          }
        }
         ''') + productFragment,
        id='product_id'
    ),
    pytest.param(
        textwrap.dedent('''
        { product(productId: 2001) {
            ...productFragment
          }
        }
         ''') + productFragment,
        id='product_id-nonexistent'
    ),
    pytest.param(
        textwrap.dedent('''
        { product(name: "lat20190213") {
            ...productFragment
          }
        }
         ''') + productFragment,
        id='name'
    ),
    pytest.param(
        textwrap.dedent('''
        { product(productId: 1001, name: "lat20190213") {
            ...productFragment
          }
        }
         ''') + productFragment,
        id='product_id-name'
    ),
    pytest.param(
        textwrap.dedent('''
        { product(productId: 1002, name: "lat20190213") {
            ...productFragment
          }
        }
         ''') + productFragment,
        id='product_id-name-nonexistent'
    ),
    pytest.param(
        textwrap.dedent('''
        { product(typeId: 1, name: "lat20190213") {
            ...productFragment
          }
        }
         ''') + productFragment,
        id='type_id-name'
    ),
]

##__________________________________________________________________||
@pytest.mark.parametrize('query', params)
def test_schema(app, snapshot, query):
    assert_query_success(app, snapshot, query)

##__________________________________________________________________||
