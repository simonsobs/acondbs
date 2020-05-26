
##__________________________________________________________________||
productFragment = '''
fragment productFragment on Product {
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
productConnectionFragment = '''
fragment productConnectionFragment on ProductConnection {
  edges {
    node {
     ...productFragment
    }
  }
}
''' + productFragment

##__________________________________________________________________||
