
import pytest
import unittest.mock as mock

from acondbs.github.api import get_user
##__________________________________________________________________||
@pytest.fixture(autouse=True)
def mock_requests(monkeypatch):
    y = mock.Mock()
    monkeypatch.setattr("acondbs.github.api.requests", y)
    yield y


##__________________________________________________________________||
def test_success(app, mock_requests):

    token = 'token-xxx'

    viewer = {
        "login": "octocat",
        "name": "monalisa octocat",
        "avatar_url": "https://github.com/images/error/octocat_happy.gif"
    }
    r = {'data': {'viewer': viewer}}

    mock_requests.post().json.return_value = r
    with app.app_context():
        user = get_user(token)

    assert viewer == user

##__________________________________________________________________||
def test_bad_credentials(app, mock_requests):

    token = 'token-xxx'

    r = {'message': 'Bad credentials', 'documentation_url': 'https://docs.github.com/graphql'}
    mock_requests.post().json.return_value = r
    with app.app_context():
        with pytest.raises(Exception) as e:
            get_user(token)
    assert r == e.value.args[0]

##__________________________________________________________________||
