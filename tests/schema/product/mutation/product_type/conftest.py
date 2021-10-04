import pytest

import datetime

from acondbs.db.sa import sa
from acondbs.models import (
    Product,
    FieldType,
)
from acondbs import ops


##__________________________________________________________________||
@pytest.fixture
def app(app_users):

    y = app_users

    with y.app_context():
        # fmt: off
        ops.create_field(field_id=1, name="contact", type_=FieldType.UnicodeText)
        ops.create_field(field_id=2, name="produced_by", type_=FieldType.UnicodeText)
        ops.create_field(field_id=3, name="date_produced", type_=FieldType.Date)
        ops.create_field(field_id=4, name="field_four", type_=FieldType.UnicodeText)
        ops.create_field(field_id=5, name="field_five", type_=FieldType.UnicodeText)
        # fmt: on
        ops.commit()

    with y.app_context():

        Map = ops.create_product_type(
            type_id=1,
            name="map",
            order=2,
            indef_article="a",
            singular="map",
            plural="maps",
            icon="mdi-map",
            field_ids=[1, 2, 3],
        )
        Beam = ops.create_product_type(
            type_id=2,
            name="beam",
            order=1,
            indef_article="a",
            singular="beam",
            plural="beams",
            icon="mdi-spotlight-beam",
            field_ids=[1, 2, 3],
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
