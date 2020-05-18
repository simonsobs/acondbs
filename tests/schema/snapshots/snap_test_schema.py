# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_types 1'] = {
    'data': {
        '__schema': {
            'types': [
                {
                    'fields': [
                        {
                            'name': 'version',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'node',
                            'type': {
                                'name': 'Node'
                            }
                        },
                        {
                            'name': 'allSimulations',
                            'type': {
                                'name': 'SimulationConnection'
                            }
                        },
                        {
                            'name': 'allMaps',
                            'type': {
                                'name': 'MapConnection'
                            }
                        },
                        {
                            'name': 'allBeams',
                            'type': {
                                'name': 'BeamConnection'
                            }
                        },
                        {
                            'name': 'allSimulationFilePaths',
                            'type': {
                                'name': 'SimulationFilePathConnection'
                            }
                        },
                        {
                            'name': 'allMapFilePaths',
                            'type': {
                                'name': 'MapFilePathConnection'
                            }
                        },
                        {
                            'name': 'allBeamFilePaths',
                            'type': {
                                'name': 'BeamFilePathConnection'
                            }
                        },
                        {
                            'name': 'allProductTypes',
                            'type': {
                                'name': 'ProductTypeConnection'
                            }
                        },
                        {
                            'name': 'productType',
                            'type': {
                                'name': 'ProductType'
                            }
                        },
                        {
                            'name': 'allProducts',
                            'type': {
                                'name': 'ProductConnection'
                            }
                        },
                        {
                            'name': 'allProductFilePaths',
                            'type': {
                                'name': 'ProductFilePathConnection'
                            }
                        },
                        {
                            'name': 'product',
                            'type': {
                                'name': 'Product'
                            }
                        },
                        {
                            'name': 'simulation',
                            'type': {
                                'name': 'Simulation'
                            }
                        },
                        {
                            'name': 'map',
                            'type': {
                                'name': 'Map'
                            }
                        },
                        {
                            'name': 'beam',
                            'type': {
                                'name': 'Beam'
                            }
                        }
                    ],
                    'name': 'Query'
                },
                {
                    'fields': None,
                    'name': 'String'
                },
                {
                    'fields': [
                        {
                            'name': 'id',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'Node'
                },
                {
                    'fields': None,
                    'name': 'ID'
                },
                {
                    'fields': [
                        {
                            'name': 'pageInfo',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'edges',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'SimulationConnection'
                },
                {
                    'fields': [
                        {
                            'name': 'hasNextPage',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'hasPreviousPage',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'startCursor',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'endCursor',
                            'type': {
                                'name': 'String'
                            }
                        }
                    ],
                    'name': 'PageInfo'
                },
                {
                    'fields': None,
                    'name': 'Boolean'
                },
                {
                    'fields': [
                        {
                            'name': 'node',
                            'type': {
                                'name': 'Simulation'
                            }
                        },
                        {
                            'name': 'cursor',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'SimulationEdge'
                },
                {
                    'fields': [
                        {
                            'name': 'productId',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'name',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'contact',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'dateProduced',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'producedBy',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'datePosted',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'postedBy',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'dateUpdated',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'updatedBy',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'note',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'paths',
                            'type': {
                                'name': 'SimulationFilePathConnection'
                            }
                        },
                        {
                            'name': 'id',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'Simulation'
                },
                {
                    'fields': [
                        {
                            'name': 'pageInfo',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'edges',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'SimulationFilePathConnection'
                },
                {
                    'fields': [
                        {
                            'name': 'node',
                            'type': {
                                'name': 'SimulationFilePath'
                            }
                        },
                        {
                            'name': 'cursor',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'SimulationFilePathEdge'
                },
                {
                    'fields': [
                        {
                            'name': 'pathId',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'path',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'note',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'productId',
                            'type': {
                                'name': 'Int'
                            }
                        },
                        {
                            'name': 'product',
                            'type': {
                                'name': 'Simulation'
                            }
                        },
                        {
                            'name': 'id',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'SimulationFilePath'
                },
                {
                    'fields': None,
                    'name': 'Int'
                },
                {
                    'fields': None,
                    'name': 'SimulationSortEnum'
                },
                {
                    'fields': [
                        {
                            'name': 'pageInfo',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'edges',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'MapConnection'
                },
                {
                    'fields': [
                        {
                            'name': 'node',
                            'type': {
                                'name': 'Map'
                            }
                        },
                        {
                            'name': 'cursor',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'MapEdge'
                },
                {
                    'fields': [
                        {
                            'name': 'productId',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'name',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'contact',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'dateProduced',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'producedBy',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'datePosted',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'postedBy',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'dateUpdated',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'updatedBy',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'note',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'paths',
                            'type': {
                                'name': 'MapFilePathConnection'
                            }
                        },
                        {
                            'name': 'beams',
                            'type': {
                                'name': 'BeamConnection'
                            }
                        },
                        {
                            'name': 'id',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'Map'
                },
                {
                    'fields': [
                        {
                            'name': 'pageInfo',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'edges',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'MapFilePathConnection'
                },
                {
                    'fields': [
                        {
                            'name': 'node',
                            'type': {
                                'name': 'MapFilePath'
                            }
                        },
                        {
                            'name': 'cursor',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'MapFilePathEdge'
                },
                {
                    'fields': [
                        {
                            'name': 'pathId',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'path',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'note',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'productId',
                            'type': {
                                'name': 'Int'
                            }
                        },
                        {
                            'name': 'product',
                            'type': {
                                'name': 'Map'
                            }
                        },
                        {
                            'name': 'id',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'MapFilePath'
                },
                {
                    'fields': [
                        {
                            'name': 'pageInfo',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'edges',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'BeamConnection'
                },
                {
                    'fields': [
                        {
                            'name': 'node',
                            'type': {
                                'name': 'Beam'
                            }
                        },
                        {
                            'name': 'cursor',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'BeamEdge'
                },
                {
                    'fields': [
                        {
                            'name': 'productId',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'name',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'contact',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'dateProduced',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'producedBy',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'datePosted',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'postedBy',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'dateUpdated',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'updatedBy',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'note',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'inputMapProductId',
                            'type': {
                                'name': 'Int'
                            }
                        },
                        {
                            'name': 'inputBeamProductId',
                            'type': {
                                'name': 'Int'
                            }
                        },
                        {
                            'name': 'map',
                            'type': {
                                'name': 'Map'
                            }
                        },
                        {
                            'name': 'parentBeam',
                            'type': {
                                'name': 'Beam'
                            }
                        },
                        {
                            'name': 'childBeams',
                            'type': {
                                'name': 'BeamConnection'
                            }
                        },
                        {
                            'name': 'paths',
                            'type': {
                                'name': 'BeamFilePathConnection'
                            }
                        },
                        {
                            'name': 'id',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'Beam'
                },
                {
                    'fields': [
                        {
                            'name': 'pageInfo',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'edges',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'BeamFilePathConnection'
                },
                {
                    'fields': [
                        {
                            'name': 'node',
                            'type': {
                                'name': 'BeamFilePath'
                            }
                        },
                        {
                            'name': 'cursor',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'BeamFilePathEdge'
                },
                {
                    'fields': [
                        {
                            'name': 'pathId',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'path',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'note',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'productId',
                            'type': {
                                'name': 'Int'
                            }
                        },
                        {
                            'name': 'product',
                            'type': {
                                'name': 'Beam'
                            }
                        },
                        {
                            'name': 'id',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'BeamFilePath'
                },
                {
                    'fields': None,
                    'name': 'MapFilter'
                },
                {
                    'fields': None,
                    'name': 'StringRange'
                },
                {
                    'fields': None,
                    'name': 'MapSortEnum'
                },
                {
                    'fields': None,
                    'name': 'BeamSortEnum'
                },
                {
                    'fields': None,
                    'name': 'SimulationFilePathSortEnum'
                },
                {
                    'fields': None,
                    'name': 'MapFilePathSortEnum'
                },
                {
                    'fields': None,
                    'name': 'BeamFilePathSortEnum'
                },
                {
                    'fields': [
                        {
                            'name': 'pageInfo',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'edges',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'ProductTypeConnection'
                },
                {
                    'fields': [
                        {
                            'name': 'node',
                            'type': {
                                'name': 'ProductType'
                            }
                        },
                        {
                            'name': 'cursor',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'ProductTypeEdge'
                },
                {
                    'fields': [
                        {
                            'name': 'productTypeId',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'name',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'products',
                            'type': {
                                'name': 'ProductConnection'
                            }
                        },
                        {
                            'name': 'id',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'ProductType'
                },
                {
                    'fields': [
                        {
                            'name': 'pageInfo',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'edges',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'ProductConnection'
                },
                {
                    'fields': [
                        {
                            'name': 'node',
                            'type': {
                                'name': 'Product'
                            }
                        },
                        {
                            'name': 'cursor',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'ProductEdge'
                },
                {
                    'fields': [
                        {
                            'name': 'productId',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'productTypeId',
                            'type': {
                                'name': 'Int'
                            }
                        },
                        {
                            'name': 'name',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'contact',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'dateProduced',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'producedBy',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'datePosted',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'postedBy',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'dateUpdated',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'updatedBy',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'note',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'productType',
                            'type': {
                                'name': 'ProductType'
                            }
                        },
                        {
                            'name': 'paths',
                            'type': {
                                'name': 'ProductFilePathConnection'
                            }
                        },
                        {
                            'name': 'id',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'Product'
                },
                {
                    'fields': [
                        {
                            'name': 'pageInfo',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'edges',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'ProductFilePathConnection'
                },
                {
                    'fields': [
                        {
                            'name': 'node',
                            'type': {
                                'name': 'ProductFilePath'
                            }
                        },
                        {
                            'name': 'cursor',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'ProductFilePathEdge'
                },
                {
                    'fields': [
                        {
                            'name': 'pathId',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'path',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'note',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'productId',
                            'type': {
                                'name': 'Int'
                            }
                        },
                        {
                            'name': 'product',
                            'type': {
                                'name': 'Product'
                            }
                        },
                        {
                            'name': 'id',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'ProductFilePath'
                },
                {
                    'fields': None,
                    'name': 'ProductTypeSortEnum'
                },
                {
                    'fields': None,
                    'name': 'ProductFilter'
                },
                {
                    'fields': None,
                    'name': 'ProductSortEnum'
                },
                {
                    'fields': None,
                    'name': 'ProductFilePathSortEnum'
                },
                {
                    'fields': [
                        {
                            'name': 'createMap',
                            'type': {
                                'name': 'CreateMap'
                            }
                        },
                        {
                            'name': 'updateMap',
                            'type': {
                                'name': 'UpdateMap'
                            }
                        },
                        {
                            'name': 'deleteMap',
                            'type': {
                                'name': 'DeleteMap'
                            }
                        },
                        {
                            'name': 'createMapFilePath',
                            'type': {
                                'name': 'CreateMapFilePath'
                            }
                        },
                        {
                            'name': 'updateMapFilePath',
                            'type': {
                                'name': 'UpdateMapFilePath'
                            }
                        },
                        {
                            'name': 'deleteMapFilePath',
                            'type': {
                                'name': 'DeleteMapFilePath'
                            }
                        },
                        {
                            'name': 'createBeam',
                            'type': {
                                'name': 'CreateBeam'
                            }
                        },
                        {
                            'name': 'updateBeam',
                            'type': {
                                'name': 'UpdateBeam'
                            }
                        },
                        {
                            'name': 'deleteBeam',
                            'type': {
                                'name': 'DeleteBeam'
                            }
                        },
                        {
                            'name': 'createBeamFilePath',
                            'type': {
                                'name': 'CreateBeamFilePath'
                            }
                        },
                        {
                            'name': 'updateBeamFilePath',
                            'type': {
                                'name': 'UpdateBeamFilePath'
                            }
                        },
                        {
                            'name': 'deleteBeamFilePath',
                            'type': {
                                'name': 'DeleteBeamFilePath'
                            }
                        },
                        {
                            'name': 'createSimulation',
                            'type': {
                                'name': 'CreateSimulation'
                            }
                        },
                        {
                            'name': 'updateSimulation',
                            'type': {
                                'name': 'UpdateSimulation'
                            }
                        },
                        {
                            'name': 'deleteSimulation',
                            'type': {
                                'name': 'DeleteSimulation'
                            }
                        },
                        {
                            'name': 'createSimulationFilePath',
                            'type': {
                                'name': 'CreateSimulationFilePath'
                            }
                        },
                        {
                            'name': 'updateSimulationFilePath',
                            'type': {
                                'name': 'UpdateSimulationFilePath'
                            }
                        },
                        {
                            'name': 'deleteSimulationFilePath',
                            'type': {
                                'name': 'DeleteSimulationFilePath'
                            }
                        },
                        {
                            'name': 'createProduct',
                            'type': {
                                'name': 'CreateProduct'
                            }
                        },
                        {
                            'name': 'updateProduct',
                            'type': {
                                'name': 'UpdateProduct'
                            }
                        },
                        {
                            'name': 'deleteProduct',
                            'type': {
                                'name': 'DeleteProduct'
                            }
                        },
                        {
                            'name': 'createProductFilePath',
                            'type': {
                                'name': 'CreateProductFilePath'
                            }
                        },
                        {
                            'name': 'updateProductFilePath',
                            'type': {
                                'name': 'UpdateProductFilePath'
                            }
                        },
                        {
                            'name': 'deleteProductFilePath',
                            'type': {
                                'name': 'DeleteProductFilePath'
                            }
                        },
                        {
                            'name': 'createProductType',
                            'type': {
                                'name': 'CreateProductType'
                            }
                        },
                        {
                            'name': 'deleteProductType',
                            'type': {
                                'name': 'DeleteProductType'
                            }
                        }
                    ],
                    'name': 'Mutation'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        },
                        {
                            'name': 'map',
                            'type': {
                                'name': 'Map'
                            }
                        }
                    ],
                    'name': 'CreateMap'
                },
                {
                    'fields': None,
                    'name': 'CreateMapInput'
                },
                {
                    'fields': None,
                    'name': 'Date'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        },
                        {
                            'name': 'map',
                            'type': {
                                'name': 'Map'
                            }
                        }
                    ],
                    'name': 'UpdateMap'
                },
                {
                    'fields': None,
                    'name': 'UpdateMapInput'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        }
                    ],
                    'name': 'DeleteMap'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        },
                        {
                            'name': 'mapFilePath',
                            'type': {
                                'name': 'MapFilePath'
                            }
                        }
                    ],
                    'name': 'CreateMapFilePath'
                },
                {
                    'fields': None,
                    'name': 'CreateMapFilePathInput'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        },
                        {
                            'name': 'mapFilePath',
                            'type': {
                                'name': 'MapFilePath'
                            }
                        }
                    ],
                    'name': 'UpdateMapFilePath'
                },
                {
                    'fields': None,
                    'name': 'UpdateMapFilePathInput'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        }
                    ],
                    'name': 'DeleteMapFilePath'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        },
                        {
                            'name': 'beam',
                            'type': {
                                'name': 'Beam'
                            }
                        }
                    ],
                    'name': 'CreateBeam'
                },
                {
                    'fields': None,
                    'name': 'CreateBeamInput'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        },
                        {
                            'name': 'beam',
                            'type': {
                                'name': 'Beam'
                            }
                        }
                    ],
                    'name': 'UpdateBeam'
                },
                {
                    'fields': None,
                    'name': 'UpdateBeamInput'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        }
                    ],
                    'name': 'DeleteBeam'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        },
                        {
                            'name': 'beamFilePath',
                            'type': {
                                'name': 'BeamFilePath'
                            }
                        }
                    ],
                    'name': 'CreateBeamFilePath'
                },
                {
                    'fields': None,
                    'name': 'CreateBeamFilePathInput'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        },
                        {
                            'name': 'beamFilePath',
                            'type': {
                                'name': 'BeamFilePath'
                            }
                        }
                    ],
                    'name': 'UpdateBeamFilePath'
                },
                {
                    'fields': None,
                    'name': 'UpdateBeamFilePathInput'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        }
                    ],
                    'name': 'DeleteBeamFilePath'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        },
                        {
                            'name': 'simulation',
                            'type': {
                                'name': 'Simulation'
                            }
                        }
                    ],
                    'name': 'CreateSimulation'
                },
                {
                    'fields': None,
                    'name': 'CreateSimulationInput'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        },
                        {
                            'name': 'simulation',
                            'type': {
                                'name': 'Simulation'
                            }
                        }
                    ],
                    'name': 'UpdateSimulation'
                },
                {
                    'fields': None,
                    'name': 'UpdateSimulationInput'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        }
                    ],
                    'name': 'DeleteSimulation'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        },
                        {
                            'name': 'simulationFilePath',
                            'type': {
                                'name': 'SimulationFilePath'
                            }
                        }
                    ],
                    'name': 'CreateSimulationFilePath'
                },
                {
                    'fields': None,
                    'name': 'CreateSimulationFilePathInput'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        },
                        {
                            'name': 'simulationFilePath',
                            'type': {
                                'name': 'SimulationFilePath'
                            }
                        }
                    ],
                    'name': 'UpdateSimulationFilePath'
                },
                {
                    'fields': None,
                    'name': 'UpdateSimulationFilePathInput'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        }
                    ],
                    'name': 'DeleteSimulationFilePath'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        },
                        {
                            'name': 'product',
                            'type': {
                                'name': 'Product'
                            }
                        }
                    ],
                    'name': 'CreateProduct'
                },
                {
                    'fields': None,
                    'name': 'CreateProductInput'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        },
                        {
                            'name': 'product',
                            'type': {
                                'name': 'Product'
                            }
                        }
                    ],
                    'name': 'UpdateProduct'
                },
                {
                    'fields': None,
                    'name': 'UpdateProductInput'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        }
                    ],
                    'name': 'DeleteProduct'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        },
                        {
                            'name': 'productFilePath',
                            'type': {
                                'name': 'ProductFilePath'
                            }
                        }
                    ],
                    'name': 'CreateProductFilePath'
                },
                {
                    'fields': None,
                    'name': 'CreateProductFilePathInput'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        },
                        {
                            'name': 'productFilePath',
                            'type': {
                                'name': 'ProductFilePath'
                            }
                        }
                    ],
                    'name': 'UpdateProductFilePath'
                },
                {
                    'fields': None,
                    'name': 'UpdateProductFilePathInput'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        }
                    ],
                    'name': 'DeleteProductFilePath'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        },
                        {
                            'name': 'productType',
                            'type': {
                                'name': 'ProductType'
                            }
                        }
                    ],
                    'name': 'CreateProductType'
                },
                {
                    'fields': None,
                    'name': 'CreateProductTypeInput'
                },
                {
                    'fields': [
                        {
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        }
                    ],
                    'name': 'DeleteProductType'
                },
                {
                    'fields': [
                        {
                            'name': 'types',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'queryType',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'mutationType',
                            'type': {
                                'name': '__Type'
                            }
                        },
                        {
                            'name': 'subscriptionType',
                            'type': {
                                'name': '__Type'
                            }
                        },
                        {
                            'name': 'directives',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': '__Schema'
                },
                {
                    'fields': [
                        {
                            'name': 'kind',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'name',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'description',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'fields',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'interfaces',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'possibleTypes',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'enumValues',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'inputFields',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'ofType',
                            'type': {
                                'name': '__Type'
                            }
                        }
                    ],
                    'name': '__Type'
                },
                {
                    'fields': None,
                    'name': '__TypeKind'
                },
                {
                    'fields': [
                        {
                            'name': 'name',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'description',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'args',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'type',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'isDeprecated',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'deprecationReason',
                            'type': {
                                'name': 'String'
                            }
                        }
                    ],
                    'name': '__Field'
                },
                {
                    'fields': [
                        {
                            'name': 'name',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'description',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'type',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'defaultValue',
                            'type': {
                                'name': 'String'
                            }
                        }
                    ],
                    'name': '__InputValue'
                },
                {
                    'fields': [
                        {
                            'name': 'name',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'description',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'isDeprecated',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'deprecationReason',
                            'type': {
                                'name': 'String'
                            }
                        }
                    ],
                    'name': '__EnumValue'
                },
                {
                    'fields': [
                        {
                            'name': 'name',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'description',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'locations',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'args',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': '__Directive'
                },
                {
                    'fields': None,
                    'name': '__DirectiveLocation'
                }
            ]
        }
    }
}
