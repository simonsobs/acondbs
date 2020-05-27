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
    parent_type = ProductRelationType(type_id=1, name='parent')
    child_type = ProductRelationType(type_id=2, name='child')
    parent_type.reverse = child_type

    # create products
    type_ = ProductType(name='robot')
    parent1 = Product(product_id=1, name="parent1", type_=type_)
    child1 = Product(product_id=2, name="child1", type_=type_)

    parent2 = Product(product_id=3, name="parent2", type_=type_)
    child2 = Product(product_id=4, name="child12", type_=type_)

    # create a relation (to test duplicate)
    relation_parent2_to_child2 = ProductRelation()
    relation_parent2_to_child2.type_ = child_type
    relation_parent2_to_child2.self_ = parent2
    relation_parent2_to_child2.other = child2

    with y.app_context():
        sa.session.add(parent_type)
        sa.session.add(parent1)
        sa.session.add(child1)
        sa.session.commit()
    yield y

##__________________________________________________________________||
params = [
    pytest.param(
        textwrap.dedent('''
          mutation m {
            createProductRelation(
              input: {
                typeId: 2,
                selfProductId: 1,
                otherProductId: 2
              }
              ) {
              productRelation {
                ...fragmentProductRelation
              }
            }
          }
        ''') + FRAGMENT_PRODUCT_RELATION,
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
        textwrap.dedent('''
          mutation m {
            createProductRelation(
              input: {
                typeId: 20,
                selfProductId: 1,
                otherProductId: 2
              }
              ) {
              productRelation {
                ...fragmentProductRelation
              }
            }
          }
        ''') + FRAGMENT_PRODUCT_RELATION,
        textwrap.dedent('''
        {
          allProductRelations {
            ...fragmentProductRelationConnection
          }
        }
         ''') + FRAGMENT_PRODUCT_RELATION_CONNECTION,
        id='error-type_id-nonexistent'
    ),
    pytest.param(
        textwrap.dedent('''
          mutation m {
            createProductRelation(
              input: {
                typeId: 2,
                selfProductId: 10,
                otherProductId: 2
              }
              ) {
              productRelation {
                ...fragmentProductRelation
              }
            }
          }
        ''') + FRAGMENT_PRODUCT_RELATION,
        textwrap.dedent('''
        {
          allProductRelations {
            ...fragmentProductRelationConnection
          }
        }
         ''') + FRAGMENT_PRODUCT_RELATION_CONNECTION,
        id='error-self_product_id-nonexistent'
    ),
    pytest.param(
        textwrap.dedent('''
          mutation m {
            createProductRelation(
              input: {
                typeId: 2,
                selfProductId: 1,
                otherProductId: 20
              }
              ) {
              productRelation {
                ...fragmentProductRelation
              }
            }
          }
        ''') + FRAGMENT_PRODUCT_RELATION,
        textwrap.dedent('''
        {
          allProductRelations {
            ...fragmentProductRelationConnection
          }
        }
         ''') + FRAGMENT_PRODUCT_RELATION_CONNECTION,
        id='error-otheer_product_id-nonexistent'
    ),
    pytest.param(
        textwrap.dedent('''
          mutation m {
            createProductRelation(
              input: {
                typeId: 2,
                selfProductId: 3,
                otherProductId: 4
              }
              ) {
              productRelation {
                ...fragmentProductRelation
              }
            }
          }
        ''') + FRAGMENT_PRODUCT_RELATION,
        textwrap.dedent('''
        {
          allProductRelations {
            ...fragmentProductRelationConnection
          }
        }
         ''') + FRAGMENT_PRODUCT_RELATION_CONNECTION,
        id='error-duplicate'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation_error(app, snapshot, mutation, query, mock_request_backup_db)

##__________________________________________________________________||
