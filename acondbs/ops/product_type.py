from ..models import ProductType as ProductTypeModel
from ..db.sa import sa


##__________________________________________________________________||
def create_product_type(input):
    """Create a product type"""
    model = ProductTypeModel(**input)
    sa.session.add(model)
    return model


def update_product_type(type_id, input):
    """Update a product type"""
    model = ProductTypeModel.query.filter_by(type_id=type_id).one()
    for k, v in input.items():
        setattr(model, k, v)
    return model


def delete_product_type(type_id):
    """Delete a product"""
    model = ProductTypeModel.query.filter_by(type_id=type_id).one()
    sa.session.delete(model)


##__________________________________________________________________||
