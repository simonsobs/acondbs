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
        new_field_ids = set(field_ids)
        old_field_ids = {f.field_id for f in model.fields}

        unchanged_field_ids = new_field_ids & old_field_ids
        added_field_ids = new_field_ids - unchanged_field_ids
        removed_field_ids = old_field_ids - unchanged_field_ids

        field_dict = {f.field_id: f for f in model.fields}
        #  {field_id: TypeFieldAssociation}

        with sa.session.no_autoflush:

            for field_id in removed_field_ids:
                field = field_dict.pop(field_id)
                sa.session.delete(field)

            for field_id in added_field_ids:
                field_ = Field.query.filter_by(field_id=field_id).one()
                field = TypeFieldAssociation(field=field_)
                field_dict[field_id] = field

        model.fields = [field_dict[i] for i in sorted(new_field_ids)]

    return model


def delete_product_type(type_id):
    """Delete a product type"""
    model = ProductType.query.filter_by(type_id=type_id).one()
    sa.session.delete(model)


##__________________________________________________________________||
