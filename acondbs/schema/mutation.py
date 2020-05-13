import graphene

from .map_ import CreateMap, UpdateMap, DeleteMap
from .map_file_path import CreateMapFilePath, UpdateMapFilePath, DeleteMapFilePath

from .beam import CreateBeam, UpdateBeam, DeleteBeam

from .query import Query

##__________________________________________________________________||
class Mutation(graphene.ObjectType):
    create_map = CreateMap.Field()
    update_map = UpdateMap.Field()
    delete_map = DeleteMap.Field()

    create_map_file_path = CreateMapFilePath.Field()
    update_map_file_path = UpdateMapFilePath.Field()
    delete_map_file_path = DeleteMapFilePath.Field()

    create_beam = CreateBeam.Field()
    update_beam = UpdateBeam.Field()
    delete_beam = DeleteBeam.Field()

##__________________________________________________________________||
