import pytest
import textwrap

from acondbs import create_app
from acondbs.db.ops import define_tables

from acondbs.db.sa import sa
from acondbs.models import ProductRelationType

from ..funcs import assert_mutation

from ..gql import (
    FRAGMENT_PRODUCT_RELATION_TYPE_CONNECTION,
    CREATE_PRODUCT_RELATION_TYPES
    )

##__________________________________________________________________||
@pytest.fixture
def app_empty():
    database_uri ="sqlite:///:memory:"
    y = create_app(SQLALCHEMY_DATABASE_URI=database_uri)
    with y.app_context():
        define_tables()
    yield y

@pytest.fixture
def app(app_empty):

    y = app_empty

    #
    #  +--------+                +-------+
    #  |        | --(reverse)->  |       |
    #  | parent |                | child |
    #  |        | <-(reverse)--  |       |
    #  +--------+                +-------+
    #

    parent = ProductRelationType(name='parent')
    child = ProductRelationType(name='child')
    parent.reverse = child

    with y.app_context():
        sa.session.add(parent)
        sa.session.commit()
    yield y

##__________________________________________________________________||
QEURY = '''
{
  allProductRelationTypes {
   ...fragmentProductRelationTypeConnection
  }
}
''' + FRAGMENT_PRODUCT_RELATION_TYPE_CONNECTION

##__________________________________________________________________||
params = [
    pytest.param(
        [
            [CREATE_PRODUCT_RELATION_TYPES],
            {
                'variables': {
                    'type': {
                        'name': "plaintiff",
                        'indefArticle': "a",
                        'singular': "plaintiff",
                        'plural': "plaintiffs"
                    },
                    'reverse': {
                        'name': "defendant",
                        'indefArticle': "a",
                        'singular': "defendant",
                        'plural': "defendants"
                    },
                }}
        ],
        [[QEURY], {}],
        id='reverse'
    ),
    pytest.param(
        [
            [CREATE_PRODUCT_RELATION_TYPES],
            {
                'variables': {
                    'type': {
                        'name': "plaintiff",
                        'indefArticle': "a",
                        'singular': "plaintiff",
                        'plural': "plaintiffs"
                    },
                    'selfReverse': True
                    }
            }
        ],
        [[QEURY], {}],
        id='self_reverse'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_success(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation(app, snapshot, mutation, query,
                    mock_request_backup_db, success=True)


##__________________________________________________________________||
params = [
    pytest.param(
        [
            [CREATE_PRODUCT_RELATION_TYPES],
            {
                'variables': {
                    'type': {
                        'name': "parent",
                        'indefArticle': "a",
                        'singular': "parent",
                        'plural': "parents"
                    },
                    'reverse': {
                        'name': "child",
                        'indefArticle': "a",
                        'singular': "child",
                        'plural': "children"
                    }
                }
            },
        ],
        [[QEURY], {}],
        id='error-already-exist'
    ),
    pytest.param(
        [
            [CREATE_PRODUCT_RELATION_TYPES],
            {
                'variables': {
                    'type': {
                        'name': "plaintiff",
                        'indefArticle': "a",
                        'singular': "plaintiff",
                        'plural': "plaintiffs"
                    },
                    'reverse': {
                        'name': "defendant",
                        'indefArticle': "a",
                        'singular': "defendant",
                        'plural': "defendants"
                    },
                    'selfReverse': True
                }
            }
        ],
        [[QEURY], {}],
        id='error-reverse-and-self_reverse'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_error(app, snapshot, mutation, query, mock_request_backup_db):
    assert_mutation(app, snapshot, mutation, query,
                    mock_request_backup_db, success=False)

##__________________________________________________________________||
