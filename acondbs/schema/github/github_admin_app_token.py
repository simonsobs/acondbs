from flask import current_app

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from graphql import GraphQLError

from ...models import (
    GitHubToken as GitHubAdminAppTokenModel,
    GitHubUser as GitHubUserModel
)
from ...github.auth import get_token
from ...github.query import get_user

from ...db.sa import sa
from ...db.backup import request_backup_db

from ..connection import CountedConnection

##__________________________________________________________________||
class GitHubAdminAppToken(SQLAlchemyObjectType):
    class Meta:
        model = GitHubAdminAppTokenModel
        interfaces = (relay.Node, )
        exclude_fields = ['token', ]
        connection_class = CountedConnection
    token_masked = graphene.String()
    def resolve_token_masked(parent, info):
        return "X" * 15

all_git_hub_admin_app_tokens_field = SQLAlchemyConnectionField(GitHubAdminAppToken.connection)

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
        token = get_token(code, token_url, client_id, client_secret, redirect_uri)
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
