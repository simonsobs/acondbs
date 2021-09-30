from acondbs import ops
from acondbs.models import FieldType, Field


##__________________________________________________________________||
def test_create_field(app_empty):
    app = app_empty

    with app.app_context():
        model = ops.create_field(name="contact", type_=FieldType.UnicodeText)
        ops.commit()
        assert model.field_id
        assert model.name == "contact"
        assert model.type_ == FieldType.UnicodeText

    with app.app_context():
        model = Field.query.filter_by(name="contact").one()
        assert model.name == "contact"
        assert model.type_ == FieldType.UnicodeText


def test_create_field_by_int(app_empty):
    app = app_empty

    with app.app_context():
        model = ops.create_field(name="contact", type_=1)
        ops.commit()
        assert model.field_id
        assert model.name == "contact"
        assert model.type_ == FieldType.UnicodeText

    with app.app_context():
        model = Field.query.filter_by(name="contact").one()
        assert model.name == "contact"
        assert model.type_ == FieldType.UnicodeText


##__________________________________________________________________||
def test_update_field(app_empty):
    app = app_empty

    with app.app_context():
        model = ops.create_field(name="contact", type_=FieldType.UnicodeText)
        ops.commit()
        field_id = model.field_id

    with app.app_context():
        model = ops.update_field(field_id=field_id, name="author")
        ops.commit()

    with app.app_context():
        model = Field.query.filter_by(field_id=field_id).one()
        assert model.name == "author"
        assert model.type_ == FieldType.UnicodeText


##__________________________________________________________________||
def test_delete_field(app_empty):
    app = app_empty

    with app.app_context():
        model = ops.create_field(name="contact", type_=FieldType.UnicodeText)
        ops.commit()
        field_id = model.field_id

    with app.app_context():
        ops.delete_field(field_id=field_id)
        ops.commit()

    with app.app_context():
        model = Field.query.filter_by(field_id=field_id).one_or_none()
        assert model is None


##__________________________________________________________________||
