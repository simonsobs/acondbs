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
from .product_relation import ProductRelation, ProductRelationModel

from .web_config import web_config_field

from .filter_ import PFilterableConnectionField

from .auth import OAuthAppInfo, GitHubUser

from ..github.api import get_user

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

    all_product_relations = PFilterableConnectionField(ProductRelation.connection)

    product_relation = graphene.Field(ProductRelation, relation_id=graphene.Int())

    def resolve_product_relation(parent, info, **kwargs):
        filter = [getattr(ProductRelationModel, k)==v for k, v in kwargs.items()]
        return ProductRelation.get_query(info).filter(*filter).one_or_none()

    github_user = graphene.Field(GitHubUser)

    def resolve_github_user(parent, info):

        auth = info.context.headers.get('Authorization')
        # e.g., 'Bearer "xxxx"'

        if not auth:
            raise GraphQLError('Authorization is required')

        token = auth.split()[1].strip('"')
        # e.g., "xxxx"

        user = get_user(token)
        if not user:
            raise GraphQLError('Unsuccessful to obtain the user')

        return GitHubUser(**user);

    oauth_app_info = graphene.Field(
        OAuthAppInfo,
        admin=graphene.Boolean(default_value=False)
        )

    def resolve_oauth_app_info(parent, info, admin):
        print(admin)
        if admin:
            return OAuthAppInfo(
                client_id=current_app.config['GITHUB_AUTH_ADMIN_CLIENT_ID'],
                authorize_url=current_app.config['GITHUB_AUTH_AUTHORIZE_URL'],
                token_url=current_app.config['GITHUB_AUTH_TOKEN_URL'],
                redirect_uri=current_app.config['GITHUB_AUTH_ADMIN_REDIRECT_URI']
            )

        return OAuthAppInfo(
            client_id=current_app.config['GITHUB_AUTH_CLIENT_ID'],
            authorize_url=current_app.config['GITHUB_AUTH_AUTHORIZE_URL'],
            token_url=current_app.config['GITHUB_AUTH_TOKEN_URL'],
            redirect_uri=current_app.config['GITHUB_AUTH_REDIRECT_URI']
        )
##__________________________________________________________________||
