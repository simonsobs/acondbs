from flask import json
import pytest

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
    assert ['map_id', 'name', 'date_posted', 'mapper', 'note'] == [f['name'] for f in un_jsonified['schema']['fields']]
    assert 3 == len(un_jsonified['data'])
    assert  {'date_posted': '2019-02-13', 'map_id': 1001, 'mapper': 'pwg-pmn', 'name': 'lat20190213'}.items() <= un_jsonified['data'][0].items()

##__________________________________________________________________||
params = [
    ['1001',
     {
         'nersc:/go/to/my/maps',
     }
    ],
    ['1012',
     {
         'nersc:/go/to/my/maps_v2',
         'abcde:/path/to/the/maps_v2',
     }
    ],
]
@pytest.mark.parametrize('map_id, paths', params)
def test_paths_post(client, map_id, paths):
    data = {'map_id': map_id}
    response = client.post('/paths', data=data)
    assert 200 == response.status_code

    un_jsonified = json.loads(response.data)
    assert 2 == len(un_jsonified)
    assert {'schema', 'data'} == un_jsonified.keys()
    assert 4 == len(un_jsonified['schema']['fields'])
    assert ['map_file_path_id', 'map_id', 'path', 'note'] == [f['name'] for f in un_jsonified['schema']['fields']]
    assert len(paths) == len(un_jsonified['data'])
    assert paths == {e['path'] for e in un_jsonified['data']}

def test_paths_get(client):
    response = client.get('/paths')
    assert 200 == response.status_code

    un_jsonified = json.loads(response.data)
    # print(json.dumps(un_jsonified, indent=2))

    assert 2 == len(un_jsonified)
    assert {'schema', 'data'} == un_jsonified.keys()
    assert 4 == len(un_jsonified['schema']['fields'])
    assert ['map_file_path_id', 'map_id', 'path', 'note'] == [f['name'] for f in un_jsonified['schema']['fields']]
    assert 4 == len(un_jsonified['data'])

##__________________________________________________________________||
