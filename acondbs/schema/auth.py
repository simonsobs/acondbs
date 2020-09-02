import graphene

from ..misc import githubauth

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
        user = githubauth.get_username(token)
        authPayload = AuthPayload(token=token, user=user)
        return GitHubAuth(authPayload=authPayload)

##__________________________________________________________________||
class GitHubUser(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)

    authPayload = graphene.Field(lambda: AuthPayload)

    def mutate(root, info, token):
        user = githubauth.get_username(token)
        authPayload = AuthPayload(token=token, user=user)
        return GitHubAuth(authPayload=authPayload)

##__________________________________________________________________||
