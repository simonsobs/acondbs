from typing import Any, Mapping
from unittest import mock

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from ....funcs import assert_mutation
from ...gql import MUTATION_CREATE_PRODUCT

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

HEADERS = {'Authorization': 'Bearer 39d86487d76a84087f1da599c872dac4473e5f07'}  # user1


params = [
    pytest.param(
        {
            'query': MUTATION_CREATE_PRODUCT,
            'variables': {
                'input': {
                    'typeId': 2,
                    'name': 'beam111',
                    'note': '- Item 1',
                    'paths': [
                        '/path/to/new/product1',
                        '/another/location/of/product1',
                    ],
                    'relations': [
                        {'typeId': 1, 'productId': 1},
                        {'typeId': 1, 'productId': 5},
                    ],
                    'attributes': {
                        'unicodeText': [
                            {'fieldId': 1, 'value': 'contact-person'},
                            {'fieldId': 2, 'value': 'producer'},
                        ],
                        'date': [
                            {'fieldId': 3, 'value': '2020-02-20'},
                        ],
                    },
                }
            },
        },
        {'query': QUERY},
        id='create',
    ),
    pytest.param(
        {
            'query': MUTATION_CREATE_PRODUCT,
            'variables': {
                'input': {
                    'typeId': 1,
                    'name': 'product1',
                }
            },
        },
        {'query': QUERY},
        id='minimum',
    ),
    pytest.param(
        {
            'query': MUTATION_CREATE_PRODUCT,
            'variables': {
                'input': {
                    'typeId': 2,
                    'name': 'map1',
                    'paths': [
                        '/path/to/new/product1',
                        '/another/location/of/product1',
                    ],
                    'attributes': {
                        'unicodeText': [
                            {'fieldId': 1, 'value': 'contact-person'},
                            {'fieldId': 2, 'value': 'pwg-pmn'},
                        ],
                        'date': [],
                    },
                }
            },
        },
        {'query': QUERY},
        id='the-same-name-different-type',
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
            'query': MUTATION_CREATE_PRODUCT,
            'variables': {
                'input': {
                    'typeId': 1,
                }
            },
        },
        {'query': QUERY},
        id='error-no-name',
    ),
    pytest.param(
        {
            'query': MUTATION_CREATE_PRODUCT,
            'variables': {
                'input': {
                    'typeId': 1,
                    'name': 'map1',
                }
            },
        },
        {'query': QUERY},
        id='error-the-same-type-and-name',
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
