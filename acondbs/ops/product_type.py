from ..db.sa import sa
from ..models import ProductType, Field, TypeFieldAssociation


##__________________________________________________________________||
def create_product_type(**kwargs):
    """Create a product type"""
    field_ids = kwargs.pop("field_ids", None)
    model = ProductType(**kwargs)
    if field_ids:
        field_ids = sorted(set(field_ids))
        fields = [Field.query.filter_by(field_id=i).one() for i in field_ids]
        fields = [TypeFieldAssociation(field=f) for f in fields]
        model.fields = fields
    sa.session.add(model)
    return model


def update_product_type(type_id, **kwargs):
    """Update a product type"""

    model = ProductType.query.filter_by(type_id=type_id).one()
    field_ids = kwargs.pop("field_ids", None)

    for k, v in kwargs.items():
        setattr(model, k, v)

    if field_ids:
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

    with sa.session.no_autoflush:

        for id_ in removed_ids:
            field = field_dict.pop(id_)
            sa.session.delete(field)

        for id_ in added_ids:
            field_ = Field.query.filter_by(field_id=id_).one()
            field = TypeFieldAssociation(field=field_)
            field_dict[id_] = field

    return [field_dict[i] for i in sorted(new_ids)]


def delete_product_type(type_id):
    """Delete a product type"""
    model = ProductType.query.filter_by(type_id=type_id).one()
    sa.session.delete(model)


##__________________________________________________________________||
