import graphene
from graphene import relay
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import ProductFilePath as ProductFilePathModel

from ..db.sa import sa
from ..db.backup import request_backup_db

from .common import CommonCreateFilePathInputFields, CommonUpdateFilePathInputFields

##__________________________________________________________________||
class ProductFilePath(SQLAlchemyObjectType):
    class Meta:
        model = ProductFilePathModel
        interfaces = (relay.Node, )

##__________________________________________________________________||
class CreateProductFilePathInput(graphene.InputObjectType, CommonCreateFilePathInputFields):
    pass

class UpdateProductFilePathInput(graphene.InputObjectType, CommonUpdateFilePathInputFields):
    pass

class CreateProductFilePath(graphene.Mutation):
    class Arguments:
        input = CreateProductFilePathInput(required=True)

    ok = graphene.Boolean()
    productFilePath = graphene.Field(lambda: ProductFilePath)

    def mutate(root, info, input):
        path = ProductFilePathModel(**input)
        sa.session.add(path)
        sa.session.commit()
        ok = True
        request_backup_db()
        return CreateProductFilePath(productFilePath=path, ok=ok)

class UpdateProductFilePath(graphene.Mutation):
    class Arguments:
        path_id = graphene.Int()
        input = UpdateProductFilePathInput(required=True)

    ok = graphene.Boolean()
    productFilePath = graphene.Field(lambda: ProductFilePath)

    def mutate(root, info, path_id, input):
        path = ProductFilePathModel.query.filter_by(path_id=path_id).first()
        for k, v in input.items():
            setattr(path, k, v)
        sa.session.commit()
        ok = True
        request_backup_db()
        return UpdateProductFilePath(productFilePath=path, ok=ok)

class DeleteProductFilePath(graphene.Mutation):
    class Arguments:
        path_id = graphene.Int()

    ok = graphene.Boolean()

    def mutate(root, info, path_id):
        path = ProductFilePathModel.query.filter_by(path_id=path_id).first()
        sa.session.delete(path)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteProductFilePath(ok=ok)

##__________________________________________________________________||
