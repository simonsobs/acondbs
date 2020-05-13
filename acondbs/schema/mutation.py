import graphene

from .map_ import CreateMap, UpdateMap, DeleteMap
from .map_file_path import CreateMapFilePath, UpdateMapFilePath, DeleteMapFilePath

from .beam import CreateBeam, UpdateBeam, DeleteBeam
from .beam_file_path import CreateBeamFilePath, UpdateBeamFilePath, DeleteBeamFilePath

from .simulation import CreateSimulation, UpdateSimulation, DeleteSimulation

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

    create_beam_file_path = CreateBeamFilePath.Field()
    update_beam_file_path = UpdateBeamFilePath.Field()
    delete_beam_file_path = DeleteBeamFilePath.Field()

    create_simulation = CreateSimulation.Field()
    update_simulation = UpdateSimulation.Field()
    delete_simulation = DeleteSimulation.Field()

##__________________________________________________________________||
