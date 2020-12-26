from flask import current_app

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from graphql import GraphQLError

from ...models import GitHubUser as GitHubUserModel

from ...github.api import get_user

from ...db.sa import sa
from ...db.backup import request_backup_db

from ..connection import CountedConnection

##__________________________________________________________________||
class GitHubUser(SQLAlchemyObjectType):
    class Meta:
        model = GitHubUserModel
        interfaces = (relay.Node, )
        connection_class = CountedConnection

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
    return GitHubUser(**user)

github_user_field = graphene.Field(GitHubUser, resolver=resolve_github_user)

##__________________________________________________________________||
