import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField

from ..db import db

from .map_ import Map, MapModel, MapConnection, CreateMap, UpdateMap
from .beam import Beam, BeamModel
from .map_file_path import MapFilePath, MapFilePathModel

##__________________________________________________________________||
class Query(graphene.ObjectType):

    version = graphene.String()

    def resolve_version(self, info):
        from .. import __version__
        return __version__

    node = relay.Node.Field()
    all_maps = SQLAlchemyConnectionField(MapConnection)
    all_beams = SQLAlchemyConnectionField(Beam._meta.connection)
    all_map_file_paths = SQLAlchemyConnectionField(MapFilePath)

    map = graphene.Field(Map, map_id=graphene.Int(), name=graphene.String())

    def resolve_map(self, info, **kwargs):
        fields = ('map_id', 'name')
        query = Map.get_query(info)
        for f in fields:
            v = kwargs.get(f)
            if v is not None:
                query = query.filter(getattr(MapModel, f)==v)
                return query.first()
        return None

    beam = graphene.Field(Beam, beam_id=graphene.Int(), name=graphene.String())

    def resolve_beam(self, info, **kwargs):
        fields = ('beam_id', 'name')
        query = Beam.get_query(info)
        for f in fields:
            v = kwargs.get(f)
            if v is not None:
                query = query.filter(getattr(BeamModel, f)==v)
                return query.first()
        return None
##__________________________________________________________________||
class Mutation(graphene.ObjectType):
    create_map = CreateMap.Field()
    update_map = UpdateMap.Field()

##__________________________________________________________________||
schema = graphene.Schema(query=Query, mutation=Mutation, types=[Map, Beam, MapFilePath])

##__________________________________________________________________||
