import graphene
from graphene import relay

from .version import version_field
from .web import web_config_field

from .auth import github_user_field, oauth_app_info_field

from . import product as p

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
