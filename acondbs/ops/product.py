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
        model.paths = _update_paths(model.paths, input_paths)

    # update relations
    input_relations = kwargs.pop("relations", None)
    if input_relations is not None:
        with sa.session.no_autoflush:
            model.relations = _update_relations(
                model.relations, input_relations
            )

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


def _update_paths(old, input):
    path_dict = {p.path: p for p in old}
    return [
        path_dict[p] if p in path_dict else ProductFilePath(path=p)
        for p in input
    ]


def _update_relations(old, input):

    # sets of tuples (type_id, other_product_id) of ProductRelation
    new_ids = {(i["type_id"], i["product_id"]) for i in input}
    old_ids = {(r.type_id, r.other_product_id) for r in old}

    added_ids = new_ids - old_ids

    model_dict = {(r.type_id, r.other_product_id): r for r in old}
    for id_ in added_ids:
        type_id, product_id = id_
        type_ = ProductRelationType.query.filter_by(type_id=type_id).one()
        other = Product.query.filter_by(product_id=product_id).one()
        model_dict[id_] = ProductRelation(type_=type_, other=other)

    return [model_dict[i] for i in sorted(new_ids)]


##__________________________________________________________________||
def delete_product(product_id):
    """Delete a product"""

    model = Product.query.filter_by(product_id=product_id).one()
    sa.session.delete(model)
    return


##__________________________________________________________________||
