import pytest
import textwrap

from acondbs import create_app
from acondbs.db.ops import define_tables

from acondbs.db.sa import sa
from acondbs.models import (
    ProductType,
    Product,
    ProductRelationType,
    ProductRelation
    )

from ..funcs import assert_mutation_success, assert_mutation_error

from ..gql import (
    FRAGMENT_PRODUCT_RELATION,
    FRAGMENT_PRODUCT_RELATION_CONNECTION
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

    # create relation types
    parent_type = ProductRelationType(name='parent')
    child_type = ProductRelationType(name='child')
    parent_type.reverse = child_type

    # create products
    type_ = ProductType(name='robot')
    parent1 = Product(name="parent1", type_=type_)
    child1 = Product(name="child1", type_=type_)

    # create a relation
    relation = ProductRelation(relation_id=1)
    relation.type_ = child_type
    relation.self_ = parent1
    relation.other = child1

    with y.app_context():
        sa.session.add(relation)
        sa.session.commit()
    yield y

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          mutation m {
            deleteProductRelation(relationId: 1) { ok }
          }
        ''',
        textwrap.dedent('''
        {
          allProductRelations {
            ...fragmentProductRelationConnection
          }
        }
         ''') + FRAGMENT_PRODUCT_RELATION_CONNECTION,
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
            deleteProductRelation(relationId: 120) { ok }
          }
        ''',
        textwrap.dedent('''
        {
          allProductRelations {
            ...fragmentProductRelationConnection
          }
        }
         ''') + FRAGMENT_PRODUCT_RELATION_CONNECTION,
        id='error-nonexistent'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation_error(app, snapshot, mutation, query, mock_request_backup_db)

##__________________________________________________________________||