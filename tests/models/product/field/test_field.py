import pytest
from flask import Flask
from sqlalchemy import exc

from acondbs.db.sa import sa
from acondbs.models import Field, FieldType


def test_repr(app_empty: Flask) -> None:
    app = app_empty  # noqa: F841

    field1 = Field(name='field1')
    repr(field1)

    field1.type_ = FieldType.UnicodeText
    repr(field1)


def test_commit(app_empty: Flask) -> None:
    app = app_empty

    with app.app_context():
        field1 = Field(name='field1', type_=FieldType.Date)
        sa.session.add(field1)
        sa.session.commit()

    with app.app_context():
        field1 = Field.query.filter_by(name='field1').one()
        assert field1.field_id
        assert field1.name == 'field1'
        assert field1.type_ is FieldType.Date


def test_commit_with_field_id(app_empty: Flask) -> None:
    app = app_empty

    with app.app_context():
        field1 = Field(field_id=259, name='field1', type_=FieldType.Date)
        sa.session.add(field1)
        sa.session.commit()

    with app.app_context():
        field1 = Field.query.filter_by(field_id=259).one()
        assert field1.name == 'field1'
        assert field1.type_ is FieldType.Date


def test_nullable(app_empty: Flask) -> None:
    app = app_empty  # noqa: F841

    # without type_
    with app.app_context():
        field = Field(name='field')
        sa.session.add(field)
        with pytest.raises(exc.IntegrityError):
            sa.session.commit()

    # without name
    with app.app_context():
        field = Field(type_=FieldType.UnicodeText)
        sa.session.add(field)
        with pytest.raises(exc.IntegrityError):
            sa.session.commit()


def test_enum_by_int(app_empty: Flask) -> None:
    '''Test if an enum can be given by a number

    No. It raises an exception at a commit

    TODO: move this test to tests.models.example
    '''
    app = app_empty

    with app.app_context():
        field1 = Field(name='field1', type_=1)
        sa.session.add(field1)
        with pytest.raises(exc.StatementError):
            sa.session.commit()
