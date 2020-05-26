import pytest

from .funcs import assert_query_success

##__________________________________________________________________||
params = [
    pytest.param(
        '''
        { product(productId: 1001) { name } }
         ''',
        id='product_id'
    ),
    pytest.param(
        '''
        { product(productId: 2001) { name } }
         ''',
        id='product_id-nonexistent'
    ),
    pytest.param(
        '''
        { product(name: "lat20190213") { productId } }
         ''',
        id='name'
    ),
    pytest.param(
        '''
        { product(productId: 1001, name: "lat20190213") { productId } }
         ''',
        id='product_id-name'
    ),
    pytest.param(
        '''
        { product(productId: 1002, name: "lat20190213") { productId } }
         ''',
        id='product_id-name-nonexistent'
    ),
    pytest.param(
        '''
        { product(typeId: 1, name: "lat20190213") { productId } }
         ''',
        id='type_id-name'
    ),
]

##__________________________________________________________________||
@pytest.mark.parametrize('query', params)
def test_schema(app, snapshot, query):
    assert_query_success(app, snapshot, query)

##__________________________________________________________________||
