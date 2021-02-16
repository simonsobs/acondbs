from flask import Blueprint, current_app
from flask_graphql import GraphQLView

from .. import auth, schema
from .graphql_ide import GRAPHIQL_NEWER, GRAPHQL_PLAYGROUND

##__________________________________________________________________||
# from flask import request
# class GraphQLView(GraphQLView):
#     def print_request(self):
#         import json
#         import textwrap
#         h = request.headers
#         h = str(h)
#         data_dict = json.loads(request.data)
#         m = '\n'.join([
#             textwrap.dedent('''
#             {}:
#             {}
#             ''').lstrip().format(k, textwrap.indent(str(v), '    ').rstrip()) for k, v in data_dict.items()]
#         )
#         msg = textwrap.dedent('''
#         - received header
#         {h}
#         - received query
#         {q}
#         --- end ---
#         ''').format(
#             h=textwrap.indent(h, '    '),
#             q=textwrap.indent(m, '    ')
#         )
#         print(msg)
#     def dispatch_request(self):
#         try:
#             self.print_request()
#         except BaseException as error:
#             import traceback
#             traceback.print_exc()
#         return super().dispatch_request()

class GraphQLViewW(GraphQLView):
    '''A wrapper of GraphQLView.

    Used to determine arguments to GraphQLView.as_view() for each view
    based on on the configuration and request.

    The usual usage of GraphQLView in add_url_rule() as in the document
    (https://github.com/graphql-python/flask-graphql/tree/v2.0.1#usage) is
    as follows
      bp.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

    The arguments (schema, graphiql) need to have already been
    determined when the module is imported. In this app, they have not
    because they depend on the configuration and request.

    The __init__() will be called in each view from
    https://github.com/pallets/flask/blob/1.1.2/src/flask/views.py#L88

    The arguments are determined in In __init__() and given to the
    base class GraphQLView.

    '''
    def __init__(self, **kwargs):
        kwargs.update({
            'schema': _select_schema(),
            'graphiql': current_app.config.get('ACONDBS_GRAPHIQL', False),
            'graphiql_template': _select_graphiql_template()
        })
        super().__init__(**kwargs)

##__________________________________________________________________||
bp = Blueprint('graphql', __name__)
bp.add_url_rule('/graphql', view_func=GraphQLViewW.as_view('graphql'))

def init_app(app):
    app.register_blueprint(bp)

##__________________________________________________________________||
def _select_schema():
    if auth.is_admin():
        return schema.schema_admin
    elif auth.is_signed_in():
        return schema.schema_private
    else:
        return schema.schema_public

def _select_graphiql_template():
    template_no = current_app.config.get('ACONDBS_GRAPHIQL_TEMPLATE_NO', None)
    if template_no == 1:
        return GRAPHIQL_NEWER
    elif template_no == 2:
        return GRAPHQL_PLAYGROUND
    else:
        return None

##__________________________________________________________________||
