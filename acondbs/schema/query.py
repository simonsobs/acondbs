import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphene_sqlalchemy_filter import FilterableConnectionField

from .product import Product, ProductModel
from .product_file_path import ProductFilePath, ProductFilePathModel
from .product_type import ProductType, ProductTypeModel
from .product_relation_type import ProductRelationType, ProductRelationTypeModel
from .product_relation import ProductRelation, ProductRelationModel

from .filter_ import ProductFilter

##__________________________________________________________________||
class Query(graphene.ObjectType):

    version = graphene.String()

    def resolve_version(self, info):
        from .. import __version__
        return __version__

    node = relay.Node.Field()

    all_product_types = FilterableConnectionField(ProductType._meta.connection)

    product_type = graphene.Field(ProductType, type_id=graphene.Int(), name=graphene.String())

    def resolve_product_type(self, info, **kwargs):
        filter = [getattr(ProductTypeModel, k)==v for k, v in kwargs.items()]
        # e.g., [ProductTypeModel.type_id == 1, ProductTypeModel.name == 'map']

        return ProductType.get_query(info).filter(*filter).one_or_none()

    all_products = FilterableConnectionField(Product._meta.connection, filters=ProductFilter())
    all_product_file_paths = FilterableConnectionField(ProductFilePath._meta.connection)

    product = graphene.Field(
        Product,
        product_id=graphene.Int(),
        type_id=graphene.Int(),
        name=graphene.String())

    def resolve_product(self, info, **kwargs):

        filter = [getattr(ProductModel, k)==v for k, v in kwargs.items()]
        # e.g., [ProductModel.type_id == 1, ProductModel.name == 'map_001']

        return Product.get_query(info).filter(*filter).one_or_none()

    all_product_relation_types = FilterableConnectionField(ProductRelationType._meta.connection)

    product_relation_type = graphene.Field(ProductRelationType, type_id=graphene.Int(), name=graphene.String())

    def resolve_product_relation_type(self, info, **kwargs):
        filter = [getattr(ProductRelationTypeModel, k)==v for k, v in kwargs.items()]
        return ProductRelationType.get_query(info).filter(*filter).one_or_none()

    all_product_relations = FilterableConnectionField(ProductRelation._meta.connection)

##__________________________________________________________________||
