from flask import current_app
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphql import GraphQLError

from .version import version_field

from .product import product_field, all_products_field
from .product_file_path import all_product_file_paths_field
from .product_type import product_type_field, all_product_types_field
from .product_relation_type import product_relation_type_field, all_product_relation_types_field
from .product_relation import product_relation_field, all_product_relations_field

from .web_config import web_config_field

from .filter_ import PFilterableConnectionField

from .auth import github_user_field, oauth_app_info_field

##__________________________________________________________________||
class Query(graphene.ObjectType):

    version = version_field

    node = relay.Node.Field()

    web_config = web_config_field

    product_type = product_type_field
    all_product_types = all_product_types_field

    all_product_file_paths = all_product_file_paths_field

    product = product_field
    all_products = all_products_field

    product_relation_type = product_relation_type_field
    all_product_relation_types = all_product_relation_types_field

    product_relation = product_relation_field
    all_product_relations = all_product_relations_field

    github_user = github_user_field

    oauth_app_info = oauth_app_info_field

##__________________________________________________________________||
