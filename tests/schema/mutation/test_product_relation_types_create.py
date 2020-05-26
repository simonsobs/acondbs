import pytest
import textwrap

from acondbs import create_app
from acondbs.db.ops import define_tables

from acondbs.db.sa import sa
from acondbs.models import ProductRelationType

from .funcs import assert_mutation_success, assert_mutation_error

from ..gql import (
    FRAGMENT_PRODUCT_RELATION_TYPE,
    FRAGMENT_PRODUCT_RELATION_TYPE_CONNECTION
    )

##__________________________________________________________________||
@pytest.fixture
def app_empty():
    database_uri ="sqlite:///:memory:"
    y = create_app(SQLALCHEMY_DATABASE_URI=database_uri)
    with y.app_context():
        define_tables()
    yield y

@pytest.fixture
def app(app_empty):

    y = app_empty

    #
    #  +--------+                +-------+
    #  |        | --(reverse)->  |       |
    #  | parent |                | child |
    #  |        | <-(reverse)--  |       |
    #  +--------+                +-------+
    #

    parent = ProductRelationType(name='parent')
    child = ProductRelationType(name='child')
    parent.reverse = child

    with y.app_context():
        sa.session.add(parent)
        sa.session.commit()
    yield y

##__________________________________________________________________||
params = [
    pytest.param(
        textwrap.dedent('''
          mutation m {
            createProductRelationType(input: {
              name: "plaintiff",
              indefArticle: "a",
              singular: "plaintiff",
              plural: "plaintiffs"
              }) {
              productRelationType {
                ...fragmentProductRelationType
              }
            }
          }
        ''') + FRAGMENT_PRODUCT_RELATION_TYPE,
        textwrap.dedent('''
        {
          allProductRelationTypes {
            ...fragmentProductRelationTypeConnection
          }
        }
         ''') + FRAGMENT_PRODUCT_RELATION_TYPE_CONNECTION,
        id='create'
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
        textwrap.dedent('''
        {
          allProductRelationTypes {
            ...fragmentProductRelationTypeConnection
          }
        }
        ''') + FRAGMENT_PRODUCT_RELATION_TYPE_CONNECTION,
        id='error-already-exist'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation_error(app, snapshot, mutation, query, mock_request_backup_db)

##__________________________________________________________________||
