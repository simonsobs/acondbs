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

@pytest.mark.parametrize('args, kwags', params)
def test_schema(app, snapshot, args, kwags):
    assert_query(app, snapshot, [args, kwags])

    # Note: the result is None, i.e., {'data': {'alembicVersion': None }}
    # because the migration is not applied in the tests.

##__________________________________________________________________||
