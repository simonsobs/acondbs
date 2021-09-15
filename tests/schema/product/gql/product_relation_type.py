from .fragments import (
    FRAGMENT_PRODUCT_RELATION_TYPE,
    FRAGMENT_PRODUCT_RELATION_TYPE_CONNECTION
)

##__________________________________________________________________||
MUTATION_CREATE_PRODUCT_RELATION_TYPES = '''
mutation CreateProductRelationTypes(
    $type: CreateProductRelationTypeInput!,
    $reverse: CreateProductRelationTypeInput,
    $selfReverse: Boolean) {
  createProductRelationTypes(type: $type, reverse: $reverse, selfReverse: $selfReverse) {
    ok
    productRelationType {
      ...fragmentProductRelationType
    }
  }
}
''' + FRAGMENT_PRODUCT_RELATION_TYPE

MUTATION_DELETE_PRODUCT_RELATION_TYPES = '''
mutation DeleteProductRelationTypes($typeId: Int!) {
  deleteProductRelationTypes(typeId: $typeId) {
    ok
  }
}
'''

MUTATION_UPDATE_PRODUCT_RELATION_TYPE = '''
mutation UpdateProductRelationType(
    $typeId: Int!, $input: UpdateProductRelationTypeInput!) {
  updateProductRelationType(typeId: $typeId, input: $input) {
    ok
    productRelationType {
      ...fragmentProductRelationType
    }
  }
}
''' + FRAGMENT_PRODUCT_RELATION_TYPE

##__________________________________________________________________||
