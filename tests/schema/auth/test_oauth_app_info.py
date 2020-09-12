import pytest

from ..funcs import assert_query

OAUTH_APP_INFO = '''
{
  oauthAppInfo {
    clientId
    authorizeUrl
    tokenUrl
    redirectUri
  }
}
'''

##__________________________________________________________________||
params = [
    pytest.param(
        [OAUTH_APP_INFO],
        { }
    )
]

##__________________________________________________________________||
@pytest.mark.parametrize('args, kwags', params)
def test_schema(app, snapshot, args, kwags):
    assert_query(app, snapshot, [args, kwags])

##__________________________________________________________________||
