from flask import current_app
import graphene
from graphql import GraphQLError

from ...models import GitHubToken as GitHubAdminAppTokenModel
from ...github.call import exchange_code_for_token
from ...github.query import is_member

from ...db.sa import sa

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
        token = exchange_code_for_token(code, token_url, client_id, client_secret, redirect_uri)
        if not token:
            raise GraphQLError('Unsuccessful to obtain the token')
        admin_token = GitHubAdminAppTokenModel.query.all()[0]
        org_name = current_app.config['GITHUB_ORG']
        if not is_member(user_token=token, admin_token=admin_token.token, org_name=org_name):
            raise GraphQLError('The user is not a member.')
        authPayload = AuthPayload(token=token)
        return AuthenticateWithGitHub(authPayload=authPayload)

##__________________________________________________________________||
