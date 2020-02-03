import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from .models import Map as MapModel
from .models import Beam as BeamModel
from .models import MapFilePath as MapFilePathModel

##__________________________________________________________________||
class Map(SQLAlchemyObjectType):
    class Meta:
        model = MapModel
        interfaces = (relay.Node, )


class MapConnection(relay.Connection):
    class Meta:
        node = Map

##__________________________________________________________________||
class Beam(SQLAlchemyObjectType):
    class Meta:
        model = BeamModel
        interfaces = (relay.Node, )


class BeamConnection(relay.Connection):
    class Meta:
        node = Beam

##__________________________________________________________________||
class MapFilePath(SQLAlchemyObjectType):
    class Meta:
        model = MapFilePathModel
        interfaces = (relay.Node, )

# class MapFilePathConnection(relay.Connection):
#     class Meta:
#         node = MapFilePath

##__________________________________________________________________||
class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_maps = SQLAlchemyConnectionField(MapConnection)
    all_beams = SQLAlchemyConnectionField(BeamConnection)
    # all_mapfilepaths = SQLAlchemyConnectionField(MapFilePathConnection)

schema = graphene.Schema(query=Query)

##__________________________________________________________________||
