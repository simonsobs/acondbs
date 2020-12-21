import graphene
from graphene import relay

from .version import version_field
from .web import web_config_field

from .auth import (
    github_user_field, oauth_app_info_field,
    GitHubAuth, StoreAdminAppToken
)

from . import product as p

##__________________________________________________________________||
def create_schema(enable_mutation=True):
    if enable_mutation:
        return graphene.Schema(query=Query, mutation=Mutation)
    return graphene.Schema(query=Query)

##__________________________________________________________________||
class Query(graphene.ObjectType):

    version = version_field

    node = relay.Node.Field()

    web_config = web_config_field

    product_type = p.product_type_field
    all_product_types = p.all_product_types_field

    all_product_file_paths = p.all_product_file_paths_field

    product = p.product_field
    all_products = p.all_products_field

    product_relation_type = p.product_relation_type_field
    all_product_relation_types = p.all_product_relation_types_field

    product_relation = p.product_relation_field
    all_product_relations = p.all_product_relations_field

    github_user = github_user_field

    oauth_app_info = oauth_app_info_field

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
