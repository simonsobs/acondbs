import pytest

from ...funcs import assert_query

QUERY = '{ isAdmin }'

# __________________________________________________________________||
params = [
    pytest.param(
        [QUERY, ], { }, [],
        {
            "environ_base": {'HTTP_AUTHORIZATION': 'Bearer 90b2ee5fed25506df04fd37343bb68d1803dd97f'}
        },
        id='octocat'
    ),
    pytest.param(
        [QUERY, ], { }, [],
        {
            "environ_base": {'HTTP_AUTHORIZATION': 'Bearer 0fb8c9e16d6f7c4961c4c49212bf197d79f14080'}
        },
        id='dojocat'
    ),
    pytest.param(
        [QUERY, ], { }, [],
        {
            "environ_base": {'HTTP_AUTHORIZATION': 'Bearer 1a2d18f270df3abacfb85c5413b668f97794b4ce'}
        },
        id='wrong-token'
    ),
    pytest.param(
        [QUERY, ], { }, [],
        {
            "environ_base": {}
        },
        id='no-token'
    ),
]

@pytest.mark.parametrize('args, kwargs, request_args, request_kwargs', params)
def test_success(app, snapshot, args, kwargs, request_args, request_kwargs):

    # Note: Because the request is used to get headers, "environ_base"
    # to test_request_context() is used rather than "context_value" to
    # client.execute()

    with app.test_request_context(*request_args, **request_kwargs):
        assert_query(app, snapshot, [args, kwargs])

# __________________________________________________________________||
