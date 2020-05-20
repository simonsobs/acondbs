import pytest
import unittest.mock as mock

from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          mutation m {
            createProduct(input: {
              typeId: 1,
              name: "product1",
              contact: "contact-person",
              dateProduced: "2020-02-20",
              producedBy: "producer",
              postedBy: "poster",
              note: "- Item 1"
              paths: [
                "/path/to/new/product1",
                "/another/location/of/product1"
              ]
            }) { product { name } }
          }
        ''',
        '''
          {
            product(name: "product1") {
              productType { name }
              name contact
              datePosted postedBy
              dateProduced producedBy
              dateUpdated updatedBy
              note
              paths { edges { node { path } } }
            }
          }
        ''',
        id='createProduct-all-options'
    ),
    pytest.param(
        '''
          mutation m {
            createProduct(input: {
              typeId: 1,
              name: "product1",
              producedBy: "pwg-pmn"
            }) { product { name } }
          }
        ''',
        '''
          {
            product(name: "product1") {
              productType { name }
              name contact
              datePosted postedBy
              dateProduced producedBy
              dateUpdated updatedBy
              note
              paths { edges { node { path } } }
            }
          }
        ''',
        id='createProduct-selective-options'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_success(app, snapshot, mutation, query, mock_request_backup_db):
    client = Client(schema)
    with app.app_context():
        result = client.execute(mutation)
        assert 'errors' not in result
        snapshot.assert_match(result)
    with app.app_context():
        result = client.execute(query)
        assert 'errors' not in result
        snapshot.assert_match(result)
    assert 1 == mock_request_backup_db.call_count

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          mutation m {
            createProduct(input: {
              producedBy: "pwg-pmn"
              paths: [
                "/path/to/new/product1",
                "/another/location/of/product1"
              ]
            }) { product { name } }
          }
        ''',
        '''
          {
            allProducts {
              edges {
                node {
                  productId
                  name
                }
              }
            }
            allProductFilePaths {
              edges {
                node {
                  path
                  productId
                }
              }
            }
          }
        ''',
        id='createProduct-error-no-name'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db):
    client = Client(schema)
    with app.app_context():
        result = client.execute(mutation)
        assert 'errors' in result
        snapshot.assert_match(result)
    with app.app_context():
        result = client.execute(query)
        assert 'errors' not in result
        snapshot.assert_match(result)
    assert 0 == mock_request_backup_db.call_count

##__________________________________________________________________||
