from .fragments import FRAGMENT_PRODUCT_RELATION

##__________________________________________________________________||
CREATE_PRODUCT_RELATION = '''
mutation CreateProductRelation($input: CreateProductRelationInput!) {
  createProductRelation(input: $input) {
    ok
    productRelation {
      ...fragmentProductRelation
    }
  }
}
''' + FRAGMENT_PRODUCT_RELATION

DELETE_PRODUCT_RELATION = '''
mutation DeleteProductRelation($relationId: Int!) {
  deleteProductRelation(relationId: $relationId) {
    ok
  }
}
'''

##__________________________________________________________________||
