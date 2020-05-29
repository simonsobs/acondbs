import datetime
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import Product as ProductModel
from ..models import ProductFilePath as ProductFilePathModel
from ..models import ProductRelation as ProductRelationModel
from ..models import ProductRelationType as ProductRelationTypeModel

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
class RelationInputFields(graphene.InputObjectType):
    '''A relation to another product'''
    product_id = graphene.Int(required=True, description='The product ID of the other product')
    type_id = graphene.Int(required=True, description='The relation type ID')

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
    relations = graphene.InputField(
        graphene.List(RelationInputFields),
        description=('Relations to other products')
    )

class UpdateProductInput(graphene.InputObjectType, CommonInputFields):
    '''Input to updateProduct()'''
    updated_by = graphene.String(description='The person who updated the DB entry.')

##__________________________________________________________________||
class CreateProduct(graphene.Mutation):
    '''Create a product'''
    class Arguments:
        input = CreateProductInput(
            required=True,
            description=('the input to createProduct()')
        )

    ok = graphene.Boolean()
    product = graphene.Field(lambda: Product)

    def mutate(root, info, input):
        paths = [ProductFilePathModel(path=p) for p in input.pop('paths', [])]
        with sa.session.no_autoflush:
            relations = [
                ProductRelationModel(
                    type_=ProductRelationTypeModel.query.filter_by(type_id=r['type_id']).one(),
                    other=ProductModel.query.filter_by(product_id=r['product_id']).one()
                )
                for r in input.pop('relations', [])
            ]
        product = ProductModel(
            date_posted=datetime.date.today(),
            paths=paths,
            relations=relations,
            **input
        )
        sa.session.add(product)
        sa.session.commit()
        ok = True
        request_backup_db()
        return CreateProduct(product=product, ok=ok)

class UpdateProduct(graphene.Mutation):
    '''Update a product. Note: This is to update the DB entry about a product. If the
    product itself has been updated, a new entry should be added by
    createProduct()

    '''
    class Arguments:
        product_id = graphene.Int(
            required=True,
            description='The productId of a product to be updated.')
        input = UpdateProductInput(
            required=True,
            description='an input to updateProduct()'
        )

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
    '''Delete a product'''
    class Arguments:
        product_id = graphene.Int(
            required=True,
            description='The productId of a product to be deleted.')

    ok = graphene.Boolean()

    def mutate(root, info, product_id):
        product = ProductModel.query.filter_by(product_id=product_id).first()
        sa.session.delete(product)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteProduct(ok=ok)

##__________________________________________________________________||
