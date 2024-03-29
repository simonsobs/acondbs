from typing import Optional

from acondbs.db.sa import sa
from acondbs.models import Field, FieldType


def create_field(name: str, type_: FieldType, field_id: Optional[int] = None) -> Field:
    '''Instantiate SQLAlchemy ORM model 'Field'

    Parameters
    ----------
    name : str
        The name of the new field
    type_ : enum or int
        The type of the new field, e.g., unicode text, int
    field_id : int, optional
        The ID of the new field

    Returns
    -------
    object
        The created model

    '''
    type_ = FieldType(type_)  # in case given by int
    model = Field(name=name, type_=type_, field_id=field_id)
    sa.session.add(model)
    return model


def update_field(field_id: int, name: str) -> Field:
    '''Update a field

    Only name can be changed.

    Parameters
    ----------
    field_id : int
        The ID of the field to be updated
    name : str
        The new name

    Returns
    -------
    object
        The model

    '''
    model = Field.query.filter_by(field_id=field_id).one()
    model.name = name
    return model


def delete_field(field_id: int) -> None:
    '''Delete a field

    Parameters
    ----------
    field_id : int
        The ID of the field to be deleted

    Returns
    -------
    None

    '''
    model = Field.query.filter_by(field_id=field_id).one()
    sa.session.delete(model)
