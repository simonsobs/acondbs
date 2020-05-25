import pytest

from itertools import permutations

from acondbs.db.sa import sa
from acondbs.models import Product, ProductRelation, ProductRelationType

# __________________________________________________________________||
params = list(permutations([1, 2, 3]))
# i.e., [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

ids = ['-'.join(['{}'.format(e) for e in p]) for p in params]
# i.e., ['1-2-3', '1-3-2', '2-1-3', '2-3-1', '3-1-2', '3-2-1']

@pytest.mark.parametrize('perm', params, ids=ids)
def test_permutations(app_empty, perm):

    app = app_empty

    #
    # +---------+                 +--------+
    # |         |  --(child)-->   |        |
    # | parent1 |       |         | child1 |
    # |         |  <-(parent)--   |        |
    # +---------+                 +--------+
    #

    relation_type_parent = ProductRelationType(name='parent')
    relation_type_child = ProductRelationType(name='child')
    relation_type_parent.reverse = relation_type_child
    relation_type_child.reverse = relation_type_parent

    parent1 = Product(name="parent1")
    child1 = Product(name="child1")

    relation_parent1_to_child1 = ProductRelation()

    # set 'type_', 'self_', 'other' in different orders
    # each triggers an event in which a reverse is automatically set
    for p in perm:
        if p == 1:
            relation_parent1_to_child1.type_ = relation_type_child
        elif p == 2:
            relation_parent1_to_child1.self_ = parent1
        elif p == 3:
            relation_parent1_to_child1.other = child1

    with app.app_context():
        sa.session.add(parent1)
        sa.session.commit()

    with app.app_context():
        parent1 = Product.query.filter_by(name='parent1').first()
        child1 = Product.query.filter_by(name='child1').first()

        assert 1 == len(parent1.relations)
        assert 1 == len(child1.relations)

        assert 'child' == parent1.relations[0].type_.name
        assert 'parent' == child1.relations[0].type_.name

        assert child1 is parent1.relations[0].other

        assert parent1 is child1.relations[0].other

        assert parent1.relations[0] is child1.relations[0].reverse
        assert parent1.relations[0].reverse is child1.relations[0]

# __________________________________________________________________||
