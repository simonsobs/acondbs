from typing import Any, Mapping
from unittest import mock

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from ....funcs import assert_mutation
from ...gql import MUTATION_UPDATE_PRODUCT

QUERY = '''
{
  allProducts {
    edges {
      node {
        name
      }
    }
  }
  allProductRelations {
    edges {
      node {
        type_ {
          name
        }
        self_ {
          name
        }
        other {
          name
        }
      }
    }
  }
  allProductFilePaths {
    edges {
      node {
        path
      }
    }
  }
}
'''

HEADERS = {
    'Authorization': 'Bearer 39d86487d76a84087f1da599c872dac4473e5f07',  # user1
}


params = [
    pytest.param(
        {
            'query': MUTATION_UPDATE_PRODUCT,
            'variables': {
                'productId': 1,
                'input': {
                    'note': '- updated note 123',
                    'attributes': {
                        'unicodeText': [
                            {'fieldId': 1, 'value': 'new-contact'},
                        ],
                    },
                },
            },
        },
        {'query': QUERY},
        id='update',
    ),
    pytest.param(
        {
            'query': MUTATION_UPDATE_PRODUCT,
            'variables': {
                'productId': 1,
                'input': {
                    'name': 'new-name',
                },
            },
        },
        {'query': QUERY},
        id='update-name',
    ),
    pytest.param(
        {
            'query': MUTATION_UPDATE_PRODUCT,
            'variables': {
                'productId': 1,
                'input': {
                    'paths': [
                        'site1:/path/to/map1',
                        'site2:/updated/way/map1',
                        'site4:/additional/map1',
                    ],
                },
            },
        },
        {'query': QUERY},
        id='update-paths',
    ),
    pytest.param(
        {
            'query': MUTATION_UPDATE_PRODUCT,
            'variables': {
                'productId': 1,
                'input': {
                    'paths': [],
                },
            },
        },
        {'query': QUERY},
        id='delete-paths',
    ),
    pytest.param(
        {
            'query': MUTATION_UPDATE_PRODUCT,
            'variables': {
                'productId': 5,
                'input': {
                    'relations': [
                        {'typeId': 1, 'productId': 4},
                        {'typeId': 1, 'productId': 2},
                    ],
                },
            },
        },
        {'query': QUERY},
        id='update-relations',
    ),
    pytest.param(
        {
            'query': MUTATION_UPDATE_PRODUCT,
            'variables': {
                'productId': 5,
                'input': {
                    'relations': [],
                },
            },
        },
        {'query': QUERY},
        id='delete-relations',
    ),
]


@pytest.mark.parametrize('data_mutation, data_query', params)
@pytest.mark.asyncio
async def test_schema_success(
    app: Flask,
    snapshot: PyTestSnapshotTest,
    data_mutation: Mapping[str, Any],
    data_query: Mapping[str, Any],
    mock_request_backup_db: mock.Mock,
) -> None:
    success = True
    await assert_mutation(
        app,
        snapshot,
        data_mutation,
        HEADERS,
        data_query,
        HEADERS,
        mock_request_backup_db,
        success,
    )


params = [
    pytest.param(
        {
            'query': MUTATION_UPDATE_PRODUCT,
            'variables': {
                'productId': 1,
                'input': {
                    'name': 'map2',
                },
            },
        },
        {'query': QUERY},
        id='error-constraint',
    ),
]


@pytest.mark.parametrize('data_mutation, data_query', params)
@pytest.mark.asyncio
async def test_schema_error(
    app: Flask,
    snapshot: PyTestSnapshotTest,
    data_mutation: Mapping[str, Any],
    data_query: Mapping[str, Any],
    mock_request_backup_db: mock.Mock,
) -> None:
    success = False
    await assert_mutation(
        app,
        snapshot,
        data_mutation,
        HEADERS,
        data_query,
        HEADERS,
        mock_request_backup_db,
        success,
    )
