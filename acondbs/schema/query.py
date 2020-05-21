import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphene_sqlalchemy_filter import FilterableConnectionField, FilterSet

from .product import Product, ProductModel
from .product_file_path import ProductFilePath, ProductFilePathModel
from .product_type import ProductType, ProductTypeModel
from .product_relation_type import ProductRelationType, ProductRelationTypeModel
from .product_relation import ProductRelation, ProductRelationModel

##__________________________________________________________________||
class ProductFilter(FilterSet):
   class Meta:
       model = ProductModel
       fields = {
           'type_id': ['eq', ],
       }

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
        fields = ('type_id', 'name')
        query = ProductType.get_query(info)
        for f in fields:
            v = kwargs.get(f)
            if v is not None:
                query = query.filter(getattr(ProductTypeModel, f)==v)
                return query.first()
        return None

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
        fields = ('type_id', 'name')
        query = ProductRelationType.get_query(info)
        for f in fields:
            v = kwargs.get(f)
            if v is not None:
                query = query.filter(getattr(ProductRelationTypeModel, f)==v)
                return query.first()
        return None

    all_product_relations = FilterableConnectionField(ProductRelation._meta.connection)

##__________________________________________________________________||
