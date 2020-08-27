import graphene
import requests

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
        github_client_id = '1ce266dd301a653ca64f'
        github_client_secret = 'adb99c5ef0cdfbc052af1e3573684026bd2c1c23'
        authorize_url = 'https://github.com/login/oauth/authorize'
        token_url = 'https://github.com/login/oauth/access_token'
        redirect_uri = 'http://localhost:8081/signin'

        params = {
            'grant_type': 'authorization_code',
            'client_id': github_client_id,
            'client_secret': github_client_secret,
            'redirect_uri': redirect_uri,
            'code': code
        };

        headers = {
            'Accept': "application/vnd.github.v3+json, application/json",
        }

        r = requests.post(token_url, json=params, headers=headers)
        r = r.json()
        # type(r): <class 'dict'>
        # e.g., r = {'access_token': 'xxx', 'token_type': 'bearer', 'scope': 'user'}


        token = r['access_token']

        headers = {
             'Authorization': 'token {}'.format(token)
        }

        # r = requests.get('https://api.github.com/user?access_token={token}'.format(token=token))
        r = requests.get('https://api.github.com/user', headers=headers)
        r = r.json()
        # e.g., {"login": "octocat", "id": 1, "node_id": "MDQ6VXNlcjE=",  ... }
        # https://docs.github.com/en/rest/reference/users

        user = r['login']

        authPayload = AuthPayload(token=token, user=user)
        return GitHubAuth(authPayload=authPayload)

##__________________________________________________________________||
