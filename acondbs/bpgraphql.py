from flask import Blueprint, request
from flask_graphql import GraphQLView

from .schema import create_schema

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

##__________________________________________________________________||
bp = Blueprint('graphql', __name__)

schema = None

class GraphQLViewW(GraphQLView):
    '''A wrapper.

    used to create schema in init_app() where app.config is accessible.


    The usual usage of GraphQLView in add_url_rule() as in the document
    (https://github.com/graphql-python/flask-graphql/tree/v2.0.1#usage) is as
    follows
      bp.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
    The schema needs to have already been created.

    In this app, the schema has not yet been created because its creation
    depends on the configuration. The configuration is only available in the
    app context. The schema is created in init_app().

    The __init__() will be called in each view from
    https://github.com/pallets/flask/blob/1.1.2/src/flask/views.py#L88

    In __init__(), schema is retrieved from schema_holder and is given to
    __init__() of GraphQLView.

    '''
    def __init__(self, **kwargs):
        kwargs['schema'] = schema
        super().__init__(**kwargs)


bp.add_url_rule('/graphql', view_func=GraphQLViewW.as_view('graphql', graphiql=True))

##__________________________________________________________________||
def init_app(app):
    global schema
    with app.app_context():
        enable_mutation = not app.config.get('ACONDBS_SCHEME_MUTATION_DISABLE', False)
    schema = create_schema(enable_mutation=enable_mutation)

    app.register_blueprint(bp)

##__________________________________________________________________||
