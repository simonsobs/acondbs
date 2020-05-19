import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphene_sqlalchemy_filter import FilterableConnectionField, FilterSet

from .simulation import Simulation, SimulationModel
from .map_ import Map, MapModel
from .beam import Beam, BeamModel
from .beam_file_path import BeamFilePath, BeamFilePathModel
from .map_file_path import MapFilePath, MapFilePathModel
from .simulation_file_path import SimulationFilePath, SimulationFilePathModel

from .product import Product, ProductModel
from .product_file_path import ProductFilePath, ProductFilePathModel
from .product_type import ProductType, ProductTypeModel
from .product_relation_type import ProductRelationType, ProductRelationTypeModel

##__________________________________________________________________||
class ProductFilter(FilterSet):
   class Meta:
       model = ProductModel
       fields = {
           'product_type_id': ['eq', ],
       }

class MapFilter(FilterSet):
   class Meta:
       model = MapModel
       fields = {
           'name': ['eq', 'ne', 'in', 'ilike'],
           'date_produced': [...],
       }

##__________________________________________________________________||
class Query(graphene.ObjectType):

    version = graphene.String()

    def resolve_version(self, info):
        from .. import __version__
        return __version__

    node = relay.Node.Field()
    all_simulations = FilterableConnectionField(Simulation._meta.connection)
    all_maps = FilterableConnectionField(Map._meta.connection, filters=MapFilter())
    all_beams = FilterableConnectionField(Beam._meta.connection)
    all_simulation_file_paths = FilterableConnectionField(SimulationFilePath._meta.connection)
    all_map_file_paths = FilterableConnectionField(MapFilePath._meta.connection)
    all_beam_file_paths = FilterableConnectionField(BeamFilePath._meta.connection)

    all_product_types = FilterableConnectionField(ProductType._meta.connection)

    product_type = graphene.Field(ProductType, product_type_id=graphene.Int(), name=graphene.String())

    def resolve_product_type(self, info, **kwargs):
        fields = ('product_type_id', 'name')
        query = ProductType.get_query(info)
        for f in fields:
            v = kwargs.get(f)
            if v is not None:
                query = query.filter(getattr(ProductTypeModel, f)==v)
                return query.first()
        return None

    all_products = FilterableConnectionField(Product._meta.connection, filters=ProductFilter())
    all_product_file_paths = FilterableConnectionField(ProductFilePath._meta.connection)

    product = graphene.Field(Product, product_id=graphene.Int(), name=graphene.String())

    def resolve_product(self, info, **kwargs):
        import time, random
        # print(kwargs)
        # time.sleep(random.randint(1, 5))
        fields = ('product_id', 'name')
        query = Product.get_query(info)
        for f in fields:
            v = kwargs.get(f)
            if v is not None:
                query = query.filter(getattr(ProductModel, f)==v)
                return query.first()
        return None

    all_product_relation_types = FilterableConnectionField(ProductRelationType._meta.connection)

    product_relation_type = graphene.Field(ProductRelationType, type_id=graphene.Int(), name=graphene.String())

    def resolve_product_relation_type(self, info, **kwargs):
        fields = ('type_id', 'name')
        query = ProductRelationType.get_query(info)
        for f in fields:
            v = kwargs.get(f)
            if v is not None:
                query = query.filter(getattr(ProductRelationTypeModel, f)==v)
                return query.first()
        return None

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
