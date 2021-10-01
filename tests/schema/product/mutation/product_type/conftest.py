import pytest

import datetime

from acondbs.db.sa import sa
from acondbs.models import (
    ProductType,
    Product,
    FieldType,
    Field,
    TypeFieldAssociation,
)
from acondbs import ops


##__________________________________________________________________||
@pytest.fixture
def app(app_users):

    y = app_users

    with y.app_context():

        # fmt: off
        field_contact = ops.create_field(field_id=1, name="contact", type_=FieldType.UnicodeText)
        field_produced_by = ops.create_field(field_id=2, name="produced_by", type_=FieldType.UnicodeText)
        field_date_produced = ops.create_field(field_id=3, name="date_produced", type_=FieldType.Date)
        # fmt: on

        fields = [field_contact, field_produced_by, field_date_produced]

        # create product types
        # Map = ProductType(
        #     type_id=1,
        #     name="map",
        #     order=2,
        #     indef_article="a",
        #     singular="map",
        #     plural="maps",
        #     icon="mdi-map",
        #     fields=[TypeFieldAssociation(field=f) for f in fields],
        # )
        Map = ops.create_product_type(
            dict(
                type_id=1,
                name="map",
                order=2,
                indef_article="a",
                singular="map",
                plural="maps",
                icon="mdi-map",
            )
        )
        Map.fields = [TypeFieldAssociation(field=f) for f in fields]
        Beam = ProductType(
            type_id=2,
            name="beam",
            order=1,
            indef_article="a",
            singular="beam",
            plural="beams",
            icon="mdi-spotlight-beam",
            fields=[TypeFieldAssociation(field=f) for f in fields],
        )

        # create products
        map1 = Product(  # noqa: F841
            name="map1", date_produced=datetime.date(2020, 2, 1), type_=Map
        )
        map2 = Product(  # noqa: F841
            name="map2", date_produced=datetime.date(2020, 5, 10), type_=Map
        )
        map3 = Product(  # noqa: F841
            name="map3", date_produced=datetime.date(2020, 3, 3), type_=Map
        )

        sa.session.add(Map)
        sa.session.add(Beam)
        sa.session.commit()
    yield y


##__________________________________________________________________||
