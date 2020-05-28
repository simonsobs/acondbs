import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import Product as ProductModel
from ..models import ProductType as ProductTypeModel

from ..db.sa import sa
from ..db.backup import request_backup_db

from .filter_ import PFilterableConnectionField

##__________________________________________________________________||
class ProductType(SQLAlchemyObjectType):
    '''A product type'''
    class Meta:
        model = ProductTypeModel
        interfaces = (graphene.relay.Node, )
        connection_field_factory = PFilterableConnectionField.factory

##__________________________________________________________________||
class CreateProductTypeInput(graphene.InputObjectType):
    '''Input to createProductType()'''
    name = graphene.String(required=True, description='The name of the product type')
    order = graphene.Int(
        description=('The order in which the type is displayed, for example, '
                     'in navigation bars.'))
    indef_article = graphene.String(
        description=('The indefinite article placed before the singular noun "'
                     'i.e., "a" or "an". '))
    singular = graphene.String(
        description=('The singular noun, the product type name in singular.'))
    plural = graphene.String(
        description=('The plural noun, the product type name in plural.'))
    icon = graphene.String(
        description=('A name of the icon from https://materialdesignicons.com/'))

##__________________________________________________________________||
class CreateProductType(graphene.Mutation):
    '''Create a product type'''
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
    '''Delete a product type'''
    class Arguments:
        type_id = graphene.Int(description='The typeId of the product type')

    ok = graphene.Boolean()

    def mutate(root, info, type_id):
        product_type = ProductTypeModel.query.filter_by(type_id=type_id).first()
        sa.session.delete(product_type)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteProductType(ok=ok)

##__________________________________________________________________||
