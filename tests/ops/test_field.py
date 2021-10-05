import pytest

from acondbs import ops
from acondbs.models import FieldType, Field


##__________________________________________________________________||
params = [
    pytest.param(dict(name="contact", type_=FieldType.UnicodeText), id="one"),
    pytest.param(dict(name="contact", type_=1), id="type-by-int"),
    pytest.param(dict(field_id=234, name="contact", type_=FieldType.UnicodeText), id="type-by-int"),  # fmt: skip
]


@pytest.mark.parametrize("kwargs", params)
def test_create_field(app_empty, kwargs):
    app = app_empty

    with app.app_context():
        model = ops.create_field(**kwargs)
        assert model.name == "contact"
        assert model.type_ == FieldType.UnicodeText
        ops.commit()
        assert model.field_id

    with app.app_context():
        model = Field.query.filter_by(name="contact").one()
        assert model.name == "contact"
        assert model.type_ == FieldType.UnicodeText
        if field_id := kwargs.get("field_id"):
            assert model.field_id == field_id
        else:
            assert model.field_id == 1


##__________________________________________________________________||
def test_update_field(app):

    field_id = 1

    with app.app_context():
        model = ops.update_field(field_id=field_id, name="author")
        ops.commit()

    with app.app_context():
        model = Field.query.filter_by(field_id=field_id).one()
        assert model.name == "author"
        assert model.type_ == FieldType.UnicodeText
        assert model.field_id == field_id


##__________________________________________________________________||
def test_delete_field(app):

    field_id = 4

    with app.app_context():
        ret = ops.delete_field(field_id=field_id)
        ops.commit()
        assert ret is None

    with app.app_context():
        model = Field.query.filter_by(field_id=field_id).one_or_none()
        assert model is None


##__________________________________________________________________||
