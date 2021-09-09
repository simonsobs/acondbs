import pytest

import datetime

from acondbs.db.sa import sa
from acondbs.models import ProductType, Product


##__________________________________________________________________||
@pytest.fixture
def app(app_users):

    y = app_users

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
    map1 = Product(  # noqa: F841
        name="map1", date_produced=datetime.date(2020, 2, 1), type_=Map
    )
    map2 = Product(  # noqa: F841
        name="map2", date_produced=datetime.date(2020, 5, 10), type_=Map
    )
    map3 = Product(  # noqa: F841
        name="map3", date_produced=datetime.date(2020, 3, 3), type_=Map
    )

    with y.app_context():
        sa.session.add(Map)
        sa.session.add(Beam)
        sa.session.commit()
    yield y


##__________________________________________________________________||
