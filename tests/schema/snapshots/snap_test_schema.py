# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_object[Simulation] 1'] = {
    'data': {
        '__type': {
            'description': None,
            'fields': [
                {
                    'name': 'productId'
                },
                {
                    'name': 'name'
                },
                {
                    'name': 'datePosted'
                },
                {
                    'name': 'mapper'
                },
                {
                    'name': 'note'
                },
                {
                    'name': 'simulationFilePaths'
                },
                {
                    'name': 'id'
                }
            ],
            'name': 'Simulation'
        }
    }
}

snapshots['test_object[SimulationConnection] 1'] = {
    'data': {
        '__type': {
            'description': None,
            'fields': [
                {
                    'name': 'pageInfo'
                },
                {
                    'name': 'edges'
                }
            ],
            'name': 'SimulationConnection'
        }
    }
}

snapshots['test_object[SimulationFilePath] 1'] = {
    'data': {
        '__type': {
            'description': None,
            'fields': [
                {
                    'name': 'pathId'
                },
                {
                    'name': 'productId'
                },
                {
                    'name': 'path'
                },
                {
                    'name': 'note'
                },
                {
                    'name': 'product'
                },
                {
                    'name': 'id'
                }
            ],
            'name': 'SimulationFilePath'
        }
    }
}

snapshots['test_object[SimulationFilePathConnection] 1'] = {
    'data': {
        '__type': {
            'description': None,
            'fields': [
                {
                    'name': 'pageInfo'
                },
                {
                    'name': 'edges'
                }
            ],
            'name': 'SimulationFilePathConnection'
        }
    }
}

snapshots['test_object[Map] 1'] = {
    'data': {
        '__type': {
            'description': None,
            'fields': [
                {
                    'name': 'name'
                },
                {
                    'name': 'contact'
                },
                {
                    'name': 'dateProduced'
                },
                {
                    'name': 'producedBy'
                },
                {
                    'name': 'datePosted'
                },
                {
                    'name': 'postedBy'
                },
                {
                    'name': 'dateUpdated'
                },
                {
                    'name': 'updatedBy'
                },
                {
                    'name': 'productId'
                },
                {
                    'name': 'note'
                },
                {
                    'name': 'paths'
                },
                {
                    'name': 'beams'
                },
                {
                    'name': 'id'
                }
            ],
            'name': 'Map'
        }
    }
}

snapshots['test_object[MapConnection] 1'] = {
    'data': {
        '__type': {
            'description': None,
            'fields': [
                {
                    'name': 'pageInfo'
                },
                {
                    'name': 'edges'
                }
            ],
            'name': 'MapConnection'
        }
    }
}

snapshots['test_object[MapFilePath] 1'] = {
    'data': {
        '__type': {
            'description': None,
            'fields': [
                {
                    'name': 'pathId'
                },
                {
                    'name': 'productId'
                },
                {
                    'name': 'path'
                },
                {
                    'name': 'note'
                },
                {
                    'name': 'product'
                },
                {
                    'name': 'id'
                }
            ],
            'name': 'MapFilePath'
        }
    }
}

snapshots['test_object[MapFilePathConnection] 1'] = {
    'data': {
        '__type': {
            'description': None,
            'fields': [
                {
                    'name': 'pageInfo'
                },
                {
                    'name': 'edges'
                }
            ],
            'name': 'MapFilePathConnection'
        }
    }
}

snapshots['test_object[Beam] 1'] = {
    'data': {
        '__type': {
            'description': None,
            'fields': [
                {
                    'name': 'productId'
                },
                {
                    'name': 'name'
                },
                {
                    'name': 'inputMapProductId'
                },
                {
                    'name': 'inputBeamProductId'
                },
                {
                    'name': 'map'
                },
                {
                    'name': 'parentBeam'
                },
                {
                    'name': 'childBeams'
                },
                {
                    'name': 'beamFilePaths'
                },
                {
                    'name': 'id'
                }
            ],
            'name': 'Beam'
        }
    }
}

snapshots['test_object[BeamConnection] 1'] = {
    'data': {
        '__type': {
            'description': None,
            'fields': [
                {
                    'name': 'pageInfo'
                },
                {
                    'name': 'edges'
                }
            ],
            'name': 'BeamConnection'
        }
    }
}

snapshots['test_object[BeamFilePath] 1'] = {
    'data': {
        '__type': {
            'description': None,
            'fields': [
                {
                    'name': 'pathId'
                },
                {
                    'name': 'productId'
                },
                {
                    'name': 'path'
                },
                {
                    'name': 'note'
                },
                {
                    'name': 'product'
                },
                {
                    'name': 'id'
                }
            ],
            'name': 'BeamFilePath'
        }
    }
}

snapshots['test_object[BeamFilePathConnection] 1'] = {
    'data': {
        '__type': {
            'description': None,
            'fields': [
                {
                    'name': 'pageInfo'
                },
                {
                    'name': 'edges'
                }
            ],
            'name': 'BeamFilePathConnection'
        }
    }
}
