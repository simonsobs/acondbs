import pytest

from ..funcs import assert_mutation_success, assert_mutation_error

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
              type_ { name }
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
              type_ { name }
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
    pytest.param(
        '''
          mutation m {
            createProduct(input: {
              typeId: 2,
              name: "lat20190213",
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
            product(typeId: 2, name: "lat20190213") {
              type_ { name }
              name contact
              datePosted postedBy
              dateProduced producedBy
              dateUpdated updatedBy
              note
              paths { edges { node { path } } }
            }
          }
        ''',
        id='createProduct-error-the-same-name-different-type'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_success(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation_success(app, snapshot, mutation, query, mock_request_backup_db)

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          mutation m {
            createProduct(input: {
              typeId: 1,
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
    pytest.param(
        '''
          mutation m {
            createProduct(input: {
              typeId: 1,
              name: "lat20190213",
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
        id='createProduct-error-the-same-type-and-name'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation_error(app, snapshot, mutation, query, mock_request_backup_db)

##__________________________________________________________________||
