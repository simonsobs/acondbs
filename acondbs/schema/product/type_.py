import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..connection import CountedConnection
from ...models import (
    Product as ProductModel,
    ProductType as ProductTypeModel,
    ProductFilePath as ProductFilePathModel,
    ProductRelation as ProductRelationModel,
    ProductRelationType as ProductRelationTypeModel
)
from ..filter_ import PFilterableConnectionField

##__________________________________________________________________||
class Product(SQLAlchemyObjectType):
    class Meta:
        model = ProductModel
        interfaces = (relay.Node, )
        connection_class = CountedConnection
        connection_field_factory = PFilterableConnectionField.factory

##__________________________________________________________________||
class ProductType(SQLAlchemyObjectType):
    '''A product type'''
    class Meta:
        model = ProductTypeModel
        interfaces = (graphene.relay.Node, )
        connection_class = CountedConnection
        connection_field_factory = PFilterableConnectionField.factory

##__________________________________________________________________||
class ProductRelation(SQLAlchemyObjectType):
    '''A relation from one product to another'''
    class Meta:
        model = ProductRelationModel
        interfaces = (graphene.relay.Node, )
        connection_class = CountedConnection
        connection_field_factory = PFilterableConnectionField.factory

##__________________________________________________________________||
class ProductRelationType(SQLAlchemyObjectType):
    '''A type of relations between products'''
    class Meta:
        model = ProductRelationTypeModel
        interfaces = (graphene.relay.Node, )
        connection_class = CountedConnection
        connection_field_factory = PFilterableConnectionField.factory

##__________________________________________________________________||
class ProductFilePath(SQLAlchemyObjectType):
    class Meta:
        model = ProductFilePathModel
        interfaces = (relay.Node, )
        connection_class = CountedConnection
        connection_field_factory = PFilterableConnectionField.factory

##__________________________________________________________________||