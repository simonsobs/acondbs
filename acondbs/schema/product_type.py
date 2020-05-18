from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import ProductType as ProductTypeModel

##__________________________________________________________________||
class ProductType(SQLAlchemyObjectType):
    class Meta:
        model = ProductTypeModel
        interfaces = (relay.Node, )

##__________________________________________________________________||
