"""Access to GitHub API
"""

from flask import current_app
import requests

API_URL = 'https://api.github.com/graphql'

##__________________________________________________________________||
def call_api(query, variables=None, token=None):

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
    #     response = {'errors': [
    #         {
    #             'path': ['query', 'viewer', 'idii'],
    #             'extensions': {'code': 'undefinedField', 'typeName': 'User', 'fieldName': 'idii'},
    #             'locations': [{'line': 1, 'column': 12}],
    #             'message': "Field 'idii' doesn't exist on type 'User'"
    #         }
    #     ]}
    #
    #   Bad credentials):
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
def get_user(token):
    query = '{ viewer { login name avatarUrl } }'
    r = call_api(query=query, token=token)
    # e.g., https://github.com/octocat
    # {
    #     "viewer": {
    #         "login": "octocat",
    #         "name": "The Octocat",
    #         "avatarUrl": "https://avatars3.githubusercontent.com/u/583231?u=a59fef2a493e2b67dd13754231daf220c82ba84d&v=4"
    #     }
    # }
    user = r.get('viewer')
    return user

##__________________________________________________________________||
def get_user_id(token):
    query = '{ viewer { id } }'
    r = call_api(query=query, token=token)
    # e.g.,
    # {
    #     "viewer": {
    #         "id": "MDQ6VXNlcjU4MzIzMQ=="
    #     }
    # }
    ret = r.get('viewer', {}).get('id')
    return ret

##__________________________________________________________________||
def get_org_member_ids(org_name, token):
    query = """
      query OrganizationMemberCount($org_login: String!) {
        organization(login: $org_login) {
          login
          membersWithRole {
            totalCount
          }
        }
      }
    """
    variables = { "org_login": org_name }
    r = call_api(query=query, variables=variables, token=token)
    # e.g.,
    # {
    #     'organization': {
    #         'login': 'urban-octo-disco',
    #         'membersWithRole': {'totalCount': 2}
    #     }
    # }

    nmembers = r['organization']['membersWithRole']['totalCount']

    query = """
      query OrganizationMembers($org_login: String!, $first: Int!) {
        organization(login: $org_login) {
          login
          membersWithRole(first: $first) {
            edges {
              role
              node {
                id
                login
              }
            }
          }
        }
      }
    """
    variables = { "org_login": org_name, "first": nmembers }
    r = call_api(query=query, variables=variables, token=token)
    # e.g.,
    # {
    #     'data': {
    #         'organization': {
    #             'login': 'urban-octo-disco',
    #             'membersWithRole': {
    #                 'edges': [
    #                     {
    #                         'node': {
    #                             'id': 'MDQ6VXNlcjEzODgwODE=',
    #                             'login': 'TaiSakuma'
    #                         },
    #                         'role': 'MEMBER'
    #                     },
    #                     {
    #                         'node': {
    #                             'id': 'MDQ6VXNlcjE1Njg1Njk3',
    #                             'login': 'tai-sakuma'
    #                         },
    #                         'role': 'ADMIN'
    #                     }
    #                 ]}
    #         }}
    # }

    edges = r['organization']['membersWithRole']['edges']

    member_ids = [e['node']['id'] for e in edges]
    # e.g., ['MDQ6VXNlcjEzODgwODE=', 'MDQ6VXNlcjE1Njg1Njk3']
    # Base64 encoded. To decode, use base64.b64decode
    # [b'04:User1388081', b'04:User15685697']
    return member_ids

##__________________________________________________________________||
def is_member(user_token, admin_token):
    github_org = current_app.config['GITHUB_ORG']
    member_ids = get_org_member_ids(org_name=github_org, token=admin_token)
    user_id = get_user_id(user_token)
    return user_id in member_ids

##__________________________________________________________________||
