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
                            'name': 'allProductRelationTypes',
                            'type': {
                                'name': 'ProductRelationTypeConnection'
                            }
                        },
                        {
                            'name': 'productRelationType',
                            'type': {
                                'name': 'ProductRelationType'
                            }
                        },
                        {
                            'name': 'allProductRelations',
                            'type': {
                                'name': 'ProductRelationConnection'
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
                    'name': 'ProductTypeConnection'
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
                            'name': 'typeId',
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
                            'name': 'order',
                            'type': {
                                'name': 'Int'
                            }
                        },
                        {
                            'name': 'indefArticle',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'singular',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'plural',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'icon',
                            'type': {
                                'name': 'String'
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
                    'fields': None,
                    'name': 'Int'
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
                            'name': 'typeId',
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
                            'name': 'type_',
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
                            'name': 'relations',
                            'type': {
                                'name': 'ProductRelationConnection'
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
                    'name': 'ProductFilePathSortEnum'
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
                    'name': 'ProductRelationConnection'
                },
                {
                    'fields': [
                        {
                            'name': 'node',
                            'type': {
                                'name': 'ProductRelation'
                            }
                        },
                        {
                            'name': 'cursor',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'ProductRelationEdge'
                },
                {
                    'fields': [
                        {
                            'name': 'relationId',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'typeId',
                            'type': {
                                'name': None
                            }
                        },
                        {
                            'name': 'selfProductId',
                            'type': {
                                'name': 'Int'
                            }
                        },
                        {
                            'name': 'otherProductId',
                            'type': {
                                'name': 'Int'
                            }
                        },
                        {
                            'name': 'reverseRelationId',
                            'type': {
                                'name': 'Int'
                            }
                        },
                        {
                            'name': 'type_',
                            'type': {
                                'name': 'ProductRelationType'
                            }
                        },
                        {
                            'name': 'self_',
                            'type': {
                                'name': 'Product'
                            }
                        },
                        {
                            'name': 'other',
                            'type': {
                                'name': 'Product'
                            }
                        },
                        {
                            'name': 'reverse',
                            'type': {
                                'name': 'ProductRelation'
                            }
                        },
                        {
                            'name': 'id',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'ProductRelation'
                },
                {
                    'fields': [
                        {
                            'name': 'typeId',
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
                            'name': 'reverseTypeId',
                            'type': {
                                'name': 'Int'
                            }
                        },
                        {
                            'name': 'indefArticle',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'singular',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'plural',
                            'type': {
                                'name': 'String'
                            }
                        },
                        {
                            'name': 'reverse',
                            'type': {
                                'name': 'ProductRelationType'
                            }
                        },
                        {
                            'name': 'relations',
                            'type': {
                                'name': 'ProductRelationConnection'
                            }
                        },
                        {
                            'name': 'id',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'ProductRelationType'
                },
                {
                    'fields': None,
                    'name': 'ProductRelationSortEnum'
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
                    'name': 'ProductTypeFilter'
                },
                {
                    'fields': None,
                    'name': 'ProductTypeSortEnum'
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
                    'name': 'ProductRelationTypeConnection'
                },
                {
                    'fields': [
                        {
                            'name': 'node',
                            'type': {
                                'name': 'ProductRelationType'
                            }
                        },
                        {
                            'name': 'cursor',
                            'type': {
                                'name': None
                            }
                        }
                    ],
                    'name': 'ProductRelationTypeEdge'
                },
                {
                    'fields': None,
                    'name': 'ProductRelationTypeSortEnum'
                },
                {
                    'fields': [
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
                        },
                        {
                            'name': 'createProductRelationType',
                            'type': {
                                'name': 'CreateProductRelationType'
                            }
                        },
                        {
                            'name': 'deleteProductRelationType',
                            'type': {
                                'name': 'DeleteProductRelationType'
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
                            'name': 'ok',
                            'type': {
                                'name': 'Boolean'
                            }
                        },
                        {
                            'name': 'productRelationType',
                            'type': {
                                'name': 'ProductRelationType'
                            }
                        }
                    ],
                    'name': 'CreateProductRelationType'
                },
                {
                    'fields': None,
                    'name': 'CreateProductRelationTypeInput'
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
                    'name': 'DeleteProductRelationType'
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
