import pytest

from acondbs import create_app
from acondbs.db.ops import define_tables
from acondbs.models import FieldType
from acondbs import ops

from acondbs.db.sa import sa
from acondbs.models import GitHubUser


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
        user1 = GitHubUser(login="user1", git_hub_id="04:User1")
        sa.session.add(user1)
        sa.session.commit()

    with y.app_context():
        ops.create_field(field_id=1, name="text_one", type_=FieldType.UnicodeText)  # fmt: skip
        ops.create_field(field_id=2, name="text_two", type_=FieldType.UnicodeText)  # fmt: skip
        ops.create_field(field_id=3, name="check1", type_=FieldType.Boolean)
        ops.create_field(field_id=4, name="check2", type_=FieldType.Boolean)
        ops.create_field(field_id=5, name="number", type_=FieldType.Integer)
        ops.create_field(field_id=6, name="value", type_=FieldType.Float)
        ops.create_field(field_id=7, name="date", type_=FieldType.Date)
        ops.create_field(field_id=8, name="date_time", type_=FieldType.DateTime)  # fmt: skip
        ops.create_field(field_id=9, name="time", type_=FieldType.Time)
        ops.create_field(field_id=10, name="not_used", type_=FieldType.Time)

        ops.commit()

    with y.app_context():
        ops.create_product_type(
            type_id=1,
            name="map",
            field_ids=[1, 3, 5, 6, 7, 8, 9],
        )
        ops.create_product_type(
            type_id=2,
            name="beam",
            field_ids=[1, 2, 3],
        )
        ops.commit()

    with y.app_context():
        ops.create_product_relation_type(
            type_={"type_id": 1, "name": "parent"},
            reverse={"type_id": 2, "name": "child"},
        )
        ops.commit()

    yield y


##__________________________________________________________________||
