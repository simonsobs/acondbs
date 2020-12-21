import graphene

from . import product as p

from .auth import GitHubAuth, StoreAdminAppToken

from .query import Query

##__________________________________________________________________||
class Mutation(graphene.ObjectType):

    create_product = p.CreateProduct.Field()
    update_product = p.UpdateProduct.Field()
    delete_product = p.DeleteProduct.Field()

    create_product_file_path = p.CreateProductFilePath.Field()
    update_product_file_path = p.UpdateProductFilePath.Field()
    delete_product_file_path = p.DeleteProductFilePath.Field()

    create_product_type = p.CreateProductType.Field()
    update_product_type = p.UpdateProductType.Field()
    delete_product_type = p.DeleteProductType.Field()

    create_product_relation_types = p.CreateProductRelationTypes.Field()
    update_product_relation_type = p.UpdateProductRelationType.Field()
    delete_product_relation_types = p.DeleteProductRelationTypes.Field()

    create_product_relation = p.CreateProductRelation.Field()
    delete_product_relation = p.DeleteProductRelation.Field()

    github_auth = GitHubAuth.Field()
    store_admin_app_token = StoreAdminAppToken.Field()

##__________________________________________________________________||
