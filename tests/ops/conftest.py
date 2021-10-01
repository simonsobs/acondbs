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
    app = app_empty

    with app.app_context():

        # fmt: off
        ops.create_field(field_id=1, name="contact", type_=FieldType.UnicodeText)
        ops.create_field(field_id=2, name="produced_by", type_=FieldType.UnicodeText)
        ops.create_field(field_id=3, name="date_produced", type_=FieldType.Date)
        # fmt: on

        ops.commit()

    yield app


##__________________________________________________________________||
