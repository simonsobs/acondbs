from flask import current_app
import graphene
from graphql import GraphQLError

from ...db.sa import sa
from ...db.backup import request_backup_db

from ...models import (
   GitHubUser as GitHubUserModel,
   GitHubToken as GitHubTokenModel
)
from ...github.ops import (
    exchange_code_for_token,
    update_org_member_lists,
    add_org,
    delete_org,
    store_token_for_code
)
from ...github.query import is_member
from ...github.query import get_user

from . import type_

##__________________________________________________________________||
class AddGitHubOrg(graphene.Mutation):
    class Arguments:
        login = graphene.String(required=True)
    ok = graphene.Boolean()
    git_hub_org = graphene.Field(lambda: type_.GitHubOrg)
    def mutate(root, info, login):
        model = add_org(login)
        ok = True
        # request_backup_db()
        return AddGitHubOrg(git_hub_org=model, ok=ok)

class DeleteGitHubOrg(graphene.Mutation):
    class Arguments:
        login = graphene.String(required=True)
    ok = graphene.Boolean()
    def mutate(root, info, login):
        delete_org(login)
        ok = True
        # request_backup_db()
        return DeleteGitHubOrg(ok=ok)

##__________________________________________________________________||
class AuthenticateWithGitHub(graphene.Mutation):
    class Arguments:
        code = graphene.String(required=True)

    authPayload = graphene.Field(lambda: type_.AuthPayload)

    def mutate(root, info, code):
        token_dict = exchange_code_for_token(code)
        if not token_dict:
            raise GraphQLError('Unsuccessful to obtain the token')
        token = token_dict['access_token']
        admin_token = GitHubTokenModel.query.all()[0]
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
        token = exchange_code_for_token(code)
        if not token:
            raise GraphQLError('Unsuccessful to obtain the token')
        user = get_user(token)
        userModel = GitHubUserModel.query.filter_by(login=user['login']).one_or_none()
        if userModel is None:
            userModel = GitHubUserModel(login=user['login'])
        model = GitHubTokenModel(token=token, user=userModel)
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
        model = GitHubTokenModel.query.filter_by(token_id=token_id).one()
        sa.session.delete(model)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteGitHubAdminAppToken(ok=ok)

##__________________________________________________________________||
class UpdateGitHubOrgMemberLists(graphene.Mutation):
    '''Update the member lists of GitHub organizations'''

    ok = graphene.Boolean()

    def mutate(root, info):
        update_org_member_lists()
        ok = True
        # request_backup_db()
        return UpdateGitHubOrgMemberLists(ok=ok)

##__________________________________________________________________||
