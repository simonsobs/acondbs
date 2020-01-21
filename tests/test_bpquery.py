from flask import json

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

    print(un_jsonified)
    assert 2 == len(un_jsonified)
    assert {'schema', 'data'} == un_jsonified.keys()
    assert 2 == len(un_jsonified['schema']['fields'])
    assert ['id', 'name'] == [f['name'] for f in un_jsonified['schema']['fields']]
    assert 13 == len(un_jsonified['data'])
    assert {'id': 1001, 'name': 'e20180309'} == un_jsonified['data'][0]

##__________________________________________________________________||
