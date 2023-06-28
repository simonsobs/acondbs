import textwrap
from typing import Any, Mapping
from unittest import mock

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from ....funcs import assert_mutation

HEADERS = {'Authorization': 'Bearer token123'}  # octocat


params = [
    pytest.param(
        {
            'query': textwrap.dedent(
                '''
                  mutation m {
                    createProductFilePath(input: {
                      path: "nersc:/go/to/my/new_product_v1",
                      note: "- Note 1",
                      productId: 1010
                    }) { productFilePath { path } }
                  }
                ''',
            ),
        },
        {
            'query': textwrap.dedent(
                '''
                  {
                    product(productId: 1010) {
                      name timePosted note
                      paths { edges { node { path note product { productId } } } }
                    }
                  }
                ''',
            )
        },
        id='createProductFilePath',
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
    ## To find the token
    # from acondbs.models import GitHubUser
    # with app.app_context():
    #     user1 = GitHubUser.query.filter_by(login='octocat').one()
    #     print(user1)
    #     print(user1.tokens[0].token)

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
            'query': textwrap.dedent(
                '''
                  mutation m {
                    createProductFilePath(input: {
                      path: "nersc:/go/to/my/new_product_v1",
                      note: "- Note 1",
                      productId: 1010,
                      noSuchField: "xxx"
                    }) { productFilePath { path } }
                  }
                ''',
            )
        },
        {
            'query': textwrap.dedent(
                '''
                  {
                    allProductFilePaths {
                      edges {
                        node {
                          productId
                        }
                      }
                    }
                  }
                ''',
            )
        },
        id='createProductFilePath-noSuchField',
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
