import graphene

from ...funcs import get_git_hub_viewer_from_info
from .. import type_

from .... import ops

from ....db.backup import request_backup_db


##__________________________________________________________________||
class RelationInputFields(graphene.InputObjectType):
    """A relation to another product"""

    product_id = graphene.Int(
        required=True,
        description="The product ID of the other product",
    )
    type_id = graphene.Int(
        required=True,
        description="The relation type ID",
    )


class CommonInputFields:
    """Common input fields of mutations for creating and updating products"""

    contact = graphene.String(
        description=(
            "A person or group that can be contacted for questions or "
            "issues about the product."
        )
    )
    note = graphene.String(
        description="Note about the product in MarkDown.",
    )
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

    type_id = graphene.Int(
        required=True,
        description="The product type ID",
    )
    name = graphene.String(
        required=True,
        description="The name of the product",
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
            required=True,
            description="the input to createProduct()",
        )

    ok = graphene.Boolean()
    product = graphene.Field(lambda: type_.Product)

    def mutate(root, info, input):
        user = get_git_hub_viewer_from_info(info)
        model = ops.create_product(user, input)
        ops.commit()
        request_backup_db()
        ok = True
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
            required=True,
            description="an input to updateProduct()",
        )

    ok = graphene.Boolean()
    product = graphene.Field(lambda: type_.Product)

    def mutate(root, info, product_id, input):
        user = get_git_hub_viewer_from_info(info)
        model = ops.update_product(user, product_id, input)
        ops.commit()
        request_backup_db()
        ok = True
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
        ops.delete_product(product_id)
        ops.commit()
        request_backup_db()
        ok = True
        return DeleteProduct(ok=ok)


##__________________________________________________________________||
