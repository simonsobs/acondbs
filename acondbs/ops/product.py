import datetime

from ..models import (
    ProductType,
    Product,
    ProductFilePath,
    ProductRelation,
    ProductRelationType,
    AttributeUnicodeText,
    AttributeDate,
)

from ..db.sa import sa


##__________________________________________________________________||
def create_product(user, **kwargs):
    """Create a product"""

    type_id = kwargs.pop("type_id")
    paths = kwargs.pop("paths", [])
    relations = kwargs.pop("relations", [])

    product_type = ProductType.query.filter_by(type_id=type_id).one()

    model = Product(
        type_=product_type,
        posting_git_hub_user=user,
        **kwargs,
    )

    model.paths = [ProductFilePath(path=p) for p in paths]

    with sa.session.no_autoflush:
        model.relations = [
            ProductRelation(
                type_=ProductRelationType.query.filter_by(
                    type_id=r["type_id"]
                ).one(),
                other=Product.query.filter_by(
                    product_id=r["product_id"]
                ).one(),
            )
            for r in relations
        ]

    field_dict = {f.field.name: f.field for f in product_type.fields}
    columns_text = ["contact", "produced_by"]
    columns_date = ["date_produced"]
    for c in columns_text:
        AttributeUnicodeText(
            name=c, field=field_dict[c], product=model, value=kwargs.get(c)
        )
    for c in columns_date:
        AttributeDate(
            name=c, field=field_dict[c], product=model, value=kwargs.get(c)
        )
    sa.session.add(model)
    return model


def update_product(user, product_id, **kwargs):
    """Update a product"""

    model = Product.query.filter_by(product_id=product_id).one()

    # update paths
    input_paths = kwargs.pop("paths", None)
    if input_paths is not None:
        pdict = {p.path: p for p in model.paths}
        model.paths = [
            pdict[p] if p in pdict else ProductFilePath(path=p)
            for p in input_paths
        ]

    # update relations
    input_relations = kwargs.pop("relations", None)
    if input_relations is not None:
        with sa.session.no_autoflush:
            old_relations_dict = {
                (r.type_id, r.self_product_id, r.other_product_id): r
                for r in model.relations
            }
            for r in input_relations:
                rmodel = old_relations_dict.pop(
                    (r["type_id"], model.product_id, r["product_id"]), None
                )
                if not rmodel:
                    type_ = ProductRelationType.query.filter_by(
                        type_id=r["type_id"]
                    ).one()
                    other = Product.query.filter_by(
                        product_id=r["product_id"]
                    ).one()
                    m = ProductRelation(self_=model, type_=type_, other=other)
                    sa.session.add(m)
            for m in old_relations_dict.values():
                sa.session.delete(m)

    # update scalar fields
    for k, v in kwargs.items():
        setattr(model, k, v)

    # update attributes
    field_dict = {f.field.name: f.field for f in model.type_.fields}
    columns_text = ["contact", "produced_by"]
    columns_date = ["date_produced"]
    attr_dict = {a.name: a for a in model.attributes_unicode_text}
    for c in columns_text:
        if c not in kwargs:
            continue
        attr = attr_dict.get(c)
        if attr:
            attr.value = kwargs[c]
        else:
            AttributeUnicodeText(
                name=c, field=field_dict[c], product=model, value=kwargs[c]
            )
    attr_dict = {a.name: a for a in model.attributes_date}
    for c in columns_date:
        if c not in kwargs:
            continue
        attr = attr_dict.get(c)
        if attr:
            attr.value = kwargs[c]
        else:
            AttributeDate(
                name=c, field=field_dict[c], product=model, value=kwargs[c]
            )

    model.time_updated = datetime.datetime.now()
    model.updating_git_hub_user = user

    return model


def delete_product(product_id):
    """Delete a product"""

    model = Product.query.filter_by(product_id=product_id).one()
    sa.session.delete(model)
    return


##__________________________________________________________________||
