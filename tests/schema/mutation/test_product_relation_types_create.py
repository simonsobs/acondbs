import pytest

from .funcs import assert_mutation_success, assert_mutation_error

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          mutation m {
            createProductRelationType(input: {
              name: "proctor",
              indefArticle: "a",
              singular: "proctor",
              plural: "proctors",
            }) { productRelationType { name } }
          }
        ''',
        '''
          {
            productRelationType(name: "proctor") {
              name
              indefArticle
              singular
              plural
            }
          }
        ''',
        id='createProductRelationType'
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
            createProductRelationType(input: {
              name: "parent",
            }) { productType { name } }
          }
        ''',
        '''
          {
            allProductRelationTypes {
              edges {
                node {
                  name
                }
              }
            }
          }
        ''',
        id='createProduct-error-already-exist'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation_error(app, snapshot, mutation, query, mock_request_backup_db)

##__________________________________________________________________||
