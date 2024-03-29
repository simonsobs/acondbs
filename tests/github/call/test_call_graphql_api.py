import unittest.mock as mock

import pytest
from snapshottest.pytest import PyTestSnapshotTest

from acondbs.github.call import call_graphql_api


@pytest.fixture(autouse=True)
def mock_requests(monkeypatch: pytest.MonkeyPatch) -> mock.Mock:
    from acondbs.github import call

    y = mock.Mock()
    monkeypatch.setattr(call, 'requests', y)
    return y


def test_simple(mock_requests: mock.Mock, snapshot: PyTestSnapshotTest) -> None:
    query = '{ viewer { login name avatarUrl } }'
    token = 'token-xxx'

    response = {
        'data': {
            'viewer': {
                'login': 'octocat',
                'name': 'The Octocat',
                'avatarUrl': 'https://avatars3.githubusercontent.com/u/583231?u=a59fef2a493e2b67dd13754231daf220c82ba84d&v=4',
            }
        }
    }
    mock_requests.post().json.return_value = response

    r = call_graphql_api(query=query, token=token)

    assert response['data'] == r

    snapshot.assert_match(mock_requests.post.call_args_list)


def test_variables(mock_requests: mock.Mock, snapshot: PyTestSnapshotTest) -> None:
    query = '''
      query Organization($org_login: String!) {
        organization(login: $org_login) {
          login
          avatarUrl
        }
      }
    '''

    variables = {'org_login': 'urban-octo-disco'}

    token = 'token-xxx'

    response = {
        'data': {
            'organization': {
                'login': 'urban-octo-disco',
                'avatarUrl': 'https://avatars0.githubusercontent.com/u/75631844?v=4',
            }
        }
    }

    mock_requests.post().json.return_value = response

    r = call_graphql_api(query=query, variables=variables, token=token)

    assert response['data'] == r

    snapshot.assert_match(mock_requests.post.call_args_list)


def test_error(mock_requests: mock.Mock) -> None:
    query = '''
      {
        viewer {
          login
          followers {
            edges {
              node {
                id
              }
            }
          }
        }
      }
    '''

    token = 'token-xxx'

    response = {
        'errors': [
            {
                'type': 'MISSING_PAGINATION_BOUNDARIES',
                'path': ['viewer', 'followers'],
                'locations': [{'line': 9, 'column': 5}],
                'message': 'You must provide a `first` or `last` value to properly paginate the `followers` connection.',
            }
        ]
    }
    mock_requests.post().json.return_value = response

    with pytest.raises(Exception) as e:
        call_graphql_api(query=query, token=token)

    assert response['errors'] == e.value.args[0]


def test_bad_credentials(mock_requests: mock.Mock) -> None:
    query = '{ viewer { login name avatarUrl } }'
    token = 'token-xxx'

    response = {
        'message': 'Bad credentials',
        'documentation_url': 'https://docs.github.com/graphql',
    }
    mock_requests.post().json.return_value = response

    with pytest.raises(Exception) as e:
        call_graphql_api(query=query, token=token)

    assert response == e.value.args[0]
