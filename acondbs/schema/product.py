import datetime
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import Product as ProductModel
from ..models import ProductFilePath as ProductFilePathModel

from ..db.sa import sa
from ..db.backup import request_backup_db

from .filter_ import PFilterableConnectionField

##__________________________________________________________________||
class Product(SQLAlchemyObjectType):
    class Meta:
        model = ProductModel
        interfaces = (relay.Node, )
        connection_field_factory = PFilterableConnectionField.factory

# class ProductConnection(relay.Connection):
#     class Meta:
#         node = Product

## Product._meta.connection is used instead
## https://github.com/graphql-python/graphene-sqlalchemy/issues/153#issuecomment-478744077

##__________________________________________________________________||
class CommonInputFields:
    """Common input fields of mutations for creating and updating products

    """
    contact = graphene.String(
        description=('A person or group that can be contacted for questions or '
                     'issues about the product.'))
    note = graphene.String(description='Note about the product in MarkDown.')
    paths = graphene.List(
        graphene.String,
        description="Paths to the products. e.g., nersc:/go/to/my/product_v3"
    )

class CreateProductInput(graphene.InputObjectType, CommonInputFields):
    '''Input to createProduct()'''
    type_id = graphene.Int(required=True, description='The product type ID')
    name = graphene.String(required=True, description='The name of the product')
    date_produced = graphene.Date(description='The date on which the product was produced')
    produced_by = graphene.String(description='The person or group that produced the product')
    posted_by = graphene.String(description='The person who entered the DB entry.')

class UpdateProductInput(graphene.InputObjectType, CommonInputFields):
    updated_by = graphene.String()

##__________________________________________________________________||
class CreateProduct(graphene.Mutation):
    class Arguments:
        input = CreateProductInput(required=True)

    ok = graphene.Boolean()
    product = graphene.Field(lambda: Product)

    def mutate(root, info, input):
        paths = input.pop('paths', None)
        product = ProductModel(**input)
        if paths:
            product.paths = ([ProductFilePathModel(path=p) for p in paths])
        today = datetime.date.today()
        product.date_posted = today
        sa.session.add(product)
        sa.session.commit()
        ok = True
        request_backup_db()
        return CreateProduct(product=product, ok=ok)

class UpdateProduct(graphene.Mutation):
    class Arguments:
        product_id = graphene.Int()
        input = UpdateProductInput(required=True)

    ok = graphene.Boolean()
    product = graphene.Field(lambda: Product)

    def mutate(root, info, product_id, input):
        product = ProductModel.query.filter_by(product_id=product_id).first()
        for k, v in input.items():
            setattr(product, k, v)
        today = datetime.date.today()
        product.date_updated = today
        sa.session.commit()
        ok = True
        request_backup_db()
        return UpdateProduct(product=product, ok=ok)

class DeleteProduct(graphene.Mutation):
    class Arguments:
        product_id = graphene.Int()

    ok = graphene.Boolean()

    def mutate(root, info, product_id):
        product = ProductModel.query.filter_by(product_id=product_id).first()
        sa.session.delete(product)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteProduct(ok=ok)

##__________________________________________________________________||
