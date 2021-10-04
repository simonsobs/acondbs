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


def update_product_type(type_id, input):
    """Update a product type"""
    model = ProductType.query.filter_by(type_id=type_id).one()
    for k, v in input.items():
        setattr(model, k, v)
    return model


def delete_product_type(type_id):
    """Delete a product type"""
    model = ProductType.query.filter_by(type_id=type_id).one()
    sa.session.delete(model)


##__________________________________________________________________||
