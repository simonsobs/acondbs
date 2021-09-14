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
def test_one(app_empty):
    app = app_empty

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

    with app.app_context():
        sa.session.add(product1)
        sa.session.commit()

    with app.app_context():
        product1 = Product.query.filter_by(name="product1").one_or_none()
        assert product1 is not None
        note = product1.attributes_text[0]
        assert "note" == note.name
        assert "This is a test" == note.value
        date_produced = product1.attributes_date[0]
        assert "date_produced" == date_produced.name
        assert datetime.date(2019, 2, 23) == date_produced.value
        time_posted = product1.attributes_date_time[0]
        assert "time_posted" == time_posted.name
        assert datetime.datetime(2019, 2, 24, 9, 10, 25) == time_posted.value


##__________________________________________________________________||
