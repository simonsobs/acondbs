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

    #
    version = version_.version_field
    alembic_version = version_.alembic_version_field

    node = relay.Node.Field()

    web_config = web_config_field

    #
    all_products = p.query.all_products_field
    all_product_file_paths = p.query.all_product_file_paths_field
    all_product_relations = p.query.all_product_relations_field
    all_product_relation_types = p.query.all_product_relation_types_field
    all_product_types = p.query.all_product_types_field

    product = p.query.product_field
    product_relation = p.query.product_relation_field
    product_relation_type = p.query.product_relation_type_field
    product_type = p.query.product_type_field

    #
    all_git_hub_orgs = github.query.all_git_hub_orgs_field
    all_git_hub_tokens = github.query.all_git_hub_tokens_field
    all_git_hub_users = github.query.all_git_hub_users_field

    git_hub_viewer = github.query.git_hub_viewer_field
    git_hub_o_auth_app_info = github.query.git_hub_o_auth_app_info_field

##__________________________________________________________________||
class Mutation(graphene.ObjectType):

    #
    create_product = p.mutation.CreateProduct.Field()
    delete_product = p.mutation.DeleteProduct.Field()
    update_product = p.mutation.UpdateProduct.Field()

    create_product_file_path = p.mutation.CreateProductFilePath.Field()
    delete_product_file_path = p.mutation.DeleteProductFilePath.Field()
    update_product_file_path = p.mutation.UpdateProductFilePath.Field()

    create_product_relation = p.mutation.CreateProductRelation.Field()
    delete_product_relation = p.mutation.DeleteProductRelation.Field()

    create_product_relation_types = p.mutation.CreateProductRelationTypes.Field()
    delete_product_relation_types = p.mutation.DeleteProductRelationTypes.Field()
    update_product_relation_type = p.mutation.UpdateProductRelationType.Field()

    create_product_type = p.mutation.CreateProductType.Field()
    delete_product_type = p.mutation.DeleteProductType.Field()
    update_product_type = p.mutation.UpdateProductType.Field()

    #
    add_git_hub_org = github.mutation.AddGitHubOrg.Field()
    delete_git_hub_org = github.mutation.DeleteGitHubOrg.Field()

    authenticate_with_git_hub = github.mutation.AuthenticateWithGitHub.Field()

    add_git_hub_admin_app_token = github.mutation.AddGitHubAdminAppToken.Field()
    delete_git_hub_admin_app_token = github.mutation.DeleteGitHubAdminAppToken.Field()

    update_git_hub_org_member_lists = github.mutation.UpdateGitHubOrgMemberLists.Field()

##__________________________________________________________________||
