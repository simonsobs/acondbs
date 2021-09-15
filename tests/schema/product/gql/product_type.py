from .fragments import FRAGMENT_PRODUCT_TYPE

##__________________________________________________________________||
MUTATION_CREATE_PRODUCT_TYPE = '''
mutation CreateProductType($input: CreateProductTypeInput!) {
  createProductType(input: $input) {
    ok
    productType {
      ...fragmentProductType
    }
  }
}
''' + FRAGMENT_PRODUCT_TYPE

MUTATION_DELETE_PRODUCT_TYPE = '''
mutation DeleteProductType($typeId: Int!) {
  deleteProductType(typeId: $typeId) {
    ok
  }
}
'''

MUTATION_UPDATE_PRODUCT_TYPE = '''
mutation UpdateProductType($typeId: Int!, $input: UpdateProductTypeInput!) {
  updateProductType(typeId: $typeId,input: $input) {
    ok
    productType {
      ...fragmentProductType
    }
  }
}
''' + FRAGMENT_PRODUCT_TYPE

##__________________________________________________________________||
