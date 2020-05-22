import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import Product as ProductModel
from ..models import ProductType as ProductTypeModel

from ..db.sa import sa
from ..db.backup import request_backup_db

##__________________________________________________________________||
class ProductType(SQLAlchemyObjectType):
    class Meta:
        model = ProductTypeModel
        interfaces = (graphene.relay.Node, )

##__________________________________________________________________||
class CreateProductTypeInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    order = graphene.Int()
    indef_article = graphene.String()
    singular = graphene.String()
    plural = graphene.String()
    icon = graphene.String()

##__________________________________________________________________||
class CreateProductType(graphene.Mutation):
    class Arguments:
        input = CreateProductTypeInput(required=True)

    ok = graphene.Boolean()
    product_type = graphene.Field(lambda: ProductType)

    def mutate(root, info, input):
        product_type = ProductTypeModel(**input)
        sa.session.add(product_type)
        sa.session.commit()
        ok = True
        request_backup_db()
        return CreateProductType(product_type=product_type, ok=ok)

class DeleteProductType(graphene.Mutation):
    class Arguments:
        type_id = graphene.Int()

    ok = graphene.Boolean()

    def mutate(root, info, type_id):
        product_type = ProductTypeModel.query.filter_by(type_id=type_id).first()
        products = ProductModel.query.filter_by(type_id=type_id).all()
        if products:
            raise ValueError('Cannot delete the product type "{}". Products of this type exist'.format(product_type.name))
        sa.session.delete(product_type)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteProductType(ok=ok)

##__________________________________________________________________||
