import pytest

from acondbs import create_app
from acondbs.db.ops import define_tables
from acondbs.models import FieldType
from acondbs import ops


##__________________________________________________________________||
@pytest.fixture
def app_empty():
    database_uri = "sqlite:///:memory:"
    y = create_app(SQLALCHEMY_DATABASE_URI=database_uri)
    with y.app_context():
        define_tables()
    yield y


@pytest.fixture
def app(app_empty):
    y = app_empty

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
        ops.create_product_type(
            type_id=1,
            name="map",
            order=2,
            indef_article="a",
            singular="map",
            plural="maps",
            icon="mdi-map",
            field_ids=[1, 2, 3],
        )
        ops.create_product_type(
            type_id=2,
            name="beam",
            order=1,
            indef_article="a",
            singular="beam",
            plural="beams",
            icon="mdi-spotlight-beam",
            field_ids=[1, 2, 3],
        )
        ops.commit()

    yield y


##__________________________________________________________________||
