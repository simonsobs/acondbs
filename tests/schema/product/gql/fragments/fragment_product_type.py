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
