from .fragments import (
    FRAGMENT_PRODUCT,
    FRAGMENT_PRODUCT_CONNECTION,
    FRAGMENT_PRODUCT_SHALLOW,
    FRAGMENT_PRODUCT_CONNECTION_SHALLOW
)


##__________________________________________________________________||
CREATE_PRODUCT = '''
mutation CreateProduct($input: CreateProductInput!) {
  createProduct(input: $input) {
    ok
    product {
      ...fragmentProduct
    }
  }
}
''' + FRAGMENT_PRODUCT

DELETE_PRODUCT = '''
mutation DeleteProduct($productId: Int!) {
  deleteProduct(productId: $productId) {
    ok
  }
}
'''

UPDATE_PRODUCT = '''
mutation($productId: Int!, $input: UpdateProductInput!) {
  updateProduct(productId: $productId, input: $input) {
    ok
    product {
      ...fragmentProduct
    }
  }
}
''' + FRAGMENT_PRODUCT

##__________________________________________________________________||
