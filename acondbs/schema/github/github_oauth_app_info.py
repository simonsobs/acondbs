from ...github.ops import get_github_oauth_app_info

import graphene

##__________________________________________________________________||
class GitHubOAuthAppInfo(graphene.ObjectType):
    client_id = graphene.String()
    authorize_url = graphene.String()
    redirect_uri = graphene.String()

def resolve_git_hub_o_auth_app_info(parent, info):
    info = get_github_oauth_app_info()
    return GitHubOAuthAppInfo(
        client_id=info['client_id'],
        authorize_url=info['authorize_url'],
        redirect_uri=info['redirect_uri']
    )

git_hub_o_auth_app_info_field = graphene.Field(
    GitHubOAuthAppInfo,
    resolver=resolve_git_hub_o_auth_app_info
    )

##__________________________________________________________________||
