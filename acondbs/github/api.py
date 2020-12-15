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
    #                 "id": "MDQ6VXNlcjU4MzIzMQ==",
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

    return response

##__________________________________________________________________||
def get_user(token):
    query = '{ viewer { login name avatarUrl } }'
    r = call_api(query=query, token=token)
    # e.g.,
    #  {
    #      "data": {
    #          "viewer": {
    #              "id": "MDQ6VXNlcjU4MzIzMQ==",
    #              "name": "The Octocat",
    #              "avatarUrl": "https://avatars3.githubusercontent.com/u/583231?u=a59fef2a493e2b67dd13754231daf220c82ba84d&v=4"
    #          }
    #      }
    #  }
    user = r.get('data', {}).get('viewer')
    return user

##__________________________________________________________________||
def get_user_id(token):
    headers = {
         'Authorization': 'token {}'.format(token)
    }

    json = {'query': '{ viewer { id } }'}

    r = requests.post('https://api.github.com/graphql', json=json, headers=headers)

    r = r.json()
    # examples:
    #   success:
    #     r = {
    #         "data": {
    #             "viewer": {
    #                 "id": "MDQ6VXNlcjU4MzIzMQ=="
    #             }
    #         }
    #     }
    #
    #   error (bad credentials):
    #     r = {'message': 'Bad credentials', 'documentation_url': 'https://docs.github.com/graphql'}
    #
    #   error (query error):
    #     r = {'errors': [
    #         {
    #             'path': ['query', 'viewer', 'idii'],
    #             'extensions': {'code': 'undefinedField', 'typeName': 'User', 'fieldName': 'idii'},
    #             'locations': [{'line': 1, 'column': 12}],
    #             'message': "Field 'idii' doesn't exist on type 'User'"
    #         }
    #     ]}

    if 'errors' in r:
      raise Exception(r['errors'])

    ret = r.get('data', {}).get('viewer', {}).get('id')
    return ret

##__________________________________________________________________||
def get_org_member_ids(org_name, token):

    headers = {
         'Authorization': 'bearer {}'.format(token)
    }

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
    json = {'query': query, 'variables': variables }
    r = requests.post('https://api.github.com/graphql', json=json, headers=headers)
    r = r.json()
    # examples:
    #   success:
    #     r = {
    #         'data': {
    #             'organization': {
    #                 'login': 'urban-octo-disco',
    #                 'membersWithRole': {'totalCount': 2}
    #             }
    #         }
    #     }
    #   error:
    #     r = {
    #         'data': {'organization': None},
    #         'errors': [{
    #             'extensions': {'saml_failure': False},
    #             'locations': [{'column': 11, 'line': 5}],
    #             'message': 'Although you appear to have the correct authorization '
    #                        'credentials, the `simonsobs` organization has enabled '
    #                        'OAuth App access restrictions, meaning that data '
    #                        'access to third-parties is limited. For more '
    #                        'information on these restrictions, including how to '
    #                        'whitelist this app, visit '
    #                        'https://docs.github.com/articles/restricting-access-to-your-organization-s-data/',
    #             'path': ['organization', 'membersWithRole'],
    #             'type': 'FORBIDDEN'
    #         }]
    #     }

    if 'errors' in r:
      raise Exception(r['errors'])

    nmembers = r['data']['organization']['membersWithRole']['totalCount']

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
    json = {'query': query, 'variables': variables }
    r = requests.post('https://api.github.com/graphql', json=json, headers=headers)
    r = r.json()

    # examples:
    #   success:
    #     r = {
    #         'data': {
    #             'organization': {
    #                 'login': 'urban-octo-disco',
    #                 'membersWithRole': {
    #                     'edges': [
    #                         {
    #                             'node': {
    #                                 'id': 'MDQ6VXNlcjEzODgwODE=',
    #                                 'login': 'TaiSakuma'
    #                             },
    #                             'role': 'MEMBER'
    #                         },
    #                         {
    #                             'node': {
    #                                 'id': 'MDQ6VXNlcjE1Njg1Njk3',
    #                                 'login': 'tai-sakuma'
    #                             },
    #                             'role': 'ADMIN'
    #                         }
    #                     ]}
    #             }}
    #     }
    #   error:
    #     r = {
    #         'data': { 'organization': None},
    #         'errors': [{
    #             'extensions': {'saml_failure': False},
    #             'locations': [{'column': 11, 'line': 5}],
    #             'message': 'Although you appear to have the correct authorization '
    #                        'credentials, the `simonsobs` organization has enabled '
    #                        'OAuth App access restrictions, meaning that data '
    #                        'access to third-parties is limited. For more '
    #                        'information on these restrictions, including how to '
    #                        'whitelist this app, visit '
    #                        'https://docs.github.com/articles/restricting-access-to-your-organization-s-data/',
    #             'path': ['organization', 'membersWithRole'],
    #             'type': 'FORBIDDEN'
    #         }]
    #     }

    from pprint import pprint
    pprint(r)
    if 'errors' in r:
      raise Exception(r['errors'])

    edges = r['data']['organization']['membersWithRole']['edges']
    print(edges)

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
