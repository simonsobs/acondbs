import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from ...models import (
    Product as ProductModel,
    ProductType as ProductTypeModel
)

from ...db.sa import sa
from ...db.backup import request_backup_db

from ..connection import CountedConnection
from .filter_ import PFilterableConnectionField

##__________________________________________________________________||
class ProductType(SQLAlchemyObjectType):
    '''A product type'''
    class Meta:
        model = ProductTypeModel
        interfaces = (graphene.relay.Node, )
        connection_class = CountedConnection
        connection_field_factory = PFilterableConnectionField.factory

def resolve_product_type(parent, info, **kwargs):
    filter = [getattr(ProductTypeModel, k) == v for k, v in kwargs.items()]
    # e.g., [ProductTypeModel.type_id == 1, ProductTypeModel.name == 'map']

    return ProductType.get_query(info).filter(*filter).one_or_none()

product_type_field = graphene.Field(
    ProductType,
    type_id=graphene.Int(),
    name=graphene.String(),
    resolver=resolve_product_type)

all_product_types_field = PFilterableConnectionField(ProductType.connection)

##__________________________________________________________________||
class CommonInputFields:
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

class CreateProductTypeInput(graphene.InputObjectType, CommonInputFields):
    '''Input to createProductType()'''
    name = graphene.String(required=True, description='The name of the product type')

class UpdateProductTypeInput(graphene.InputObjectType,CommonInputFields):
    '''Input to updateProductType()'''

##__________________________________________________________________||
class CreateProductType(graphene.Mutation):
    '''Create a product type'''
    class Arguments:
        input = CreateProductTypeInput(required=True)

    ok = graphene.Boolean()
    product_type = graphene.Field(lambda: ProductType)

    def mutate(root, info, input):
        model = ProductTypeModel(**input)
        sa.session.add(model)
        sa.session.commit()
        ok = True
        request_backup_db()
        return CreateProductType(product_type=model, ok=ok)

class UpdateProductType(graphene.Mutation):
    '''Update a product type'''
    class Arguments:
        type_id = graphene.Int(required=True)
        input = UpdateProductTypeInput(required=True)

    ok = graphene.Boolean()
    product_type = graphene.Field(lambda: ProductType)

    def mutate(root, info, type_id, input):
        model = ProductTypeModel.query.filter_by(type_id=type_id).one()
        for k, v in input.items():
            setattr(model, k, v)
        sa.session.commit()
        ok = True
        request_backup_db()
        return UpdateProductType(product_type=model, ok=ok)

class DeleteProductType(graphene.Mutation):
    '''Delete a product type'''
    class Arguments:
        type_id = graphene.Int(description='The typeId of the product type')

    ok = graphene.Boolean()

    def mutate(root, info, type_id):
        model = ProductTypeModel.query.filter_by(type_id=type_id).one()
        sa.session.delete(model)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteProductType(ok=ok)

##__________________________________________________________________||
