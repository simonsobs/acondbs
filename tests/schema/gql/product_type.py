
##__________________________________________________________________||
FRAGMENT_PRODUCT_TYPE = '''
fragment fragmentProductType on ProductType {
  typeId
  name
  order
  indefArticle
  singular
  plural
  icon
  products {
    edges {
      node {
        name
      }
    }
  }
}
'''

FRAGMENT_PRODUCT_TYPE_CONNECTION = '''
fragment fragmentProductTypeConnection on ProductTypeConnection {
  edges {
    node {
      ...fragmentProductType
    }
  }
}
''' + FRAGMENT_PRODUCT_TYPE

##__________________________________________________________________||
CREATE_PRODUCT_TYPE = '''
mutation CreateProductType($input: CreateProductTypeInput!) {
  createProductType(input: $input) {
    ok
    productType {
      ...fragmentProductType
    }
  }
}
''' + FRAGMENT_PRODUCT_TYPE

##__________________________________________________________________||
