import pytest

import datetime

from acondbs.db.sa import sa
from acondbs.models import (
    ProductType,
    Product,
    ProductFilePath,
    ProductRelationType,
    ProductRelation,
    GitHubUser,
    GitHubToken,
    FieldType,
    Field,
    TypeFieldAssociation,
    AttributeDate,
)


##__________________________________________________________________||
@pytest.fixture
def app(app_empty):

    y = app_empty

    user1 = GitHubUser(login="user1", git_hub_id="04:User1")
    token1 = GitHubToken(
        token="39d86487d76a84087f1da599c872dac4473e5f07", scope="", user=user1
    )

    with y.app_context():
        sa.session.add(user1)
        sa.session.add(token1)
        sa.session.commit()

    # map1 -> beam1
    #   |        |
    #   +--------+---> beam2
    #
    # map2
    # map3

    # create relation types
    Parent = ProductRelationType(type_id=1, name="parent")
    Parent.reverse = ProductRelationType(type_id=2, name="child")

    # create fields
    field_contact = Field(name="contact", type_=FieldType.UnicodeText)
    field_produced_by = Field(name="produced_by", type_=FieldType.UnicodeText)
    field_date_produced = Field(name="date_produced", type_=FieldType.Date)
    fields = [field_contact, field_produced_by, field_date_produced]

    # create product types
    Map = ProductType(type_id=1, name="map")
    Map.fields = [TypeFieldAssociation(field=f) for f in fields]
    Beam = ProductType(type_id=2, name="beam")
    Beam.fields = [TypeFieldAssociation(field=f) for f in fields]

    # create products
    map1 = Product(
        product_id=1,
        name="map1",
        date_produced=datetime.date(2020, 2, 1),
        type_=Map,
        attributes_date=[
            AttributeDate(
                name="date_produced",
                field=field_date_produced,
                value=datetime.date(2020, 2, 1),
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
                name="date_produced",
                field=field_date_produced,
                value=datetime.date(2020, 2, 10),
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
                name="date_produced",
                field=field_date_produced,
                value=datetime.date(2020, 3, 19),
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
                name="date_produced",
                field=field_date_produced,
                value=datetime.date(2020, 2, 5),
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
                name="date_produced",
                field=field_date_produced,
                value=datetime.date(2020, 3, 4),
            )
        ],
    )

    # add paths
    map1.paths = [
        ProductFilePath(path="site1:/path/to/map1"),
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
    relation1 = ProductRelation(type_=Parent, self_=beam1, other=map1)
    relation2 = ProductRelation(type_=Parent, self_=beam2, other=map1)
    relation3 = ProductRelation(type_=Parent, self_=beam2, other=beam1)

    with y.app_context():
        sa.session.add(Map)
        sa.session.add(Beam)
        sa.session.add(relation1)
        sa.session.add(relation2)
        sa.session.add(relation3)
        sa.session.commit()
    yield y


##__________________________________________________________________||
