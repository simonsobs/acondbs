import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..connection import CountedConnection
from ...github.ops import get_github_oauth_app_info
from ...models import (
    GitHubUser as GitHubUserModel,
    GitHubOrg as GitHubOrgModel,
    GitHubOrgMembership as GitHubOrgMembershipModel,
    GitHubToken as GitHubTokenModel,
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
        model = GitHubTokenModel
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
class GitHubOrg(SQLAlchemyObjectType):
    class Meta:
        model = GitHubOrgModel
        interfaces = (relay.Node, )
        connection_class = CountedConnection

##__________________________________________________________________||
class GitHubOrgMembership(SQLAlchemyObjectType):
    class Meta:
        model = GitHubOrgMembershipModel
        interfaces = (relay.Node, )
        connection_class = CountedConnection

##__________________________________________________________________||
