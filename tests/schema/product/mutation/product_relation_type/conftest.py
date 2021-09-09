import pytest

import datetime

from acondbs.db.sa import sa
from acondbs.models import ProductType, Product, ProductRelationType, ProductRelation


##__________________________________________________________________||
@pytest.fixture
def app(app_users):

    y = app_users

    # Relation types:
    #   parent <-> child
    #   plaintiff <-> defendant

    # Relations:
    #   map1 -> beam1
    #     |        |
    #     +--------+---> beam2

    # create relation types
    Parent = ProductRelationType(
        type_id=1, name="parent", indef_article="a", singular="parent", plural="parents"
    )
    Parent.reverse = ProductRelationType(
        type_id=2, name="child", indef_article="a", singular="child", plural="children"
    )
    Plaintiff = ProductRelationType(
        type_id=3,
        name="plaintiff",
        indef_article="a",
        singular="plaintiff",
        plural="plaintiffs",
    )
    Plaintiff.reverse = ProductRelationType(
        type_id=4,
        name="defendant",
        indef_article="a",
        singular="defendant",
        plural="defendants",
    )

    # create product types
    Map = ProductType(type_id=1, name="map")
    Beam = ProductType(type_id=2, name="beam")

    # create products
    map1 = Product(
        product_id=1, name="map1", date_produced=datetime.date(2020, 2, 1), type_=Map
    )
    beam1 = Product(
        product_id=4, name="beam1", date_produced=datetime.date(2020, 2, 5), type_=Beam
    )
    beam2 = Product(
        product_id=5, name="beam2", date_produced=datetime.date(2020, 3, 4), type_=Beam
    )

    # create relations
    relation1 = ProductRelation(type_=Parent, self_=beam1, other=map1)  # noqa: F841
    relation2 = ProductRelation(type_=Parent, self_=beam2, other=map1)  # noqa: F841
    relation3 = ProductRelation(type_=Parent, self_=beam2, other=beam1)  # noqa: F841

    with y.app_context():
        sa.session.add(Parent)
        sa.session.add(Plaintiff)
        sa.session.commit()
    yield y


##__________________________________________________________________||
