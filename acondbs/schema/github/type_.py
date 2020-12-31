import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..connection import CountedConnection
from ...github.ops import get_github_oauth_app_info
from ...models import (
    GitHubUser as GitHubUserModel,
    GitHubToken as GitHubAdminAppTokenModel,
)

##__________________________________________________________________||
class GitHubOAuthAppInfo(graphene.ObjectType):
    client_id = graphene.String()
    authorize_url = graphene.String()
    redirect_uri = graphene.String()

##__________________________________________________________________||
class AuthPayload(graphene.ObjectType):
    token = graphene.String()

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

##__________________________________________________________________||
class GitHubUser(SQLAlchemyObjectType):
    class Meta:
        model = GitHubUserModel
        interfaces = (relay.Node, )
        connection_class = CountedConnection

##__________________________________________________________________||
