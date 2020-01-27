from flask import json
import pytest

##__________________________________________________________________||
def test_tables(client):
    response = client.get('/tables')
    assert 200 == response.status_code

    un_jsonified = json.loads(response.data)
    # {"tables": {"maps": table_html, "beams": table_html, "map_path": table_html}

    assert 1 == len(un_jsonified)

    tables = un_jsonified['tables']
    assert {'maps', 'beams', 'map_path'} == tables.keys()

    for name, tbl in tables.items():
        assert tbl.startswith("<table")
        assert tbl.endswith("</table>")
        assert '<td>' in tbl
        assert 1000 <= len(tbl)

##__________________________________________________________________||
def test_query(client):
    data = {'query': 'select * from maps;'}
    response = client.post('/query', data=data)
    assert 200 == response.status_code

    un_jsonified = json.loads(response.data)

    assert 1 == len(un_jsonified)
    table_html = un_jsonified['result']
    assert 1000 <= len(table_html)
    assert table_html.startswith("<table")
    assert table_html.endswith("</table>")
    assert '<td>' in table_html

##__________________________________________________________________||
def test_maps(client):
    response = client.get('/maps')
    assert 200 == response.status_code

    un_jsonified = json.loads(response.data)
    # e.g.,
    # {'schema': {
    #     'fields': [
    #         {'name': 'id', 'type': 'integer'},
    #         {'name': 'name','type': 'string'},
    #         {'name': 'date_posted', 'type': 'string'},
    #         {'name': 'mapper', 'type': 'string'},
    #         {'name': 'note', 'type': 'string'}],
    #     'pandas_version': '0.20.0'},
    #  'data': [
    #      {
    #          'id': 1001,
    #          'name': 'e20180309',
    #          'date_posted': '2018-05-21',
    #          'mapper': 'SKN',
    #          'note': '- ...'
    #      },
    #      {
    #          ...
    #      }
    #      ]

    assert 2 == len(un_jsonified)
    assert {'schema', 'data'} == un_jsonified.keys()
    assert 5 == len(un_jsonified['schema']['fields'])
    assert ['id', 'name', 'date_posted', 'mapper', 'note'] == [f['name'] for f in un_jsonified['schema']['fields']]
    assert 15 == len(un_jsonified['data'])
    assert  {'date_posted': '2018-05-21', 'id': 1001, 'mapper': 'SKN', 'name': 'e20180309'}.items() <= un_jsonified['data'][0].items()

##__________________________________________________________________||
params = [
    ['1007',
     {
         'tiger:/home/snaess/scratch/actpol/maps/mr3_20180914/post_time/release',
         'nersc:/project/projectdirs/act/data/synced_maps/mr3_20180914',
         'niagara:/scratch/r/rbond/msyriac/synced_maps/mr3_20180914'
     }
    ],
    ['1013',
      {
          'niagara:/home/r/rbond/sigurdkn/project/actpol/maps/mr3f_20190502/release',
      }
    ],
]
@pytest.mark.parametrize('map_id, paths', params)
def test_map_path(client, map_id, paths):
    data = {'map_id': map_id}
    response = client.post('/paths', data=data)
    assert 200 == response.status_code

    un_jsonified = json.loads(response.data)
    assert 2 == len(un_jsonified)
    assert {'schema', 'data'} == un_jsonified.keys()
    assert 3 == len(un_jsonified['schema']['fields'])
    assert ['map_id', 'path', 'note'] == [f['name'] for f in un_jsonified['schema']['fields']]
    assert len(paths) == len(un_jsonified['data'])
    assert paths == {e['path'] for e in un_jsonified['data']}

##__________________________________________________________________||
