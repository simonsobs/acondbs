from ..db.sa import sa
from ..models import ProductType, Field, TypeFieldAssociation


##__________________________________________________________________||
def create_product_type(**kwargs):
    """Create a product type"""
    field_ids = kwargs.pop("field_ids", None)
    model = ProductType(**kwargs)
    if field_ids:
        with sa.session.no_autoflush:
            model.fields = _create_fields(field_ids)
    sa.session.add(model)
    return model


def _create_fields(field_ids):
    ids = sorted(set(field_ids))
    fields_ = [Field.query.filter_by(field_id=i).one() for i in ids]
    return [TypeFieldAssociation(field=f) for f in fields_]


##__________________________________________________________________||
def update_product_type(type_id, **kwargs):
    """Update a product type"""

    model = ProductType.query.filter_by(type_id=type_id).one()
    field_ids = kwargs.pop("field_ids", None)

    for k, v in kwargs.items():
        setattr(model, k, v)

    if field_ids is not None:
        with sa.session.no_autoflush:
            model.fields = _update_fields(model.fields, field_ids)

    return model


def _update_fields(old_fields: list, new_field_ids: list) -> list:

    new_ids = set(new_field_ids)
    old_ids = {f.field_id for f in old_fields}

    unchanged_ids = new_ids & old_ids
    added_ids = new_ids - unchanged_ids
    removed_ids = old_ids - unchanged_ids

    field_dict = {f.field_id: f for f in old_fields}
    #  {field_id: TypeFieldAssociation}

    for id_ in removed_ids:
        field = field_dict.pop(id_)
        sa.session.delete(field)
        # NOTE: Probably unnecesary. TypeFieldAssociation is likely to
        # be automatically deleted.

    for id_ in added_ids:
        field_ = Field.query.filter_by(field_id=id_).one()
        field = TypeFieldAssociation(field=field_)
        field_dict[id_] = field

    return [field_dict[i] for i in sorted(new_ids)]


##__________________________________________________________________||
def delete_product_type(type_id):
    """Delete a product type"""
    model = ProductType.query.filter_by(type_id=type_id).one()
    sa.session.delete(model)


##__________________________________________________________________||
