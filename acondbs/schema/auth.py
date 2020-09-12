import graphene
from graphql import GraphQLError

from ..misc import githubauth

##__________________________________________________________________||
class OAuthAppInfo(graphene.ObjectType):
    client_id = graphene.String()
    authorize_url = graphene.String()
    token_url = graphene.String()
    redirect_uri = graphene.String()

##__________________________________________________________________||
class AuthPayload(graphene.ObjectType):
    token = graphene.String()
    user = graphene.String()

##__________________________________________________________________||
class GitHubAuth(graphene.Mutation):
    class Arguments:
        code = graphene.String(required=True)

    authPayload = graphene.Field(lambda: AuthPayload)

    def mutate(root, info, code):
        token = githubauth.get_token(code)
        if not token:
            raise GraphQLError('Unsuccessful to obtain the token')
        user = githubauth.get_username(token)
        if not user:
            raise GraphQLError('Unsuccessful to obtain the username')
        authPayload = AuthPayload(token=token, user=user)
        return GitHubAuth(authPayload=authPayload)

##__________________________________________________________________||
