
import pytest
import unittest.mock as mock

from acondbs.misc import githubauth

##__________________________________________________________________||
@pytest.fixture(autouse=True)
def mock_requests(monkeypatch):
    y = mock.Mock()
    monkeypatch.setattr("acondbs.misc.githubauth.requests", y)
    yield y


##__________________________________________________________________||
def test_success(app, mock_requests):

    token = 'token-xxx'

    r = {"login": "octocat", "id": 1, "node_id": "MDQ6VXNlcjE="}
    mock_requests.get().json.return_value = r
    with app.app_context():
        username = githubauth.get_username(token)

    assert 'octocat' == username

##__________________________________________________________________||
def test_error(app, mock_requests):

    token = 'token-xxx'

    r = {'message': 'Bad credentials', 'documentation_url': 'https://docs.github.com/rest'}
    mock_requests.get().json.return_value = r
    with app.app_context():
        username = githubauth.get_username(token)

    assert username is None

##__________________________________________________________________||
