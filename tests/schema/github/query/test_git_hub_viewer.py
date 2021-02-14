import pytest
import textwrap

from graphene import Context
from werkzeug.datastructures import Headers

from ...funcs import assert_query

QUERY = '{ gitHubViewer { login name avatarUrl } }'

# __________________________________________________________________||
params = [
    pytest.param(
        [QUERY, ],
        {
            "context_value": Context(
                headers=Headers(
                    {'Authorization': 'Bearer "token1"'}
            ))
        },
        id='one'
    ),
]

@pytest.mark.parametrize('args, kwags', params)
def test_success(app, snapshot, args, kwags):
    assert_query(app, snapshot, [args, kwags])

# __________________________________________________________________||
params = [
    pytest.param(
        [QUERY, ],
        {
            "context_value": Context(
                headers=Headers(
                    {'Authorization': 'Bearer "no-such-token"'}
            ))
        },
        id='wrong-token'
    ),
    pytest.param(
        [QUERY, ],
        { },
        id='no-token'
    ),
]

@pytest.mark.parametrize('args, kwags', params)
def test_error(app, snapshot, args, kwags):
    assert_query(app, snapshot, [args, kwags], error=True)

# __________________________________________________________________||
