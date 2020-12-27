"""Call GitHub APIs
"""

import requests

API_URL = 'https://api.github.com/graphql'

##__________________________________________________________________||
def call_graphql_api(query, variables=None, token=None):
    """Call a GitHub GraphQL API

    Parameters
    ----------
    query : str
        A GraphQL query, e.g.,
        'query User($login: String!) { user(login: $login) { name } }'
    variables: dict, optional
        Variables for the query, e.g., {"login": "octocat"}
    token: str, optional
        An access token

    Returns
    -------
    dict
        The data field of the query results, e.g.,
        { "user": { "name": "The Octocat" } }

    Raises
    ------
    Exception
        If the query results include the field "errors" or don't include the
        field "data."
    """

    headers = {}
    if token:
      headers['Authorization'] = 'token {}'.format(token)

    json = {'query': query }
    if variables:
        json['variables'] = variables

    # example:
    #   headers = {'Authorization': 'token XXXXXXXXXXXXXXXXXXXX'}
    #   json = {
    #       'query': (
    #           'query User($login: String!) '
    #           '{ user(login: $login) { name } }'
    #       ),
    #       'variables': {"login": "octocat"}
    #   }


    response = requests.post(API_URL, json=json, headers=headers)
    response = response.json()
    # examples:
    #   success:
    #     response = {"data": {"user": {"name": "The Octocat"} } }
    #
    #   error: (note: the 'data' field might not exist.)
    #     response = {
    #         "data": {"user": null},
    #         "errors": [
    #             {
    #                 "type": "NOT_FOUND",
    #                 "path": ["user"],
    #                 "locations": [{"line": 7, "column": 3 }],
    #                 "message": "Could not resolve to a User with the login of 'octocat'."
    #             }
    #         ]
    #     }
    #
    #   bad credentials:
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
