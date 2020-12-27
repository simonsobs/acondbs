
import pytest
import unittest.mock as mock

from acondbs.github.query import get_user
##__________________________________________________________________||
@pytest.fixture(autouse=True)
def mock_requests(monkeypatch):
    y = mock.Mock()
    monkeypatch.setattr("acondbs.github.call.requests", y)
    yield y


##__________________________________________________________________||
def test_success(mock_requests):

    token = 'token-xxx'

    viewer = {
        "login": "octocat",
        "name": "monalisa octocat",
        "avatar_url": "https://github.com/images/error/octocat_happy.gif"
    }
    r = {'data': {'viewer': viewer}}

    mock_requests.post().json.return_value = r

    user = get_user(token)

    assert viewer == user

##__________________________________________________________________||
def test_bad_credentials(mock_requests):

    token = 'token-xxx'

    r = {'message': 'Bad credentials', 'documentation_url': 'https://docs.github.com/graphql'}
    mock_requests.post().json.return_value = r

    with pytest.raises(Exception) as e:
        get_user(token)

    assert r == e.value.args[0]

##__________________________________________________________________||
