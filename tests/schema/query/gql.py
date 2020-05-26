
##__________________________________________________________________||
FRAGMENT_PRODUCT_DEEP = '''
fragment fragmentProductDeep on Product {
  productId
  typeId
  type_ {
    typeId
    name
  }
  name
  contact
  dateProduced
  producedBy
  datePosted
  postedBy
  dateUpdated
  updatedBy
  paths {
    edges {
      node {
        pathId
        path
        note
      }
    }
  }
  relations {
    edges {
      node {
        relationId
        typeId
        type_ {
          typeId
          name
        }
        otherProductId
        other {
          productId
          typeId
          type_ {
            typeId
            name
          }
          name
        }
        reverseRelationId
        reverse {
          relationId
          typeId
          type_ {
            typeId
            name
          }
        }
      }
    }
  }
  note
}
'''

##__________________________________________________________________||
FRAGMENT_PRODUCT_CONNECTION_DEEP = '''
fragment fragmentProductConnectionDeep on ProductConnection {
  edges {
    node {
     ...fragmentProductDeep
    }
  }
}
''' + FRAGMENT_PRODUCT_DEEP

##__________________________________________________________________||
