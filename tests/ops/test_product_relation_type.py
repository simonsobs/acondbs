import pytest
from flask import Flask

from acondbs import ops
from acondbs.models import ProductRelationType


def test_fixture(app: Flask) -> None:
    with app.app_context():
        assert ProductRelationType.query.count() == 2


def test_create(app: Flask) -> None:
    type_ = {'name': 'doctor'}
    reverse = {'name': 'patient'}

    with app.app_context():
        count = ProductRelationType.query.count()
        model = ops.create_product_relation_type(type_, reverse)
        ops.commit()
        type_id = model.type_id
        assert type_id

    with app.app_context():
        assert ProductRelationType.query.count() == (count + 2)
        model = ProductRelationType.query.filter_by(type_id=type_id).one()
        assert model.name == 'doctor'
        assert model.reverse.name == 'patient'


def test_create_self_reverse(app: Flask) -> None:
    type_ = {'name': 'spouse'}

    with app.app_context():
        count = ProductRelationType.query.count()
        model = ops.create_product_relation_type(type_, self_reverse=True)
        ops.commit()
        type_id = model.type_id
        assert type_id

    with app.app_context():
        assert ProductRelationType.query.count() == (count + 1)
        model = ProductRelationType.query.filter_by(type_id=type_id).one()
        assert model.name == 'spouse'
        assert model.reverse is model


def test_create_error_both(app: Flask) -> None:
    type_ = {'name': 'doctor'}
    reverse = {'name': 'patient'}

    with app.app_context():
        count = ProductRelationType.query.count()
        with pytest.raises(ValueError):
            ops.create_product_relation_type(type_, reverse, self_reverse=True)
            ops.commit()

    with app.app_context():
        assert ProductRelationType.query.count() == count


def test_create_error_neither(app: Flask) -> None:
    type_ = {'name': 'doctor'}

    with app.app_context():
        count = ProductRelationType.query.count()
        with pytest.raises(ValueError):
            ops.create_product_relation_type(type_)
            ops.commit()

    with app.app_context():
        assert ProductRelationType.query.count() == count


def test_update(app: Flask) -> None:
    type_id = 1

    with app.app_context():
        count = ProductRelationType.query.count()
        model = ops.update_product_relation_type(type_id=type_id, name='renamed')
        ops.commit()
        assert model.type_id == type_id

    with app.app_context():
        assert ProductRelationType.query.count() == count
        model = ProductRelationType.query.filter_by(type_id=type_id).one()
        assert model.name == 'renamed'


def test_delete(app: Flask) -> None:
    with app.app_context():
        model = ops.create_product_relation_type(
            type_={'name': 'to_be_deleted'},
            reverse={'name': 'reverse'},
        )
        ops.commit()
        type_id = model.type_id

    with app.app_context():
        count = ProductRelationType.query.count()
        ops.delete_product_relation_type(type_id=type_id)
        ops.commit()

    with app.app_context():
        assert ProductRelationType.query.count() == count - 2
