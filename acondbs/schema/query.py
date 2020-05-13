import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField

from .simulation import Simulation, SimulationModel
from .map_ import Map, MapModel
from .beam import Beam, BeamModel
from .beam_file_path import BeamFilePath, BeamFilePathModel
from .map_file_path import MapFilePath, MapFilePathModel
from .simulation_file_path import SimulationFilePath, SimulationFilePathModel

##__________________________________________________________________||
class Query(graphene.ObjectType):

    version = graphene.String()

    def resolve_version(self, info):
        from .. import __version__
        return __version__

    node = relay.Node.Field()
    all_simulations = SQLAlchemyConnectionField(Simulation._meta.connection)
    all_maps = SQLAlchemyConnectionField(Map._meta.connection)
    all_beams = SQLAlchemyConnectionField(Beam._meta.connection)
    all_simulation_file_paths = SQLAlchemyConnectionField(SimulationFilePath._meta.connection)
    all_map_file_paths = SQLAlchemyConnectionField(MapFilePath._meta.connection)
    all_beam_file_paths = SQLAlchemyConnectionField(BeamFilePath._meta.connection)

    simulation = graphene.Field(Simulation, product_id=graphene.Int(), name=graphene.String())

    def resolve_simulation(self, info, **kwargs):
        import time, random
        # print(kwargs)
        # time.sleep(random.randint(1, 5))
        fields = ('product_id', 'name')
        query = Simulation.get_query(info)
        for f in fields:
            v = kwargs.get(f)
            if v is not None:
                query = query.filter(getattr(SimulationModel, f)==v)
                return query.first()
        return None

    map = graphene.Field(Map, product_id=graphene.Int(), name=graphene.String())

    def resolve_map(self, info, **kwargs):
        import time, random
        # print(kwargs)
        # time.sleep(random.randint(1, 5))
        fields = ('product_id', 'name')
        query = Map.get_query(info)
        for f in fields:
            v = kwargs.get(f)
            if v is not None:
                query = query.filter(getattr(MapModel, f)==v)
                return query.first()
        return None

    beam = graphene.Field(Beam, product_id=graphene.Int(), name=graphene.String())

    def resolve_beam(self, info, **kwargs):
        fields = ('product_id', 'name')
        query = Beam.get_query(info)
        for f in fields:
            v = kwargs.get(f)
            if v is not None:
                query = query.filter(getattr(BeamModel, f)==v)
                return query.first()
        return None
##__________________________________________________________________||
