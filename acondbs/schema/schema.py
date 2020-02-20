import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from ..models import Map as MapModel
from ..models import Beam as BeamModel
from ..models import MapFilePath as MapFilePathModel

from ..db import db

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

# class BeamConnection(relay.Connection):
#      class Meta:
#          node = Beam

## The class "BeamConnection" is commented out because it causes the error
## "AssertionError: Found different types with the same name in the schema:
## BeamConnection, BeamConnection". In the class "Query" below
## "Beam._meta.connection" is used instead. This solution was mentioned in the
## issue
## https://github.com/graphql-python/graphene-sqlalchemy/issues/153#issuecomment-478744077

##__________________________________________________________________||
class MapFilePath(SQLAlchemyObjectType):
    class Meta:
        model = MapFilePathModel
        interfaces = (relay.Node, )

# class MapFilePathConnection(relay.Connection):
#     class Meta:
#         node = MapFilePath

##__________________________________________________________________||
class MapAttribute:
    name = graphene.String()
    date_posted = graphene.Date()
    mapper = graphene.String()
    note = graphene.String()

class CreateMapInput(graphene.InputObjectType, MapAttribute):
    name = graphene.String(required=True)

class UpdateMapInput(graphene.InputObjectType, MapAttribute):
    pass

class CreateMap(graphene.Mutation):
    class Arguments:
        input = CreateMapInput(required=True)

    ok = graphene.Boolean()
    map = graphene.Field(lambda: Map)

    def mutate(root, info, input):
        map = MapModel(name=input.name)
        db.session.add(map)
        db.session.commit()
        ok = True
        return CreateMap(map=map, ok=ok)

class UpdateMap(graphene.Mutation):
    class Arguments:
        map_id = graphene.Int()
        input = UpdateMapInput(required=True)

    ok = graphene.Boolean()
    map = graphene.Field(lambda: Map)

    def mutate(root, info, map_id, input):
        map = MapModel.query.filter_by(map_id=map_id).first()
        map.name = input.name
        db.session.commit()
        ok = True
        return CreateMap(map=map, ok=ok)

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
