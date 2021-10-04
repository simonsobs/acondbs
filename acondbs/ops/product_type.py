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
        with sa.session.no_autoflush:
            old_field_dict = {f.field_id: f for f in model.fields}
            new_fields = []
            field_ids = sorted(set(field_ids))
            for field_id in field_ids:
                field = old_field_dict.pop(field_id, None)
                if not field:
                    field = Field.query.filter_by(field_id=field_id).one()
                    field = TypeFieldAssociation(field=field)
                new_fields.append(field)
            for field in old_field_dict.values():
                print(field)
                sa.session.delete(field)
            model.fields = new_fields
    return model


def delete_product_type(type_id):
    """Delete a product type"""
    model = ProductType.query.filter_by(type_id=type_id).one()
    sa.session.delete(model)


##__________________________________________________________________||
