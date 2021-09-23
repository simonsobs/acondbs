import datetime
from sqlalchemy.orm import aliased

import pytest

from acondbs.db.sa import sa

from acondbs.models import (
    Product,
    ProductType,
    FieldType,
    Field,
    TypeFieldAssociation,
    AttributeUnicodeText,
    AttributeBoolean,
    AttributeInteger,
    AttributeFloat,
    AttributeDate,
    AttributeDateTime,
    AttributeTime
)


##__________________________________________________________________||
params = [
    pytest.param(FieldType.UnicodeText, AttributeUnicodeText, "value1 値１", id='UnicodeText'),  # fmt: skip
    pytest.param(FieldType.Boolean, AttributeBoolean, True, id='Boolean'),  # fmt: skip
    pytest.param(FieldType.Integer, AttributeInteger, -512442, id='Integer'),  # fmt: skip
    pytest.param(FieldType.Float, AttributeFloat, 3.14592613, id='Float'),  # fmt: skip
    pytest.param(FieldType.Date, AttributeDate, datetime.date(2020, 2, 1), id='Date'),  # fmt: skip
    pytest.param(FieldType.DateTime, AttributeDateTime, datetime.datetime(2020, 2, 1, 9, 10, 25), id='DateTime'),  # fmt: skip
    pytest.param(FieldType.Time, AttributeTime, datetime.time(9, 10, 25), id='Time'),  # fmt: skip
]


@pytest.mark.parametrize('field_type, AttributeClass, value', params)
def test_repr(app_empty, field_type, AttributeClass, value):
    app = app_empty  # noqa: F841

    attr1 = AttributeClass(value=value)
    repr(attr1)

    attr1.field = Field(name="attr1", type_=field_type)
    repr(attr1)


@pytest.mark.parametrize('field_type, AttributeClass, value', params)
def test_obj(app_empty, field_type, AttributeClass, value):
    app = app_empty  # noqa: F841
    field = Field(name="field1", type_=field_type)
    attr = AttributeClass(field=field, value=value)  # noqa: F841


@pytest.mark.parametrize('field_type, AttributeClass, value', params)
def test_commit(app_empty, field_type, AttributeClass, value):
    app = app_empty
    with app.app_context():
        field = Field(name="field1", type_=field_type)
        product_type = ProductType(name="map")
        product_type.fields = [TypeFieldAssociation(field=field)]
        sa.session.add(product_type)
        sa.session.commit()

    with app.app_context():
        product_type = ProductType.query.filter_by(name="map").one()
        field = product_type.fields[0].field
        product = Product(name="product1", type_=product_type)
        attr = AttributeClass(product=product, field=field, value=value)
        sa.session.add(attr)
        sa.session.commit()

    with app.app_context():
        attr = AttributeClass.query.one()
        assert attr.__class__ is AttributeClass
        assert attr.field.name == 'field1'
        assert attr.field.type_ is field_type
        assert attr.value == value
        assert getattr(attr.product, AttributeClass.backref_column) == [attr]
        assert getattr(attr.field, AttributeClass.backref_column) == [attr]


##__________________________________________________________________||
def test_map1_attributes(app):
    with app.app_context():
        map1 = Product.query.filter_by(product_id=1).one()

        assert len(map1.attributes_unicode_text) == 1
        name = [a for a in map1.attributes_unicode_text if a.name == "attr1"][0]
        assert name.value == "value1"

        assert len(map1.attributes_date) == 1
        date_produced = [
            a for a in map1.attributes_date if a.name == "date_produced"
        ][0]
        assert date_produced.value == datetime.date(2020, 2, 1)

        assert len(map1.attributes_date_time) == 1
        time_posted = [
            a for a in map1.attributes_date_time if a.name == "time_posted"
        ][0]
        assert time_posted.value == datetime.datetime(2020, 2, 1, 9, 10, 25)


def test_filter(app):

    with app.app_context():
        expected = Product.query.filter_by(product_id=1).one()
        actual = (
            Product.query.join(AttributeUnicodeText)
            .filter_by(name="attr1", value="value1")
            .one()
        )
        assert actual is expected

def test_order(app):

    with app.app_context():
        map1 = Product.query.filter_by(product_id=1).one()
        map2 = Product.query.filter_by(product_id=2).one()
        map3 = Product.query.filter_by(product_id=3).one()

        expected = [map3, map2, map1]

        actual = (
            Product.query.join(ProductType)
            .filter_by(name="map")
            .join(AttributeDate)
            .filter_by(name="date_produced")
            .order_by(AttributeDate.value.desc())
            .all()
        )

        assert actual == expected


##__________________________________________________________________||
def test_order_nested(app_empty):
    app = app_empty

    Map = ProductType(type_id=1, name="map")
    map1 = Product(product_id=1, name="map1", type_=Map)
    map2 = Product(product_id=2, name="map2", type_=Map)
    map3 = Product(product_id=3, name="map3", type_=Map)
    map4 = Product(product_id=4, name="map4", type_=Map)
    map5 = Product(product_id=5, name="map5", type_=Map)

    AttributeUnicodeText(product=map1, name="attr1", value="1")
    AttributeUnicodeText(product=map2, name="attr1", value="2")
    AttributeUnicodeText(product=map3, name="attr1", value="1")
    AttributeUnicodeText(product=map4, name="attr1", value="2")
    AttributeUnicodeText(product=map5, name="attr1", value="1")

    AttributeUnicodeText(product=map1, name="attr2", value="b")
    AttributeUnicodeText(product=map2, name="attr2", value="a")
    AttributeUnicodeText(product=map3, name="attr2", value="c")
    AttributeUnicodeText(product=map4, name="attr2", value="b")
    AttributeUnicodeText(product=map5, name="attr2", value="a")

    with app.app_context():
        sa.session.add(Map)
        sa.session.commit()

    with app.app_context():

        map1 = Product.query.filter_by(product_id=1).one()
        map2 = Product.query.filter_by(product_id=2).one()
        map3 = Product.query.filter_by(product_id=3).one()
        map4 = Product.query.filter_by(product_id=4).one()
        map5 = Product.query.filter_by(product_id=5).one()

        expected = [map2, map4, map5, map1, map3]

        # ORM Alias: https://docs.sqlalchemy.org/en/14/tutorial/data_select.html#orm-entity-aliases
        # refer to the same table multiple times
        AliasedAttributeUnicodeText1 = aliased(AttributeUnicodeText)
        AliasedAttributeUnicodeText2 = aliased(AttributeUnicodeText)

        # sort descending order of attr1 then ascending order of attr2
        query = (
            Product.query.join(ProductType)
            .filter_by(name="map")
            .join(AliasedAttributeUnicodeText1)
            .filter_by(name="attr1")
            .order_by(AliasedAttributeUnicodeText1.value.desc())
            .join(AliasedAttributeUnicodeText2)
            .filter_by(name="attr2")
            .order_by(AliasedAttributeUnicodeText2.value)
        )

        actual = query.all()

        assert actual == expected


##__________________________________________________________________||
def test_delte_orphan(app):

    with app.app_context():
        map1 = Product.query.filter_by(product_id=1).one()
        sa.session.delete(map1)
        sa.session.commit()

    with app.app_context():
        map1 = Product.query.filter_by(product_id=1).one_or_none()
        assert map1 is None
        attr = AttributeUnicodeText.query.filter_by(name='attr1', value='value1').one_or_none()
        assert attr is None

##__________________________________________________________________||
