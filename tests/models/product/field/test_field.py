from sqlalchemy import exc

import pytest

from acondbs.db.sa import sa
from acondbs.models import ProductType, FieldType, Field, TypeFieldAssociation


##__________________________________________________________________||
def test_repr(app_empty):
    app = app_empty  # noqa: F841

    assoc = TypeFieldAssociation()
    repr(assoc)

    field1 = Field(name="field1")
    repr(field1)

    field1.type_ = FieldType.UnicodeText
    repr(field1)

    type1 = ProductType(name="type1")
    repr(type1)

    assoc.type_ = type1
    assoc.field = field1
    repr(assoc)


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
def test_one(app):
    with app.app_context():
        field = Field.query.filter_by(name="field1").one()
        assert field.name == "field1"
        assert field.type_ is FieldType.UnicodeText
        assert field.type_.name == "UnicodeText"


def test_two(app):
    with app.app_context():
        field = Field.query.filter_by(name="フィールド2").one()
        assert field.name == "フィールド2"
        assert field.type_ is FieldType.UnicodeText
        assert field.type_.name == "UnicodeText"


##__________________________________________________________________||
def test_type(app):
    with app.app_context():
        field1 = Field.query.filter_by(name="field1").one()
        field2 = Field.query.filter_by(name="フィールド2").one()
        type1 = ProductType.query.filter_by(name="type1").one()
        assert [f.field for f in type1.fields] == [field1, field2]


def test_delete_type(app):
    """test delete a type

    When a type is deleted, its associations should be automatically
    deleted while the fields themselves should still exist.

    """

    with app.app_context():
        type1 = ProductType.query.filter_by(name="type1").one()
        sa.session.delete(type1)
        sa.session.commit()

    with app.app_context():
        assert ProductType.query.filter_by(name="type1").one_or_none() is None
        assert Field.query.filter_by(name="field1").one()
        assert Field.query.filter_by(name="フィールド2").one()
        associations = TypeFieldAssociation.query.all()
        assert not associations  # emtpy


def test_delete_field(app):
    """test delete a field

    When a field is deleted, its associations should be automatically
    deleted.

    """

    with app.app_context():
        field1 = Field.query.filter_by(name="field1").one()
        sa.session.delete(field1)
        sa.session.commit()

    with app.app_context():
        assert ProductType.query.filter_by(name="type1").one()
        assert Field.query.filter_by(name="field1").one_or_none() is None
        associations = TypeFieldAssociation.query.all()
        assert len(associations) == 1


##__________________________________________________________________||
