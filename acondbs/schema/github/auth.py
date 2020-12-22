from flask import current_app
import graphene
from graphql import GraphQLError

from ...models import GitHubAdminAppToken as GitHubAdminAppTokenModel
from ...github.auth import get_token
from ...github.api import is_member, get_user

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
class GitHubUser(graphene.ObjectType):
    login = graphene.String()
    name = graphene.String()
    avatarUrl = graphene.String() # Camel case so can easily be instantiated

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

github_user_field = graphene.Field(GitHubUser, resolver=resolve_github_user)

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
class StoreAdminAppToken(graphene.Mutation):
    class Arguments:
        code = graphene.String(required=True)

    ok = graphene.Boolean()

    def mutate(root, info, code):
        token_url = current_app.config['GITHUB_AUTH_TOKEN_URL']
        client_id = current_app.config['GITHUB_AUTH_ADMIN_CLIENT_ID']
        client_secret = current_app.config['GITHUB_AUTH_ADMIN_CLIENT_SECRET']
        redirect_uri = current_app.config['GITHUB_AUTH_ADMIN_REDIRECT_URI']
        token = get_token(code, token_url, client_id, client_secret, redirect_uri)

        row = GitHubAdminAppTokenModel.query.one_or_none()
        if row:
            row.token = token
        else:
            row = GitHubAdminAppTokenModel(token=token)
            sa.session.add(row)
        sa.session.commit()
        ok = True
        return StoreAdminAppToken(ok=ok)
