import pytest

from ...funcs import assert_query

GITHUB_OAUTH_APP_INFO = '''
{
  gitHubOAuthAppInfo {
    clientId
    authorizeUrl
    redirectUri
  }
}
'''

# __________________________________________________________________||
params = [
    pytest.param(
        [GITHUB_OAUTH_APP_INFO, ],
        {},
        id='query'
    ),
]

# __________________________________________________________________||
@pytest.mark.parametrize('args, kwags', params)
def test_schema(app, snapshot, args, kwags):
    assert_query(app, snapshot, [args, kwags])

# __________________________________________________________________||
