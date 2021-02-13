import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..connection import CountedConnection
from ...models import (
    Product as ProductModel,
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
