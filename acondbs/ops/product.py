import datetime

from ..models import (
    ProductType as ProductTypeModel,
    Product as ProductModel,
    ProductFilePath as ProductFilePathModel,
    ProductRelation as ProductRelationModel,
    ProductRelationType as ProductRelationTypeModel,
    AttributeUnicodeText as AttributeUnicodeTextModel,
    AttributeDate as AttributeDateModel,
)

from ..db.sa import sa


##__________________________________________________________________||
def create_product(user, input):
    """Create a product"""

    type_id = input.pop("type_id")
    product_type = ProductTypeModel.query.filter_by(type_id=type_id).one()
    paths = [ProductFilePathModel(path=p) for p in input.pop("paths", [])]
    with sa.session.no_autoflush:
        relations = [
            ProductRelationModel(
                type_=ProductRelationTypeModel.query.filter_by(
                    type_id=r["type_id"]
                ).one(),
                other=ProductModel.query.filter_by(
                    product_id=r["product_id"]
                ).one(),
            )
            for r in input.pop("relations", [])
        ]
    model = ProductModel(
        type_=product_type,
        posting_git_hub_user=user,
        paths=paths,
        relations=relations,
        **input
    )
    field_dict = {f.field.name: f.field for f in product_type.fields}
    columns_text = ["contact", "produced_by"]
    columns_date = ["date_produced"]
    for c in columns_text:
        AttributeUnicodeTextModel(
            name=c, field=field_dict[c], product=model, value=input.get(c)
        )
    for c in columns_date:
        AttributeDateModel(
            name=c, field=field_dict[c], product=model, value=input.get(c)
        )
    sa.session.add(model)
    return model


def update_product(user, product_id, input):
    """Update a product"""

    model = ProductModel.query.filter_by(product_id=product_id).one()

    # update paths
    input_paths = input.pop("paths", None)
    if input_paths is not None:
        pdict = {p.path: p for p in model.paths}
        model.paths = [
            pdict[p] if p in pdict else ProductFilePathModel(path=p)
            for p in input_paths
        ]

    # update relations
    input_relations = input.pop("relations", None)
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
                    type_ = ProductRelationTypeModel.query.filter_by(
                        type_id=r["type_id"]
                    ).one()
                    other = ProductModel.query.filter_by(
                        product_id=r["product_id"]
                    ).one()
                    m = ProductRelationModel(
                        self_=model, type_=type_, other=other
                    )
                    sa.session.add(m)
            for m in old_relations_dict.values():
                sa.session.delete(m)

    # update scalar fields
    for k, v in input.items():
        setattr(model, k, v)

    # update attributes
    field_dict = {f.field.name: f.field for f in model.type_.fields}
    columns_text = ["contact", "produced_by"]
    columns_date = ["date_produced"]
    attr_dict = {a.name: a for a in model.attributes_unicode_text}
    for c in columns_text:
        if c not in input:
            continue
        attr = attr_dict.get(c)
        if attr:
            attr.value = input[c]
        else:
            AttributeUnicodeTextModel(
                name=c, field=field_dict[c], product=model, value=input[c]
            )
    attr_dict = {a.name: a for a in model.attributes_date}
    for c in columns_date:
        if c not in input:
            continue
        attr = attr_dict.get(c)
        if attr:
            attr.value = input[c]
        else:
            AttributeDateModel(
                name=c, field=field_dict[c], product=model, value=input[c]
            )

    model.time_updated = datetime.datetime.now()
    model.updating_git_hub_user = user

    return model


def delete_product(product_id):
    """Delete a product"""

    model = ProductModel.query.filter_by(product_id=product_id).one()
    sa.session.delete(model)
    return


##__________________________________________________________________||
