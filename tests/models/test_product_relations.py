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
    #                              | child1 |
    #  +---------+  <-(parent)--   |        |
    #  |         |                 +--------+
    #  | parent1 |
    #  |         |                 +--------+
    #  +---------+  --(child)-->   |        |
    #                              | child2 |
    #               <-(parent)--   |        |
    #                              +--------+


    relation_type_parent = ProductRelationType(name='parent')
    relation_type_child = ProductRelationType(name='child')

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
def test_relations(app):

    with app.app_context():
        parent1 = Product.query.filter_by(name='parent1').first()
        child1 = Product.query.filter_by(name='child1').first()
        child2 = Product.query.filter_by(name='child2').first()

        assert 2 == len(parent1.relations)
        assert 1 == len(child1.relations)
        assert 1 == len(child2.relations)

        assert 'child' == parent1.relations[0].type_.name
        assert 'child' == parent1.relations[1].type_.name
        assert 'parent' == child1.relations[0].type_.name
        assert 'parent' == child2.relations[0].type_.name

        assert child1 is parent1.relations[0].other
        assert child2 is parent1.relations[1].other

        assert parent1 is child1.relations[0].other
        assert parent1 is child2.relations[0].other

        assert parent1.relations[0] is child1.relations[0].reverse
        assert parent1.relations[0].reverse is child1.relations[0]

        assert parent1.relations[1] is child2.relations[0].reverse
        assert parent1.relations[1].reverse is child2.relations[0]

def test_example_how_to_query(app):

    with app.app_context():

        parent1 = Product.query.filter_by(name='parent1').first()
        child1 = Product.query.filter_by(name='child1').first()
        child2 = Product.query.filter_by(name='child2').first()

        # Product relations with the type name "child"
        relations = ProductRelation.query.join(ProductRelationType).filter(ProductRelationType.name=='child').all()
        assert ['child', 'child'] == [r.type_.name for r in relations]

        # Products with "parent"
        products = Product.query.join(ProductRelation, (Product.product_id == ProductRelation.self_product_id)).join(ProductRelationType).filter(ProductRelationType.name=='parent').all()
        assert [child1, child2] == products

        # Products with "child"
        products = Product.query.join(ProductRelation, (Product.product_id == ProductRelation.self_product_id)).join(ProductRelationType).filter(ProductRelationType.name=='child').all()
        assert [parent1] == products

# __________________________________________________________________||
