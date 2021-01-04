"""Queries to GitHub API
"""

from .call import call_graphql_api

##__________________________________________________________________||
def org(login, token):
    query = """
      query Organization($login: String!) {
        organization(login: $login) {
          id
          login
        }
      }
    """
    variables = { "login": login }
    r = call_graphql_api(query=query, variables=variables, token=token)
    # e.g.,
    #   {
    #     "organization": {
    #       "id": "MDEyOk9yZ2FuaXphdGlvbjc1NjMxODQ0",
    #       "login": "urban-octo-disco"
    #     }
    #   }

    return r['organization']

##__________________________________________________________________||
def org_members(org_login, token):
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
    variables = { "org_login": org_login }
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
                name
                avatarUrl
              }
            }
          }
        }
      }
    """
    variables = { "org_login": org_login, "first": nmembers }
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
    #                         'login': 'TaiSakuma',
    #                         'name': 'Tai Sakuma',
    #                         'avatarUrl': 'https://avatars0.githubusercontent.com/u/1388081?v=4'
    #                     },
    #                     'role': 'MEMBER'
    #                 },
    #                 {
    #                     'node': {
    #                         'id': 'MDQ6VXNlcjE1Njg1Njk3',
    #                         'login': 'tai-sakuma',
    #                         'name': None,
    #                         'avatarUrl': 'https://avatars0.githubusercontent.com/u/15685697?v=4'
    #                     },
    #                     'role': 'ADMIN'
    #                 }
    #             ]}
    #     }
    # }

    edges = r['organization']['membersWithRole']['edges']

    return edges

##__________________________________________________________________||
def viewer(token):
    query = '{ viewer { login id name avatarUrl } }'
    r = call_graphql_api(query=query, token=token)
    # e.g., https://github.com/octocat
    # {
    #     "viewer": {
    #         "id": "MDQ6VXNlcjU4MzIzMQ==",
    #         "login": "octocat",
    #         "name": "The Octocat",
    #         "avatarUrl": "https://avatars3.githubusercontent.com/u/583231?u=a59fef2a493e2b67dd13754231daf220c82ba84d&v=4"
    #     }
    # }
    user = r.get('viewer')
    return user

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
