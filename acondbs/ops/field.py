from ..models import Field
from ..db.sa import sa


##__________________________________________________________________||
def create_field(**kwargs):
    """Create a field"""
    model = Field(**kwargs)
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
