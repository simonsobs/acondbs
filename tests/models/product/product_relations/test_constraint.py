import pytest
from flask import Flask
from sqlalchemy import exc

from acondbs.db.sa import sa
from acondbs.models import Product, ProductRelation, ProductRelationType


def test_constraint(app: Flask) -> None:
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

    # try to duplicate relation
    with app.app_context():
        parent1 = Product.query.filter_by(name='parent1').first()
        child1 = Product.query.filter_by(name='child1').first()
        type_ = ProductRelationType.query.filter_by(name='child').first()

        relation = ProductRelation()
        relation.type_ = type_
        relation.self_ = parent1
        relation.other = child1

        with pytest.raises(exc.IntegrityError):
            sa.session.commit()
