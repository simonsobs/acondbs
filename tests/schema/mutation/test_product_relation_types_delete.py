import pytest
import textwrap

from ..funcs import assert_mutation_success, assert_mutation_error

from ..gql import FRAGMENT_PRODUCT_RELATION_TYPE_CONNECTION

##__________________________________________________________________||
params = [
    pytest.param(
        '''
        mutation m {
          deleteProductRelationType(typeId: 3) { ok }
        }
         ''',
        textwrap.dedent('''
        {
          allProductRelationTypes {
            ...fragmentProductRelationTypeConnection
          }
        }
         ''') + FRAGMENT_PRODUCT_RELATION_TYPE_CONNECTION,
        id='delete'
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
          deleteProductRelationType(typeId: 512) { ok }
        }
         ''',
        textwrap.dedent('''
        {
          allProductRelationTypes {
            ...fragmentProductRelationTypeConnection
          }
        }
         ''') + FRAGMENT_PRODUCT_RELATION_TYPE_CONNECTION,
        id='error-nonexistent'
    ),
    pytest.param(
        '''
        mutation m {
          deleteProductRelationType(typeId: 1) { ok }
        }
         ''',
        textwrap.dedent('''
        {
          allProductRelationTypes {
            ...fragmentProductRelationTypeConnection
          }
        }
         ''') + FRAGMENT_PRODUCT_RELATION_TYPE_CONNECTION,
        id='error-unempty'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation_error(app, snapshot, mutation, query, mock_request_backup_db)

##__________________________________________________________________||
