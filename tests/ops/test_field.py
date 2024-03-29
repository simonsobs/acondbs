import pytest
from flask import Flask

from acondbs import ops
from acondbs.models import Field, FieldType

params = [
    pytest.param(FieldType.Float, id='by-enum'),
    pytest.param(4, id='by-int'),
]


@pytest.mark.parametrize('type_', params)
def test_create(app_empty: Flask, type_) -> None:
    app = app_empty

    with app.app_context():
        model = ops.create_field(name='new_field', type_=type_)
        assert model.name == 'new_field'
        assert model.type_ == FieldType.Float
        ops.commit()
        field_id = model.field_id
        assert field_id

    with app.app_context():
        model = Field.query.filter_by(field_id=field_id).one()
        assert model.name == 'new_field'
        assert model.type_ == FieldType.Float
        assert model.field_id == field_id


def test_fixture(app: Flask) -> None:
    with app.app_context():
        assert Field.query.count() == 9


def test_update(app: Flask) -> None:
    with app.app_context():
        model = Field.query.filter_by(name='number').one()
        field_id = model.field_id

    with app.app_context():
        model = ops.update_field(field_id=field_id, name='number_renamed')
        ops.commit()

    with app.app_context():
        model = Field.query.filter_by(field_id=field_id).one()
        assert model.name == 'number_renamed'
        assert model.field_id == field_id


def test_delete(app: Flask) -> None:
    with app.app_context():
        model = ops.create_field(name='to_be_deleted', type_=FieldType.Float)
        ops.commit()
        field_id = model.field_id

    with app.app_context():
        count = Field.query.count()
        ops.delete_field(field_id=field_id)
        ops.commit()

    with app.app_context():
        model = Field.query.filter_by(field_id=field_id).one_or_none()
        assert model is None
        assert Field.query.count() == count - 1
