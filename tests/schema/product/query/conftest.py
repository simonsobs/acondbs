import pytest

import datetime

from acondbs.db.sa import sa
from acondbs.models import (
    ProductType,
    Product,
    ProductFilePath,
    ProductRelationType,
    ProductRelation,
    AttributeDate,
)


##__________________________________________________________________||
@pytest.fixture
def app(app_users):

    y = app_users

    # Relation types:
    #   parent <-> child
    #   plaintiff <-> defendant

    # Products and Relations:
    #   map1 -> beam1
    #     |        |
    #     +--------+---> beam2
    #
    #   map2
    #   map3

    # create relation types
    Parent = ProductRelationType(
        type_id=1,
        name="parent",
        indef_article="a",
        singular="parent",
        plural="parents",
    )
    Parent.reverse = ProductRelationType(
        type_id=2,
        name="child",
        indef_article="a",
        singular="child",
        plural="children",
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
    Map = ProductType(
        type_id=1,
        name="map",
        order=2,
        indef_article="a",
        singular="map",
        plural="maps",
        icon="mdi-map",
    )
    Beam = ProductType(
        type_id=2,
        name="beam",
        order=1,
        indef_article="a",
        singular="beam",
        plural="beams",
        icon="mdi-spotlight-beam",
    )

    # create products
    map1 = Product(
        product_id=1,
        name="map1",
        date_produced=datetime.date(2020, 2, 1),
        type_=Map,
        attributes_date=[
            AttributeDate(
                name="date_produced", value=datetime.date(2020, 2, 1)
            )
        ],
    )
    map2 = Product(
        product_id=2,
        name="map2",
        date_produced=datetime.date(2020, 2, 10),
        type_=Map,
        attributes_date=[
            AttributeDate(
                name="date_produced", value=datetime.date(2020, 2, 10)
            )
        ],
    )
    map3 = Product(
        product_id=3,
        name="map3",
        date_produced=datetime.date(2020, 3, 19),
        type_=Map,
        attributes_date=[
            AttributeDate(
                name="date_produced", value=datetime.date(2020, 3, 19)
            )
        ],
    )
    beam1 = Product(
        product_id=4,
        name="beam1",
        date_produced=datetime.date(2020, 2, 5),
        type_=Beam,
        attributes_date=[
            AttributeDate(
                name="date_produced", value=datetime.date(2020, 2, 5)
            )
        ],
    )
    beam2 = Product(
        product_id=5,
        name="beam2",
        date_produced=datetime.date(2020, 3, 4),
        type_=Beam,
        attributes_date=[
            AttributeDate(
                name="date_produced", value=datetime.date(2020, 3, 4)
            )
        ],
    )

    # add paths
    map1.paths = [
        ProductFilePath(path="site1:/path/to/map1", note="sample comment"),
        ProductFilePath(path="site2:/another/way/map1"),
    ]

    map2.paths = [
        ProductFilePath(path="site1:/path/to/map2"),
    ]

    map3.paths = [
        ProductFilePath(path="site1:/path/to/map3"),
        ProductFilePath(path="site2:/another/way/map3"),
    ]

    beam1.paths = [
        ProductFilePath(path="site1:/path/to/beam1"),
        ProductFilePath(path="site2:/another/way/beam1"),
    ]

    beam2.paths = [
        ProductFilePath(path="site1:/path/to/beam2"),
    ]

    # create relations
    relation1 = ProductRelation(
        relation_id=2, type_=Parent, self_=beam1, other=map1
    )
    relation2 = ProductRelation(
        relation_id=4, type_=Parent, self_=beam2, other=map1
    )
    relation3 = ProductRelation(
        relation_id=5, type_=Parent, self_=beam2, other=beam1
    )

    with y.app_context():
        sa.session.add(Map)
        sa.session.add(Beam)
        sa.session.add(relation1)
        sa.session.add(relation2)
        sa.session.add(relation3)
        sa.session.commit()
    yield y


##__________________________________________________________________||
