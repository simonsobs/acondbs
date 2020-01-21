from flask import Blueprint, request, jsonify
import pandas as pd

from .db import get_db

##__________________________________________________________________||
bp = Blueprint('query', __name__)

##__________________________________________________________________||
@bp.route('/tables')
def tables():
    table_names = ['maps', 'beams', 'map_path']
    tables = { }
    for table_name in table_names:
        query_ = "SELECT * FROM {}".format(table_name)
        table_html = query_to_table_html(query_)
        tables[table_name] = table_html
    return jsonify(tables=tables)

##__________________________________________________________________||
@bp.route('/query', methods=['POST'])
def query():
    query = request.form['query']
    table_html = query_to_table_html(query)
    return jsonify(result=table_html)

##__________________________________________________________________||
@bp.route('/maps')
def maps():
    query_ = "SELECT * FROM maps"
    return query_to_table_json(query_)

##__________________________________________________________________||
def query_to_dataframe(query):
    db = get_db()
    rows = db.execute(query)
    df = pd.DataFrame(rows, columns=rows.keys())
    return df

##__________________________________________________________________||
def query_to_table_html(query):
    df = query_to_dataframe(query)
    html = df.to_html()
    return html

##__________________________________________________________________||
def query_to_table_json(query):
    df = query_to_dataframe(query)
    json = df.to_json(orient='table', index=False)
    return json

##__________________________________________________________________||
