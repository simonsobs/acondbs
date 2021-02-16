# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_selection[False-False] 1'] = {
    'data': {
        '__schema': {
            'mutationType': {
                'fields': [
                    {
                        'name': 'authenticateWithGitHub'
                    }
                ]
            },
            'queryType': {
                'fields': [
                    {
                        'name': 'webConfig'
                    },
                    {
                        'name': 'isSignedIn'
                    },
                    {
                        'name': 'gitHubOAuthAppInfo'
                    }
                ]
            },
            'subscriptionType': None
        }
    }
}

snapshots['test_schema_selection[False-True] 1'] = {
    'data': {
        '__schema': {
            'mutationType': {
                'fields': [
                    {
                        'name': 'authenticateWithGitHub'
                    },
                    {
                        'name': 'createProduct'
                    },
                    {
                        'name': 'deleteProduct'
                    },
                    {
                        'name': 'updateProduct'
                    },
                    {
                        'name': 'createProductFilePath'
                    },
                    {
                        'name': 'deleteProductFilePath'
                    },
                    {
                        'name': 'updateProductFilePath'
                    },
                    {
                        'name': 'createProductRelation'
                    },
                    {
                        'name': 'deleteProductRelation'
                    },
                    {
                        'name': 'createProductRelationTypes'
                    },
                    {
                        'name': 'deleteProductRelationTypes'
                    },
                    {
                        'name': 'updateProductRelationType'
                    },
                    {
                        'name': 'createProductType'
                    },
                    {
                        'name': 'deleteProductType'
                    },
                    {
                        'name': 'updateProductType'
                    }
                ]
            },
            'queryType': {
                'fields': [
                    {
                        'name': 'webConfig'
                    },
                    {
                        'name': 'isSignedIn'
                    },
                    {
                        'name': 'gitHubOAuthAppInfo'
                    },
                    {
                        'name': 'version'
                    },
                    {
                        'name': 'alembicVersion'
                    },
                    {
                        'name': 'isAdmin'
                    },
                    {
                        'name': 'allProducts'
                    },
                    {
                        'name': 'allProductTypes'
                    },
                    {
                        'name': 'allProductRelations'
                    },
                    {
                        'name': 'allProductRelationTypes'
                    },
                    {
                        'name': 'allProductFilePaths'
                    },
                    {
                        'name': 'product'
                    },
                    {
                        'name': 'productType'
                    },
                    {
                        'name': 'productRelation'
                    },
                    {
                        'name': 'productRelationType'
                    },
                    {
                        'name': 'node'
                    }
                ]
            },
            'subscriptionType': None
        }
    }
}

snapshots['test_schema_selection[True-False] 1'] = {
    'data': {
        '__schema': {
            'mutationType': {
                'fields': [
                    {
                        'name': 'authenticateWithGitHub'
                    },
                    {
                        'name': 'createProduct'
                    },
                    {
                        'name': 'deleteProduct'
                    },
                    {
                        'name': 'updateProduct'
                    },
                    {
                        'name': 'createProductFilePath'
                    },
                    {
                        'name': 'deleteProductFilePath'
                    },
                    {
                        'name': 'updateProductFilePath'
                    },
                    {
                        'name': 'createProductRelation'
                    },
                    {
                        'name': 'deleteProductRelation'
                    },
                    {
                        'name': 'createProductRelationTypes'
                    },
                    {
                        'name': 'deleteProductRelationTypes'
                    },
                    {
                        'name': 'updateProductRelationType'
                    },
                    {
                        'name': 'createProductType'
                    },
                    {
                        'name': 'deleteProductType'
                    },
                    {
                        'name': 'updateProductType'
                    },
                    {
                        'name': 'addGitHubOrg'
                    },
                    {
                        'name': 'deleteGitHubOrg'
                    },
                    {
                        'name': 'addGitHubAdminAppToken'
                    },
                    {
                        'name': 'deleteGitHubAdminAppToken'
                    },
                    {
                        'name': 'updateGitHubOrgMemberLists'
                    }
                ]
            },
            'queryType': {
                'fields': [
                    {
                        'name': 'webConfig'
                    },
                    {
                        'name': 'isSignedIn'
                    },
                    {
                        'name': 'gitHubOAuthAppInfo'
                    },
                    {
                        'name': 'version'
                    },
                    {
                        'name': 'alembicVersion'
                    },
                    {
                        'name': 'isAdmin'
                    },
                    {
                        'name': 'allProducts'
                    },
                    {
                        'name': 'allProductTypes'
                    },
                    {
                        'name': 'allProductRelations'
                    },
                    {
                        'name': 'allProductRelationTypes'
                    },
                    {
                        'name': 'allProductFilePaths'
                    },
                    {
                        'name': 'product'
                    },
                    {
                        'name': 'productType'
                    },
                    {
                        'name': 'productRelation'
                    },
                    {
                        'name': 'productRelationType'
                    },
                    {
                        'name': 'node'
                    },
                    {
                        'name': 'allGitHubOrgs'
                    },
                    {
                        'name': 'allGitHubUsers'
                    },
                    {
                        'name': 'allGitHubTokens'
                    },
                    {
                        'name': 'gitHubViewer'
                    }
                ]
            },
            'subscriptionType': None
        }
    }
}

