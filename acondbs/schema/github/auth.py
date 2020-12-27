from flask import current_app
import graphene
from graphql import GraphQLError

from ...models import GitHubToken as GitHubAdminAppTokenModel
from ...github.auth import get_token
from ...github.query import is_member

from ...db.sa import sa

##__________________________________________________________________||
class OAuthAppInfo(graphene.ObjectType):
    client_id = graphene.String()
    authorize_url = graphene.String()
    token_url = graphene.String()
    redirect_uri = graphene.String()

def resolve_oauth_app_info(parent, info, admin):
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

oauth_app_info_field = graphene.Field(
    OAuthAppInfo,
    admin=graphene.Boolean(default_value=False),
    resolver=resolve_oauth_app_info
    )

##__________________________________________________________________||
class AuthPayload(graphene.ObjectType):
    token = graphene.String()

##__________________________________________________________________||
class AuthenticateWithGitHub(graphene.Mutation):
    class Arguments:
        code = graphene.String(required=True)

    authPayload = graphene.Field(lambda: AuthPayload)

    def mutate(root, info, code):
        token_url = current_app.config['GITHUB_AUTH_TOKEN_URL']
        client_id = current_app.config['GITHUB_AUTH_CLIENT_ID']
        client_secret = current_app.config['GITHUB_AUTH_CLIENT_SECRET']
        redirect_uri = current_app.config['GITHUB_AUTH_REDIRECT_URI']
        token = get_token(code, token_url, client_id, client_secret, redirect_uri)
        if not token:
            raise GraphQLError('Unsuccessful to obtain the token')
        admin_token = GitHubAdminAppTokenModel.query.one()
        org_name = current_app.config['GITHUB_ORG']
        if not is_member(user_token=token, admin_token=admin_token.token, org_name=org_name):
            raise GraphQLError('The user is not a member.')
        authPayload = AuthPayload(token=token)
        return AuthenticateWithGitHub(authPayload=authPayload)

##__________________________________________________________________||
