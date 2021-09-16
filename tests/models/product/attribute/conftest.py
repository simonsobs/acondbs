import pytest

import datetime

from acondbs.db.sa import sa
from acondbs.models import (
    ProductType,
    Product,
    AttributeText,
    AttributeDate,
    AttributeDateTime,
)


##__________________________________________________________________||
@pytest.fixture
def app(app_empty):

    y = app_empty

    type1 = ProductType(name="type1")

    product1 = Product(name="product1", type_=type1)

    AttributeText(product=product1, name="note", value="This is a test")
    AttributeDate(
        product=product1,
        name="date_produced",
        value=datetime.date(2019, 2, 23),
    )
    AttributeDateTime(
        product=product1,
        name="time_posted",
        value=datetime.datetime(2019, 2, 24, 9, 10, 25),
    )

    with y.app_context():
        sa.session.add(product1)
        sa.session.commit()

    yield y


##__________________________________________________________________||
