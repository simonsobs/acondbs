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
        token = githubauth.get_token(code)
        if not token:
            raise GraphQLError('Unsuccessful to obtain the token')
        authPayload = AuthPayload(token=token)
        return GitHubAuth(authPayload=authPayload)

##__________________________________________________________________||
