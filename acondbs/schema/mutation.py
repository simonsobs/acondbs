import graphene

from .map_ import CreateMap, UpdateMap, DeleteMap
from .map_file_path import CreateMapFilePath, UpdateMapFilePath, DeleteMapFilePath

from .beam import CreateBeam, UpdateBeam, DeleteBeam
from .beam_file_path import CreateBeamFilePath, UpdateBeamFilePath, DeleteBeamFilePath

from .simulation import CreateSimulation, UpdateSimulation, DeleteSimulation
from .simulation_file_path import CreateSimulationFilePath, UpdateSimulationFilePath, DeleteSimulationFilePath

from .product import CreateProduct, UpdateProduct, DeleteProduct
from .product_file_path import CreateProductFilePath, UpdateProductFilePath, DeleteProductFilePath
from .product_type import CreateProductType, DeleteProductType
from .product_relation_type import CreateProductRelationType, DeleteProductRelationType

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

    create_simulation_file_path = CreateSimulationFilePath.Field()
    update_simulation_file_path = UpdateSimulationFilePath.Field()
    delete_simulation_file_path = DeleteSimulationFilePath.Field()

    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()

    create_product_file_path = CreateProductFilePath.Field()
    update_product_file_path = UpdateProductFilePath.Field()
    delete_product_file_path = DeleteProductFilePath.Field()

    create_product_type = CreateProductType.Field()
    delete_product_type = DeleteProductType.Field()

    create_product_relation_type = CreateProductRelationType.Field()
    delete_product_relation_type = DeleteProductRelationType.Field()

##__________________________________________________________________||
