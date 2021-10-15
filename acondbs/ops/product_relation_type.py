from ..db.sa import sa
from ..models import ProductRelationType


##__________________________________________________________________||
def create_product_relation_type(type_, reverse=None, self_reverse=False):
    """Create a product relation type"""

    if self_reverse and reverse:
        raise ValueError('"reverse" is given when "self_reverse" is True')

    model = ProductRelationType(**type_)
    if self_reverse:
        model.reverse = model
    else:
        reverse_ = ProductRelationType(**reverse)
        model.reverse = reverse_

    sa.session.add(model)
    return model


def update_product_relation_type(type_id, **kwargs):
    """Update a product relation type"""
    model = ProductRelationType.query.filter_by(type_id=type_id).one()
    for k, v in kwargs.items():
        setattr(model, k, v)
    return model


def delete_product_relation_type(type_id):
    """Delete a product relation type"""
    model = ProductRelationType.query.filter_by(type_id=type_id).one()
    sa.session.delete(model)


##__________________________________________________________________||
