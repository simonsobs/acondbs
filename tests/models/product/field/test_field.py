from sqlalchemy import exc

import pytest

from acondbs.db.sa import sa
from acondbs.models import FieldType, Field


##__________________________________________________________________||
def test_repr(app_empty):
    app = app_empty  # noqa: F841

    field1 = Field(name="field1")
    repr(field1)

    field1.type_ = FieldType.UnicodeText
    repr(field1)


##__________________________________________________________________||
def test_attribute_class(app_empty):
    app = app_empty  # noqa: F841
    for k, v in FieldType.__members__.items():
        assert v.attribute_class.__name__ == f"Attribute{k}"


##__________________________________________________________________||
def test_one(app):
    with app.app_context():
        field = Field.query.filter_by(name="field1").one()
        assert field.name == "field1"
        assert field.type_ is FieldType.UnicodeText
        assert field.type_.name == "UnicodeText"


def test_entries(app):
    with app.app_context():
        fields = Field.query.all()
        assert len(fields) == 8


def test_unicode_name(app):
    with app.app_context():
        field = Field.query.filter_by(name="フィールド").one()
        assert field.name == "フィールド"


##__________________________________________________________________||
def test_nullable(app_empty):
    app = app_empty  # noqa: F841

    with app.app_context():
        field = Field(name="field")
        sa.session.add(field)
        with pytest.raises(exc.IntegrityError):
            sa.session.commit()

    with app.app_context():
        field = Field(type_=FieldType.UnicodeText)
        sa.session.add(field)
        with pytest.raises(exc.IntegrityError):
            sa.session.commit()


##__________________________________________________________________||
def test_enum_by_int(app_empty):
    """Test if an enum can be given by a number

    No. It raises an exception at a commit

    TODO: move this test to tests.models.example
    """
    app = app_empty

    with app.app_context():
        field1 = Field(name="field1", type_=1)
        sa.session.add(field1)
        with pytest.raises(exc.StatementError):
            sa.session.commit()


##__________________________________________________________________||
