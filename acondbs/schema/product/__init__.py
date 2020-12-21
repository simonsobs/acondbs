
##__________________________________________________________________||
from .product import (
    product_field, all_products_field,
    CreateProduct, UpdateProduct, DeleteProduct
)
from .product_file_path import (
    all_product_file_paths_field,
    CreateProductFilePath, UpdateProductFilePath, DeleteProductFilePath
)
from .product_type import (
    product_type_field, all_product_types_field,
    CreateProductType, UpdateProductType, DeleteProductType
)
from .product_relation_type import (
    product_relation_type_field, all_product_relation_types_field,
    CreateProductRelationTypes, UpdateProductRelationType, DeleteProductRelationTypes
)
from .product_relation import (
    product_relation_field, all_product_relations_field,
    CreateProductRelation, DeleteProductRelation
)

##__________________________________________________________________||
