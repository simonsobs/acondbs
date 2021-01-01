import graphene
from graphene import relay

from . import version as version_
from .web import web_config_field

from . import (github, product as p)

##__________________________________________________________________||
def create_schema(enable_mutation=True):
    if enable_mutation:
        return graphene.Schema(query=Query, mutation=Mutation)
    return graphene.Schema(query=Query)

##__________________________________________________________________||
class Query(graphene.ObjectType):

    version = version_.version_field
    alembic_version = version_.alembic_version_field

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

    github_user = github.query.github_user_field

    all_git_hub_tokens = github.query.all_git_hub_tokens_field

    git_hub_o_auth_app_info = github.query.git_hub_o_auth_app_info_field

    all_git_hub_orgs = github.query.all_git_hub_orgs_field
    all_git_hub_users = github.query.all_git_hub_users_field

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

    authenticate_with_git_hub = github.mutation.AuthenticateWithGitHub.Field()

    add_git_hub_admin_app_token = github.mutation.AddGitHubAdminAppToken.Field()
    delete_git_hub_admin_app_token = github.mutation.DeleteGitHubAdminAppToken.Field()

##__________________________________________________________________||
