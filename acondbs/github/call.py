"""Call GitHub APIs
"""

import requests

API_URL = 'https://api.github.com/graphql'

##__________________________________________________________________||
def call_graphql_api(query, variables=None, token=None):

    headers = {}
    if token:
      headers['Authorization'] = 'token {}'.format(token)

    json = {'query': query }
    if variables:
        json['variables'] = variables

    response = requests.post(API_URL, json=json, headers=headers)
    response = response.json()
    # Examples: query = '{ viewer { login name avatarUrl } }'
    #   Success:
    #     response = {
    #         "data": {
    #             "viewer": {
    #                 "login": "octocat",
    #                 "name": "The Octocat",
    #                 "avatarUrl": "https://avatars3.githubusercontent.com/u/583231?u=a59fef2a493e2b67dd13754231daf220c82ba84d&v=4"
    #             }
    #         }
    #     }
    #
    #   Error: sometimes, the 'data' field still exists.
    #     response = {
    #         'errors': [
    #             {
    #                 'path': ['query', 'viewer', 'idii'],
    #                 'extensions': {'code': 'undefinedField', 'typeName': 'User', 'fieldName': 'idii'},
    #                 'locations': [{'line': 1, 'column': 12}],
    #                 'message': "Field 'idii' doesn't exist on type 'User'"
    #             }
    #         ]}
    #
    #   Bad credentials:
    #     response = {
    #         'message': 'Bad credentials',
    #         'documentation_url': 'https://docs.github.com/graphql'
    #     }

    if 'errors' in response:
      raise Exception(response['errors'])

    if 'data' not in response:
      raise Exception(response)

    return response['data']

##__________________________________________________________________||
