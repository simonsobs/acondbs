import pytest
import textwrap

from .funcs import assert_query

##__________________________________________________________________||
ALEMBIC_VERSION = '''
{
  alembicVersion
}
'''

##__________________________________________________________________||
params = [
    pytest.param(
        [ALEMBIC_VERSION, ],
        {},
        id='alembicVersion'
    ),
]

@pytest.mark.parametrize('args, kwargs', params)
def test_schema(app, snapshot, args, kwargs):
    assert_query(app, snapshot, [args, kwargs])

    # Note: the result is None, i.e., {'data': {'alembicVersion': None }}
    # because the migration is not applied in the tests.

##__________________________________________________________________||
