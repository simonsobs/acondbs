import graphene
from graphql import GraphQLError

from ...github.ops import get_github_oauth_app_info, get_user_for_token

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
def resolve_git_hub_viewer(parent, info):

    auth = info.context.headers.get('Authorization')
    # e.g., 'Bearer "xxxx"'

    if not auth:
        raise GraphQLError('Authorization is required')

    token = auth.split()[1].strip('"')
    # e.g., "xxxx"

    return get_user_for_token(token)

git_hub_viewer_field = graphene.Field(type_.GitHubUser, resolver=resolve_git_hub_viewer)

##__________________________________________________________________||
