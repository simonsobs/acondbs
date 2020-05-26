
##__________________________________________________________________||
FRAGMENT_PRODUCT_RELATION = '''
fragment fragmentProductRelation on ProductRelation {
  relationId
  type_ {
    typeId
    name
  }
  self_ {
    productId
    name
  }
  other {
    productId
    name
  }
  reverse {
    relationId
  }
}
'''

FRAGMENT_PRODUCT_RELATION_CONNECTION = '''
fragment fragmentProductRelationConnection on ProductRelationConnection {
  edges {
    node {
      ...fragmentProductRelation
    }
  }
}
''' + FRAGMENT_PRODUCT_RELATION

##__________________________________________________________________||
