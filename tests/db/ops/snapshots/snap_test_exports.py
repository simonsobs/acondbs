# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_export_db_to_dict_of_dict_list 1'] = {
    'beam_file_paths': [
        {
            'note': '',
            'path': 'BEAM_DEPOT/Beams/20190304',
            'path_id': 1,
            'product_id': 1070
        },
        {
            'note': '',
            'path': 'BEAM_DEPOT/Beams/20190607',
            'path_id': 2,
            'product_id': 1120
        },
        {
            'note': '',
            'path': 'BEAM_DEPOT/Beams/20200123',
            'path_id': 3,
            'product_id': 1130
        },
        {
            'note': '',
            'path': 'BEAM_DEPOT/Beams/20200207',
            'path_id': 4,
            'product_id': 1150
        }
    ],
    'beams': [
        {
            'contact': 'pwg-pmn',
            'date_posted': GenericRepr('datetime.date(2018, 1, 1)'),
            'date_produced': GenericRepr('datetime.date(2018, 1, 1)'),
            'date_updated': None,
            'input_beam_product_id': '',
            'input_map_product_id': '',
            'name': '20180101',
            'note': '- test entry',
            'posted_by': 'pwg-pmn',
            'produced_by': 'pwg-pmn',
            'product_id': 1010,
            'updated_by': ''
        },
        {
            'contact': 'pwg-pmn',
            'date_posted': GenericRepr('datetime.date(2019, 3, 4)'),
            'date_produced': GenericRepr('datetime.date(2019, 3, 4)'),
            'date_updated': None,
            'input_beam_product_id': '',
            'input_map_product_id': '',
            'name': '20190304',
            'note': '- test entry',
            'posted_by': 'pwg-pmn',
            'produced_by': 'pwg-pmn',
            'product_id': 1070,
            'updated_by': ''
        },
        {
            'contact': 'pwg-pmn',
            'date_posted': GenericRepr('datetime.date(2019, 6, 7)'),
            'date_produced': GenericRepr('datetime.date(2019, 6, 7)'),
            'date_updated': None,
            'input_beam_product_id': '',
            'input_map_product_id': '',
            'name': '20190607',
            'note': '- test entry',
            'posted_by': 'pwg-pmn',
            'produced_by': 'pwg-pmn',
            'product_id': 1120,
            'updated_by': ''
        },
        {
            'contact': 'pwg-pmn',
            'date_posted': GenericRepr('datetime.date(2020, 1, 23)'),
            'date_produced': GenericRepr('datetime.date(2020, 1, 23)'),
            'date_updated': None,
            'input_beam_product_id': '',
            'input_map_product_id': 1012,
            'name': '20200123',
            'note': '- test entry',
            'posted_by': 'pwg-pmn',
            'produced_by': 'pwg-pmn',
            'product_id': 1130,
            'updated_by': ''
        },
        {
            'contact': 'pwg-pmn',
            'date_posted': GenericRepr('datetime.date(2020, 2, 7)'),
            'date_produced': GenericRepr('datetime.date(2020, 2, 7)'),
            'date_updated': None,
            'input_beam_product_id': 1130,
            'input_map_product_id': 1013,
            'name': '20200207',
            'note': '- test entry',
            'posted_by': 'pwg-pmn',
            'produced_by': 'pwg-pmn',
            'product_id': 1150,
            'updated_by': ''
        }
    ],
    'map_file_paths': [
        {
            'note': '',
            'path': 'nersc:/go/to/my/maps',
            'path_id': 1,
            'product_id': 1001
        },
        {
            'note': 'lat only',
            'path': 'nersc:/go/to/my/maps_v2',
            'path_id': 2,
            'product_id': 1012
        },
        {
            'note': 'lat only',
            'path': 'abcde:/path/to/the/maps_v2',
            'path_id': 3,
            'product_id': 1012
        },
        {
            'note': 'lat only',
            'path': 'nersc:/go/to/my/maps_v3',
            'path_id': 4,
            'product_id': 1013
        }
    ],
    'maps': [
        {
            'contact': 'pwg-pmn',
            'date_posted': GenericRepr('datetime.date(2019, 2, 13)'),
            'date_produced': GenericRepr('datetime.date(2019, 2, 13)'),
            'date_updated': GenericRepr('datetime.date(2019, 2, 13)'),
            'name': 'lat20190213',
            'note': '''- This is a dummy test with a lat map
- This should not depend on any beam''',
            'posted_by': 'pwg-pmn',
            'produced_by': 'pwg-pmn',
            'product_id': 1001,
            'updated_by': 'pwg-pmn'
        },
        {
            'contact': 'pwg-pmn',
            'date_posted': GenericRepr('datetime.date(2020, 1, 20)'),
            'date_produced': GenericRepr('datetime.date(2020, 1, 20)'),
            'date_updated': GenericRepr('datetime.date(2020, 1, 20)'),
            'name': 'lat20200120',
            'note': '''- This is a dummy test with a lat map
- A beam depends on this map''',
            'posted_by': 'pwg-pmn',
            'produced_by': 'pwg-pmn',
            'product_id': 1012,
            'updated_by': 'pwg-pmn'
        },
        {
            'contact': 'pwg-pmn',
            'date_posted': GenericRepr('datetime.date(2020, 2, 1)'),
            'date_produced': GenericRepr('datetime.date(2020, 2, 1)'),
            'date_updated': GenericRepr('datetime.date(2020, 2, 1)'),
            'name': 'lat20200201',
            'note': '''- This is a dummy test with a lat map
- A beam depends on this map''',
            'posted_by': 'pwg-pmn',
            'produced_by': 'pwg-pmn',
            'product_id': 1013,
            'updated_by': 'pwg-pmn'
        }
    ],
    'product_file_paths': [
        {
            'note': '',
            'path': 'nersc:/go/to/my/maps',
            'path_id': 1,
            'product_id': 1001
        },
        {
            'note': 'lat only',
            'path': 'nersc:/go/to/my/maps_v2',
            'path_id': 2,
            'product_id': 1012
        },
        {
            'note': 'lat only',
            'path': 'abcde:/path/to/the/maps_v2',
            'path_id': 3,
            'product_id': 1012
        },
        {
            'note': 'lat only',
            'path': 'nersc:/go/to/my/maps_v3',
            'path_id': 4,
            'product_id': 1013
        },
        {
            'note': '',
            'path': 'BEAM_DEPOT/Beams/20190304',
            'path_id': 5,
            'product_id': 1070
        },
        {
            'note': '',
            'path': 'BEAM_DEPOT/Beams/20190607',
            'path_id': 6,
            'product_id': 1120
        },
        {
            'note': '',
            'path': 'BEAM_DEPOT/Beams/20200123',
            'path_id': 7,
            'product_id': 1130
        },
        {
            'note': '',
            'path': 'BEAM_DEPOT/Beams/20200207',
            'path_id': 8,
            'product_id': 1150
        },
        {
            'note': '',
            'path': 'nersc:/go/to/my/simulations',
            'path_id': 9,
            'product_id': 1002
        },
        {
            'note': '',
            'path': 'abcde:/path/to/the/simulations',
            'path_id': 10,
            'product_id': 1002
        }
    ],
    'product_relation_types': [
        {
            'name': 'parent',
            'type_id': 1
        },
        {
            'name': 'child',
            'type_id': 2
        }
    ],
    'product_relations': [
    ],
    'product_types': [
        {
            'name': 'map',
            'product_type_id': 1
        },
        {
            'name': 'beam',
            'product_type_id': 2
        },
        {
            'name': 'simulation',
            'product_type_id': 3
        },
        {
            'name': 'anchor',
            'product_type_id': 4
        }
    ],
    'products': [
        {
            'contact': 'pwg-pmn',
            'date_posted': GenericRepr('datetime.date(2019, 2, 13)'),
            'date_produced': GenericRepr('datetime.date(2019, 2, 13)'),
            'date_updated': GenericRepr('datetime.date(2019, 2, 13)'),
            'name': 'lat20190213',
            'note': '''- This is a dummy test with a lat map
- This should not depend on any beam''',
            'posted_by': 'pwg-pmn',
            'produced_by': 'pwg-pmn',
            'product_id': 1001,
            'product_type_id': 1,
            'updated_by': 'pwg-pmn'
        },
        {
            'contact': 'abc-def',
            'date_posted': GenericRepr('datetime.date(2019, 3, 15)'),
            'date_produced': GenericRepr('datetime.date(2019, 3, 15)'),
            'date_updated': None,
            'name': 'xyz-s1234-20200101',
            'note': '''- note 1
- note 2''',
            'posted_by': 'abc-def',
            'produced_by': 'abc-def',
            'product_id': 1002,
            'product_type_id': 3,
            'updated_by': ''
        },
        {
            'contact': 'pwg-pmn',
            'date_posted': GenericRepr('datetime.date(2018, 1, 1)'),
            'date_produced': GenericRepr('datetime.date(2018, 1, 1)'),
            'date_updated': None,
            'name': '20180101',
            'note': '- test entry',
            'posted_by': 'pwg-pmn',
            'produced_by': 'pwg-pmn',
            'product_id': 1010,
            'product_type_id': 2,
            'updated_by': ''
        },
        {
            'contact': 'pwg-pmn',
            'date_posted': GenericRepr('datetime.date(2020, 1, 20)'),
            'date_produced': GenericRepr('datetime.date(2020, 1, 20)'),
            'date_updated': GenericRepr('datetime.date(2020, 1, 20)'),
            'name': 'lat20200120',
            'note': '''- This is a dummy test with a lat map
- A beam depends on this map''',
            'posted_by': 'pwg-pmn',
            'produced_by': 'pwg-pmn',
            'product_id': 1012,
            'product_type_id': 1,
            'updated_by': 'pwg-pmn'
        },
        {
            'contact': 'pwg-pmn',
            'date_posted': GenericRepr('datetime.date(2020, 2, 1)'),
            'date_produced': GenericRepr('datetime.date(2020, 2, 1)'),
            'date_updated': GenericRepr('datetime.date(2020, 2, 1)'),
            'name': 'lat20200201',
            'note': '''- This is a dummy test with a lat map
- A beam depends on this map''',
            'posted_by': 'pwg-pmn',
            'produced_by': 'pwg-pmn',
            'product_id': 1013,
            'product_type_id': 1,
            'updated_by': 'pwg-pmn'
        },
        {
            'contact': 'pwg-pmn',
            'date_posted': GenericRepr('datetime.date(2019, 3, 4)'),
            'date_produced': GenericRepr('datetime.date(2019, 3, 4)'),
            'date_updated': None,
            'name': '20190304',
            'note': '- test entry',
            'posted_by': 'pwg-pmn',
            'produced_by': 'pwg-pmn',
            'product_id': 1070,
            'product_type_id': 2,
            'updated_by': ''
        },
        {
            'contact': 'pwg-pmn',
            'date_posted': GenericRepr('datetime.date(2019, 6, 7)'),
            'date_produced': GenericRepr('datetime.date(2019, 6, 7)'),
            'date_updated': None,
            'name': '20190607',
            'note': '- test entry',
            'posted_by': 'pwg-pmn',
            'produced_by': 'pwg-pmn',
            'product_id': 1120,
            'product_type_id': 2,
            'updated_by': ''
        },
        {
            'contact': 'pwg-pmn',
            'date_posted': GenericRepr('datetime.date(2020, 1, 23)'),
            'date_produced': GenericRepr('datetime.date(2020, 1, 23)'),
            'date_updated': None,
            'name': '20200123',
            'note': '- test entry',
            'posted_by': 'pwg-pmn',
            'produced_by': 'pwg-pmn',
            'product_id': 1130,
            'product_type_id': 2,
            'updated_by': ''
        },
        {
            'contact': 'pwg-pmn',
            'date_posted': GenericRepr('datetime.date(2020, 2, 7)'),
            'date_produced': GenericRepr('datetime.date(2020, 2, 7)'),
            'date_updated': None,
            'name': '20200207',
            'note': '- test entry',
            'posted_by': 'pwg-pmn',
            'produced_by': 'pwg-pmn',
            'product_id': 1150,
            'product_type_id': 2,
            'updated_by': ''
        }
    ],
    'simulation_file_paths': [
        {
            'note': '',
            'path': 'nersc:/go/to/my/simulations',
            'path_id': 1,
            'product_id': 1001
        },
        {
            'note': '',
            'path': 'abcde:/path/to/the/simulations',
            'path_id': 2,
            'product_id': 1001
        }
    ],
    'simulations': [
        {
            'contact': 'abc-def',
            'date_posted': GenericRepr('datetime.date(2019, 3, 15)'),
            'date_produced': GenericRepr('datetime.date(2019, 3, 15)'),
            'date_updated': None,
            'name': 'xyz-s1234-20200101',
            'note': '''- note 1
- note 2''',
            'posted_by': 'abc-def',
            'produced_by': 'abc-def',
            'product_id': 1001,
            'updated_by': ''
        }
    ]
}
