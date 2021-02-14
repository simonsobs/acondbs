"""Queries to GitHub API
"""

import base64

from .call import call_graphql_api

##__________________________________________________________________||
def org(login, token):
    query = """
      query Organization($login: String!) {
        organization(login: $login) {
          id
          login
          avatarUrl
          url
        }
      }
    """
    variables = { "login": login }
    r = call_graphql_api(query=query, variables=variables, token=token)
    # e.g.,
    #   {
    #       "organization": {
    #           "id": "MDEyOk9yZ2FuaXphdGlvbjc1NjMxODQ0",
    #           "login": "urban-octo-disco",
    #           "avatarUrl": "https://avatars0.githubusercontent.com/u/75631844?v=4",
    #           "url": "https://github.com/urban-octo-disco"
    #       }
    #   }

    r['organization']['id'] = base64.b64decode(r['organization']['id']).decode()
    # e.g., "012:Organization75631844"

    return r['organization']

##__________________________________________________________________||
def org_members(org_login, token):

    first = 100

    query = """
      query OrganizationMembers($org_login: String!, $first: Int!, $after: String) {
        organization(login: $org_login) {
          login
          membersWithRole(first: $first, after: $after) {
            pageInfo {
              endCursor
              hasNextPage
            }
            edges {
              cursor
              role
              node {
                id
                login
                name
                avatarUrl
                url
              }
            }
          }
        }
      }
    """

    # an example query result:
    #   {'organization': {
    #       'login': 'urban-octo-disco',
    #       'membersWithRole': {
    #           'pageInfo': {
    #               'endCursor': 'Y3Vyc29yOnYyOpHOAO9YQQ==',
    #               'hasNextPage': False
    #           },
    #           'edges': [
    #               {
    #                   'cursor': 'Y3Vyc29yOnYyOpHOABUuMQ==',
    #                   'node': {
    #                       'id': 'MDQ6VXNlcjEzODgwODE=',
    #                       'login': 'TaiSakuma',
    #                       'name': 'Tai Sakuma',
    #                       'avatarUrl': 'https://avatars0.githubusercontent.com/u/1388081?v=4',
    #                       'url': 'https://github.com/TaiSakuma'
    #                   },
    #                   'role': 'MEMBER'
    #               },
    #               {
    #                   'cursor': 'Y3Vyc29yOnYyOpHOAO9YQQ==',
    #                   'node': {
    #                       'id': 'MDQ6VXNlcjE1Njg1Njk3',
    #                       'login': 'tai-sakuma',
    #                       'name': None,
    #                       'avatarUrl': 'https://avatars0.githubusercontent.com/u/15685697?v=4',
    #                       'url': 'https://github.com/tai-sakuma'
    #                   },
    #                   'role': 'ADMIN'
    #               }
    #           ],
    #       }}}

    variables = {"org_login": org_login, "first": first}

    edges = []
    while True:
        r = call_graphql_api(query=query, variables=variables, token=token)
        membersWithRole = r['organization']['membersWithRole']
        edges.extend(membersWithRole['edges'])
        pageInfo = membersWithRole['pageInfo']
        if not pageInfo['hasNextPage']:
            break
        variables["after"] = pageInfo['endCursor']

    for e in edges:
        e['node']['id'] = base64.b64decode(e['node']['id']).decode()

    return edges

##__________________________________________________________________||
def viewer(token):
    query = '{ viewer { login id name avatarUrl url } }'
    r = call_graphql_api(query=query, token=token)
    # e.g., https://github.com/octocat
    # {
    #     "viewer": {
    #         "id": "MDQ6VXNlcjU4MzIzMQ==",
    #         "login": "octocat",
    #         "name": "The Octocat",
    #         "avatarUrl": "https://avatars3.githubusercontent.com/u/583231?u=a59fef2a493e2b67dd13754231daf220c82ba84d&v=4",
    #         "url": "https://github.com/octocat"
    #     }
    # }

    viewer = r['viewer']

    # decode the user ID
    viewer['id'] = base64.b64decode(viewer['id']).decode()
    # e.g., '04:User583231'

    return viewer

##__________________________________________________________________||
def get_user(token):
    query = '{ viewer { login name avatarUrl } }'
    r = call_graphql_api(query=query, token=token)
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
    r = call_graphql_api(query=query, token=token)
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
    r = call_graphql_api(query=query, variables=variables, token=token)
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
    r = call_graphql_api(query=query, variables=variables, token=token)
    # e.g.,
    # {
    #     'organization': {
    #         'login': 'urban-octo-disco',
    #         'membersWithRole': {
    #             'edges': [
    #                 {
    #                     'node': {
    #                         'id': 'MDQ6VXNlcjEzODgwODE=',
    #                         'login': 'TaiSakuma'
    #                     },
    #                     'role': 'MEMBER'
    #                 },
    #                 {
    #                     'node': {
    #                         'id': 'MDQ6VXNlcjE1Njg1Njk3',
    #                         'login': 'tai-sakuma'
    #                     },
    #                     'role': 'ADMIN'
    #                 }
    #             ]}
    #     }
    # }

    edges = r['organization']['membersWithRole']['edges']

    member_ids = [e['node']['id'] for e in edges]
    # e.g., ['MDQ6VXNlcjEzODgwODE=', 'MDQ6VXNlcjE1Njg1Njk3']
    # Base64 encoded. To decode, use base64.b64decode
    # [b'04:User1388081', b'04:User15685697']
    # The 04 is the number of the letters in "User"
    # For organizations, it is 012, e.g., '012:Organization75631844'
    return member_ids

##__________________________________________________________________||
def is_member(user_token, admin_token, org_name):
    member_ids = get_org_member_ids(org_name=org_name, token=admin_token)
    user_id = get_user_id(user_token)
    return user_id in member_ids

##__________________________________________________________________||
