import datetime

from ..models import (
    ProductType,
    Product,
    ProductFilePath,
    ProductRelation,
    ProductRelationType,
)

from ..db.sa import sa


##__________________________________________________________________||
def uniq_preserving_order(list_):
    # https://stackoverflow.com/a/17016257/7309855
    return list(dict.fromkeys(list_))


def _normalize_paths(paths):
    # e.g., paths = ["  /d/e ", " ", "/a/b/c", "/f/g", "/d/e"]

    ret = [p.strip() for p in paths]  # strip
    # e.g., ["/d/e", "", "/a/b/c", "/f/g", "/d/e"]

    ret = [p for p in ret if p]  # remove empty
    # e.g., ["/d/e", "/a/b/c", "/f/g", "/d/e"]

    ret = uniq_preserving_order(ret)
    # e.g., ["/d/e", "/a/b/c", "/f/g"]

    return ret


##__________________________________________________________________||
def create_product(
    type_id, user=None, paths=None, relations=None, attributes=None, **kwargs
):
    """Create a product"""

    product_type = ProductType.query.filter_by(type_id=type_id).one()

    model = Product(
        type_=product_type,
        posting_git_hub_user=user,
        **kwargs,
    )

    if paths is not None:
        paths = _normalize_paths(paths)
        model.paths = [ProductFilePath(path=p) for p in paths]

    if relations is not None:
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

    if attributes is None:
        attributes = {}

    for association in product_type.fields:
        field = association.field
        value = attributes.get(field.field_id)
        field.type_.attribute_class(
            name=field.name,
            field=field,
            product=model,
            value=value,
        )

    sa.session.add(model)
    return model


def update_product(user, product_id, **kwargs):
    """Update a product"""

    model = Product.query.filter_by(product_id=product_id).one()

    paths = kwargs.pop("paths", None)
    relations = kwargs.pop("relations", None)
    attributes = kwargs.pop("attributes", {})

    # update paths
    if paths is not None:
        model.paths = _update_paths(model.paths, paths)

    # update relations
    if relations is not None:
        with sa.session.no_autoflush:
            model.relations = _update_relations(model.relations, relations)

    # update scalar fields
    for k, v in kwargs.items():
        setattr(model, k, v)

    # update attributes
    for association in model.type_.fields:
        field = association.field
        try:
            value = attributes[field.field_id]
        except KeyError:
            continue
        attribute_class = field.type_.attribute_class
        query = attribute_class.query.filter_by(product=model, field=field)
        attr = query.one_or_none()
        if attr:
            attr.value = value
        else:
            attribute_class(
                name=field.name, field=field, product=model, value=value
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
