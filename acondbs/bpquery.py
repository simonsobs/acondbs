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
def query_to_table_html(query):
    db = get_db()
    rows = db.execute(query)
    df = pd.DataFrame(rows, columns=rows.keys())
    ret = df.to_html()
    return ret

##__________________________________________________________________||
