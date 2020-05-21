from flask import Blueprint, request
from flask_graphql import GraphQLView

from .schema.schema import schema

##__________________________________________________________________||
# from flask import request
# class GraphQLView(GraphQLView):
#     def dispatch_request(self):
#         print(request.data)
#         return super().dispatch_request()

##__________________________________________________________________||
bp = Blueprint('graphql', __name__)

bp.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema, graphiql=True, ))

##__________________________________________________________________||
def init_app(app):
    app.register_blueprint(bp)

##__________________________________________________________________||
