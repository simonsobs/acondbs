from ..models import Field, FieldType
from ..db.sa import sa


##__________________________________________________________________||
def create_field(name, type_, field_id=None):
    """Create a field"""
    type_ = FieldType(type_)  # in case given by int
    model = Field(name=name, type_=type_, field_id=field_id)
    sa.session.add(model)
    return model


def update_field(field_id, name):
    """Update a field

    Only name can be changed
    """
    model = Field.query.filter_by(field_id=field_id).one()
    model.name = name
    return model


def delete_field(field_id):
    """Delete a field"""
    model = Field.query.filter_by(field_id=field_id).one()
    sa.session.delete(model)


##__________________________________________________________________||
