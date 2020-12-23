import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from ...models import GitHubAdminAppToken as GitHubAdminAppTokenModel

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
