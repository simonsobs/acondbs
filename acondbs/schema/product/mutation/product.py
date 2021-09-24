import datetime
import graphene

from ....models import (
    ProductType as ProductTypeModel,
    Product as ProductModel,
    ProductFilePath as ProductFilePathModel,
    ProductRelation as ProductRelationModel,
    ProductRelationType as ProductRelationTypeModel,
    AttributeUnicodeText as AttributeUnicodeTextModel,
    AttributeDate as AttributeDateModel,
)

from ....db.sa import sa
from ....db.backup import request_backup_db

from ...funcs import get_git_hub_viewer_from_info
from .. import type_


##__________________________________________________________________||
class RelationInputFields(graphene.InputObjectType):
    """A relation to another product"""

    product_id = graphene.Int(
        required=True, description="The product ID of the other product"
    )
    type_id = graphene.Int(required=True, description="The relation type ID")


class CommonInputFields:
    """Common input fields of mutations for creating and updating products"""

    contact = graphene.String(
        description=(
            "A person or group that can be contacted for questions or "
            "issues about the product."
        )
    )
    note = graphene.String(description="Note about the product in MarkDown.")
    paths = graphene.List(
        graphene.String,
        description="Paths to the products. e.g., nersc:/go/to/my/product_v3",
    )
    relations = graphene.InputField(
        graphene.List(RelationInputFields),
        description=("Relations to other products"),
    )


class CreateProductInput(graphene.InputObjectType, CommonInputFields):
    """Input to createProduct()"""

    type_id = graphene.Int(required=True, description="The product type ID")
    name = graphene.String(
        required=True, description="The name of the product"
    )
    date_produced = graphene.Date(
        description="The date on which the product was produced"
    )
    produced_by = graphene.String(
        description="The person or group that produced the product"
    )
    posted_by = graphene.String(
        description="The person who entered the DB entry."
    )


class UpdateProductInput(graphene.InputObjectType, CommonInputFields):
    """Input to updateProduct()"""

    updated_by = graphene.String(
        description="The person who updated the DB entry."
    )


##__________________________________________________________________||
class CreateProduct(graphene.Mutation):
    """Create a product"""

    class Arguments:
        input = CreateProductInput(
            required=True, description=("the input to createProduct()")
        )

    ok = graphene.Boolean()
    product = graphene.Field(lambda: type_.Product)

    def mutate(root, info, input):
        user = get_git_hub_viewer_from_info(info)
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
        sa.session.commit()
        ok = True
        request_backup_db()
        return CreateProduct(product=model, ok=ok)


class UpdateProduct(graphene.Mutation):
    """Update a product.

    Note: This is to update the DB entry about a product. If the
    product itself has been updated, a new entry should be added by
    createProduct()
    """

    class Arguments:
        product_id = graphene.Int(
            required=True,
            description="The productId of a product to be updated.",
        )
        input = UpdateProductInput(
            required=True, description="an input to updateProduct()"
        )

    ok = graphene.Boolean()
    product = graphene.Field(lambda: type_.Product)

    def mutate(root, info, product_id, input):
        user = get_git_hub_viewer_from_info(info)

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

        sa.session.commit()
        ok = True
        request_backup_db()
        return UpdateProduct(product=model, ok=ok)


class DeleteProduct(graphene.Mutation):
    """Delete a product"""

    class Arguments:
        product_id = graphene.Int(
            required=True,
            description="The productId of a product to be deleted.",
        )

    ok = graphene.Boolean()

    def mutate(root, info, product_id):
        model = ProductModel.query.filter_by(product_id=product_id).one()
        sa.session.delete(model)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteProduct(ok=ok)


##__________________________________________________________________||
