import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import Product as ProductModel
from ..models import ProductRelation as ProductRelationModel

from ..db.sa import sa
from ..db.backup import request_backup_db

##__________________________________________________________________||
class ProductRelation(SQLAlchemyObjectType):
    class Meta:
        model = ProductRelationModel
        interfaces = (graphene.relay.Node, )

##__________________________________________________________________||
