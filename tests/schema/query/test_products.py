import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
        { allProducts(first: 2) {
             edges { node { name } }
           } }
         ''',
        id='allProductsFirstTwo'
    ),
    pytest.param(
        '''
        { allProducts(first: 2, sort: DATE_POSTED_DESC) {
             edges { node { name } }
           } }
         ''',
        id='allProductsFirstTwoSort'
    ),
    pytest.param(
        '''
        { product(productId: 1001) { name } }
         ''',
        id='productByProductID'
    ),
    pytest.param(
        '''
        { product(productId: 2001) { name } }
         ''',
        id='productByProductID-nonexistent'
    ),
    pytest.param(
        '''
        { product(name: "lat20190213") { productId } }
         ''',
        id='productByName'
    ),
]

@pytest.mark.parametrize('query', params)
def test_schema(app, snapshot, query):
    client = Client(schema)
    with app.app_context():
        result = client.execute(query)
        assert 'errors' not in result
        snapshot.assert_match(result)

##__________________________________________________________________||
