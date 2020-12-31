from flask import current_app
import graphene
from graphql import GraphQLError

from ...db.sa import sa
from ...db.backup import request_backup_db

from ...models import (
   GitHubUser as GitHubUserModel,
   GitHubToken as GitHubAdminAppTokenModel
)
from ...github.call import exchange_code_for_token
from ...github.query import is_member
from ...github.query import get_user

from . import type_

##__________________________________________________________________||
class AuthenticateWithGitHub(graphene.Mutation):
    class Arguments:
        code = graphene.String(required=True)

    authPayload = graphene.Field(lambda: type_.AuthPayload)

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
        authPayload = type_.AuthPayload(token=token)
        return AuthenticateWithGitHub(authPayload=authPayload)

##__________________________________________________________________||
class AddGitHubAdminAppToken(graphene.Mutation):
    '''Add a token for a GitHub Admin App'''

    class Arguments:
        code = graphene.String(required=True)

    ok = graphene.Boolean()

    def mutate(root, info, code):
        token_url = current_app.config['GITHUB_AUTH_TOKEN_URL']
        client_id = current_app.config['GITHUB_AUTH_ADMIN_CLIENT_ID']
        client_secret = current_app.config['GITHUB_AUTH_ADMIN_CLIENT_SECRET']
        redirect_uri = current_app.config['GITHUB_AUTH_ADMIN_REDIRECT_URI']
        token = exchange_code_for_token(code, token_url, client_id, client_secret, redirect_uri)
        if not token:
            raise GraphQLError('Unsuccessful to obtain the token')
        user = get_user(token)
        userModel = GitHubUserModel.query.filter_by(login=user['login']).one_or_none()
        if userModel is None:
            userModel = GitHubUserModel(login=user['login'])
        model = GitHubAdminAppTokenModel(token=token, user=userModel)
        sa.session.add(model)
        sa.session.commit()
        ok = True
        request_backup_db()
        return AddGitHubAdminAppToken(ok=ok)

##__________________________________________________________________||
class DeleteGitHubAdminAppToken(graphene.Mutation):
    '''Delete a token for a GitHub Admin App'''

    class Arguments:
        token_id = graphene.Int(required=True)

    ok = graphene.Boolean()

    def mutate(root, info, token_id):
        model = GitHubAdminAppTokenModel.query.filter_by(token_id=token_id).one()
        sa.session.delete(model)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteGitHubAdminAppToken(ok=ok)

##__________________________________________________________________||
