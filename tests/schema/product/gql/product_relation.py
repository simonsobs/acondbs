from .fragments import FRAGMENT_PRODUCT_RELATION

##__________________________________________________________________||
MUTATION_CREATE_PRODUCT_RELATION = '''
mutation CreateProductRelation($input: CreateProductRelationInput!) {
  createProductRelation(input: $input) {
    ok
    productRelation {
      ...fragmentProductRelation
    }
  }
}
''' + FRAGMENT_PRODUCT_RELATION

MUTATION_DELETE_PRODUCT_RELATION = '''
mutation DeleteProductRelation($relationId: Int!) {
  deleteProductRelation(relationId: $relationId) {
    ok
  }
}
'''

##__________________________________________________________________||
