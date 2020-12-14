from flask import current_app
import graphene
from graphql import GraphQLError

from ..models import AdminAppToken as AdminAppTokenModel
from ..github.auth import get_token
from ..github.api import is_member

from ..db.sa import sa

##__________________________________________________________________||
class OAuthAppInfo(graphene.ObjectType):
    client_id = graphene.String()
    authorize_url = graphene.String()
    token_url = graphene.String()
    redirect_uri = graphene.String()

##__________________________________________________________________||
class GitHubUser(graphene.ObjectType):
    login = graphene.String()
    name = graphene.String()
    avatarUrl = graphene.String() # Camel case so can easily be instantiated

##__________________________________________________________________||
class AuthPayload(graphene.ObjectType):
    token = graphene.String()

##__________________________________________________________________||
class GitHubAuth(graphene.Mutation):
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
        admin_token = AdminAppTokenModel.query.one()
        if not is_member(user_token=token, admin_token=admin_token.token):
            raise GraphQLError('The user is not a member.')
        authPayload = AuthPayload(token=token)
        return GitHubAuth(authPayload=authPayload)

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

        row = AdminAppTokenModel.query.one_or_none()
        if row:
            row.token = token
        else:
            row = AdminAppTokenModel(token=token)
            sa.session.add(row)
        sa.session.commit()
        ok = True
        return StoreAdminAppToken(ok=ok)
