import graphene
from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyConnectionField

from ...github.query import get_user
from ...github.ops import get_github_oauth_app_info
from ..filter_ import PFilterableConnectionField
from . import type_

##__________________________________________________________________||
all_git_hub_orgs_field = PFilterableConnectionField(type_.GitHubOrg.connection)
all_git_hub_users_field = PFilterableConnectionField(type_.GitHubUser.connection)
all_git_hub_tokens_field = PFilterableConnectionField(type_.GitHubToken.connection)

##__________________________________________________________________||
def resolve_git_hub_o_auth_app_info(parent, info):
    info = get_github_oauth_app_info()
    return type_.GitHubOAuthAppInfo(
        client_id=info['client_id'],
        authorize_url=info['authorize_url'],
        redirect_uri=info['redirect_uri']
    )

git_hub_o_auth_app_info_field = graphene.Field(
    type_.GitHubOAuthAppInfo,
    resolver=resolve_git_hub_o_auth_app_info
    )

##__________________________________________________________________||
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

    user['avatar_url'] = user.pop('avatarUrl')
    return type_.GitHubUser(**user)

github_user_field = graphene.Field(type_.GitHubUser, resolver=resolve_github_user)

##__________________________________________________________________||
