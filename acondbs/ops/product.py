import re
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
def camel_to_snake(name):
    # copied from https://stackoverflow.com/a/1176023/7309855
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def snake_to_camel(name):
    # copied from https://stackoverflow.com/a/1176023/7309855
    return "".join(w.title() for w in name.split("_"))


def _reshape_arg_attributes(attributes):
    return {
        snake_to_camel(t): {e["field_id"]: e["value"] for e in v}
        for t, v in attributes.items()
    }


##__________________________________________________________________||
def create_product(user, **kwargs):
    """Create a product"""

    type_id = kwargs.pop("type_id")
    paths = kwargs.pop("paths", [])
    relations = kwargs.pop("relations", [])
    attributes = kwargs.pop("attributes", {})

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

    attr_dict = _reshape_arg_attributes(attributes)

    for association in product_type.fields:
        field = association.field
        value = attr_dict.get(field.type_.name, {}).get(field.field_id)
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
    attr_dict = _reshape_arg_attributes(attributes)
    for association in model.type_.fields:
        field = association.field
        try:
            value = attr_dict[field.type_.name][field.field_id]
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
