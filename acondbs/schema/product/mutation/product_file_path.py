import graphene

from ....models import ProductFilePath as ProductFilePathModel

from ....db.sa import sa

from .. import type_

from .... import ops


##__________________________________________________________________||
class CommonInputFields:
    """Common input fields of mutations for creating and updating file paths"""

    path = graphene.String()
    note = graphene.String()


class CreateProductFilePathInput(graphene.InputObjectType, CommonInputFields):
    product_id = graphene.Int()


class UpdateProductFilePathInput(graphene.InputObjectType, CommonInputFields):
    pass


##__________________________________________________________________||
class CreateProductFilePath(graphene.Mutation):
    class Arguments:
        input = CreateProductFilePathInput(required=True)

    ok = graphene.Boolean()
    productFilePath = graphene.Field(lambda: type_.ProductFilePath)

    def mutate(root, info, input):
        path = ProductFilePathModel(**input)
        sa.session.add(path)
        ops.commit()
        ok = True
        return CreateProductFilePath(productFilePath=path, ok=ok)


class UpdateProductFilePath(graphene.Mutation):
    class Arguments:
        path_id = graphene.Int()
        input = UpdateProductFilePathInput(required=True)

    ok = graphene.Boolean()
    productFilePath = graphene.Field(lambda: type_.ProductFilePath)

    def mutate(root, info, path_id, input):
        path = ProductFilePathModel.query.filter_by(path_id=path_id).first()
        for k, v in input.items():
            setattr(path, k, v)
        ops.commit()
        ok = True
        return UpdateProductFilePath(productFilePath=path, ok=ok)


class DeleteProductFilePath(graphene.Mutation):
    class Arguments:
        path_id = graphene.Int()

    ok = graphene.Boolean()

    def mutate(root, info, path_id):
        path = ProductFilePathModel.query.filter_by(path_id=path_id).first()
        sa.session.delete(path)
        ops.commit()
        ok = True
        return DeleteProductFilePath(ok=ok)


##__________________________________________________________________||
