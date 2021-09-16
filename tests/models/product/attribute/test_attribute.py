import datetime

from acondbs.models import Product


##__________________________________________________________________||
def test_one(app):
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