snapshots['test_schema_selection[True-True] 1'] = {
    'data': {
        '__schema': {
            'mutationType': {
                'fields': [
                    {
                        'name': 'authenticateWithGitHub'
                    },
                    {
                        'name': 'createProduct'
                    },
                    {
                        'name': 'deleteProduct'
                    },
                    {
                        'name': 'updateProduct'
                    },
                    {
                        'name': 'createProductFilePath'
                    },
                    {
                        'name': 'deleteProductFilePath'
                    },
                    {
                        'name': 'updateProductFilePath'
                    },
                    {
                        'name': 'createProductRelation'
                    },
                    {
                        'name': 'deleteProductRelation'
                    },
                    {
                        'name': 'createProductRelationTypes'
                    },
                    {
                        'name': 'deleteProductRelationTypes'
                    },
                    {
                        'name': 'updateProductRelationType'
                    },
                    {
                        'name': 'createProductType'
                    },
                    {
                        'name': 'deleteProductType'
                    },
                    {
                        'name': 'updateProductType'
                    },
                    {
                        'name': 'addGitHubOrg'
                    },
                    {
                        'name': 'deleteGitHubOrg'
                    },
                    {
                        'name': 'addGitHubAdminAppToken'
                    },
                    {
                        'name': 'deleteGitHubAdminAppToken'
                    },
                    {
                        'name': 'updateGitHubOrgMemberLists'
                    }
                ]
            },
            'queryType': {
                'fields': [
                    {
                        'name': 'webConfig'
                    },
                    {
                        'name': 'isSignedIn'
                    },
                    {
                        'name': 'gitHubOAuthAppInfo'
                    },
                    {
                        'name': 'version'
                    },
                    {
                        'name': 'alembicVersion'
                    },
                    {
                        'name': 'isAdmin'
                    },
                    {
                        'name': 'allProducts'
                    },
                    {
                        'name': 'allProductTypes'
                    },
                    {
                        'name': 'allProductRelations'
                    },
                    {
                        'name': 'allProductRelationTypes'
                    },
                    {
                        'name': 'allProductFilePaths'
                    },
                    {
                        'name': 'product'
                    },
                    {
                        'name': 'productType'
                    },
                    {
                        'name': 'productRelation'
                    },
                    {
                        'name': 'productRelationType'
                    },
                    {
                        'name': 'node'
                    },
                    {
                        'name': 'allGitHubOrgs'
                    },
                    {
                        'name': 'allGitHubUsers'
                    },
                    {
                        'name': 'allGitHubTokens'
                    },
                    {
                        'name': 'gitHubViewer'
                    }
                ]
            },
            'subscriptionType': None
        }
    }
}
