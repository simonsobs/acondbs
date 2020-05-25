import pytest

from acondbs import create_app
from acondbs.db.ops import define_tables

from acondbs.db.sa import sa
from acondbs.models import Product, ProductRelation, ProductRelationType

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

    #                              +--------+
    #               --(child)-->   |        |
    #                    |         | child1 |
    #  +---------+  <-(parent)--   |        |
    #  |         |                 +--------+
    #  | parent1 |
    #  |         |                 +--------+
    #  +---------+  --(child)-->   |        |
    #                    |         | child2 |
    #               <-(parent)--   |        |
    #                              +--------+


    relation_type_parent = ProductRelationType(name='parent')
    relation_type_child = ProductRelationType(name='child')
    relation_type_parent.reverse = relation_type_child
    relation_type_child.reverse = relation_type_parent

    parent1 = Product(name="parent1")
    child1 = Product(name="child1")
    child2 = Product(name="child2")

    # parent1 --(child)--> child1
    relation_parent1_to_child1 = ProductRelation()
    relation_parent1_to_child1.type_ = relation_type_child
    relation_parent1_to_child1.self_ = parent1
    relation_parent1_to_child1.other = child1

    # child1 --(parent)--> parent1
    relation_child1_to_parent1 = ProductRelation()
    relation_child1_to_parent1.type_ = relation_type_parent
    relation_child1_to_parent1.self_ = child1
    relation_child1_to_parent1.other = parent1

    relation_parent1_to_child1.reverse = relation_child1_to_parent1
    relation_child1_to_parent1.reverse = relation_parent1_to_child1

    # parent1 --(child)--> child2
    relation_parent1_to_child2 = ProductRelation()
    relation_parent1_to_child2.type_ = relation_type_child
    relation_parent1_to_child2.self_ = parent1
    relation_parent1_to_child2.other = child2

    # child2 --(parent)--> parent1
    relation_child2_to_parent1 = ProductRelation()
    relation_child2_to_parent1.type_ = relation_type_parent
    relation_child2_to_parent1.self_ = child2
    relation_child2_to_parent1.other = parent1

    relation_parent1_to_child2.reverse = relation_child2_to_parent1
    relation_child2_to_parent1.reverse = relation_parent1_to_child2

    # commit
    with y.app_context():
        sa.session.add(parent1)
        sa.session.commit()
    yield y

# __________________________________________________________________||
