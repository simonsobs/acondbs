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
graphiql = None
graphiql_template = None

class GraphQLViewW(GraphQLView):
    '''A wrapper of GraphQLView.

    used to determine arguments to GraphQLView.as_view() in init_app()
    where app.config is accessible.

    The usual usage of GraphQLView in add_url_rule() as in the document
    (https://github.com/graphql-python/flask-graphql/tree/v2.0.1#usage) is
    as follows
      bp.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

    The arguments, schema and graphiql, need to have already been
    determined.

    In this app, the arguments have not yet been determined because their
    creations depend on the configuration. The configuration is only
    available in the app context.

    The __init__() will be called in each view from
    https://github.com/pallets/flask/blob/1.1.2/src/flask/views.py#L88

    In __init__(), the arguments are obtained from global variables and are
    given to __init__() of GraphQLView.

    '''
    def __init__(self, **kwargs):
        kwargs['schema'] = schema
        kwargs['graphiql'] = graphiql
        kwargs['graphiql_template'] = graphiql_template
        super().__init__(**kwargs)


bp.add_url_rule('/graphql', view_func=GraphQLViewW.as_view('graphql'))

##__________________________________________________________________||
def init_app(app):
    global schema, graphiql, graphiql_template
    with app.app_context():
        enable_mutation = not app.config.get('ACONDBS_SCHEME_MUTATION_DISABLE', False)
        graphiql = app.config.get('ACONDBS_GRAPHIQL', False)
        graphiql_template_no = app.config.get('ACONDBS_GRAPHIQL_TEMPLATE_NO', None)

        if graphiql_template_no == 1:
            graphiql_template = GRAPHIQL_TEMPLATE
        elif graphiql_template_no == 2:
            graphiql_template = PLAYGROUND_TEMPLATE

    schema = create_schema(enable_mutation=enable_mutation)

    app.register_blueprint(bp)

##__________________________________________________________________||
# Based on https://github.com/graphql/graphiql/blob/codemirror-graphql@1.0.0/examples/graphiql-cdn/index.html
# To obtain fetchURL, inserted the lines https://github.com/graphql-python/flask-graphql/blob/v2.0.1/flask_graphql/render_graphiql.py#L33-L64
GRAPHIQL_TEMPLATE = '''<!--
 *  Copyright (c) 2021 GraphQL Contributors
 *  All rights reserved.
 *
 *  This source code is licensed under the license found in the
 *  LICENSE file in the root directory of this source tree.
-->
<!DOCTYPE html>
<html>
  <head>
    <style>
      body {
        height: 100%;
        margin: 0;
        width: 100%;
        overflow: hidden;
      }

      #graphiql {
        height: 100vh;
      }
    </style>

    <!--
      This GraphiQL example depends on Promise and fetch, which are available in
      modern browsers, but can be "polyfilled" for older browsers.
      GraphiQL itself depends on React DOM.
      If you do not want to rely on a CDN, you can host these files locally or
      include them directly in your favored resource bunder.
    -->
    <script
      crossorigin
      src="https://unpkg.com/react@16/umd/react.development.js"
    ></script>
    <script
      crossorigin
      src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"
    ></script>

    <!--
      These two files can be found in the npm module, however you may wish to
      copy them directly into your environment, or perhaps include them in your
      favored resource bundler.
     -->
    <link rel="stylesheet" href="https://unpkg.com/graphiql/graphiql.min.css" />
  </head>

  <body>
    <div id="graphiql">Loading...</div>
    <script
      src="https://unpkg.com/graphiql/graphiql.min.js"
      type="application/javascript"
    ></script>
    <script src="/renderExample.js" type="application/javascript"></script>
    <script>
      // Collect the URL parameters
      var parameters = {};
      window.location.search.substr(1).split('&').forEach(function (entry) {
        var eq = entry.indexOf('=');
        if (eq >= 0) {
          parameters[decodeURIComponent(entry.slice(0, eq))] =
            decodeURIComponent(entry.slice(eq + 1));
        }
      });

      // Produce a Location query string from a parameter object.
      function locationQuery(params) {
        return '?' + Object.keys(params).map(function (key) {
          return encodeURIComponent(key) + '=' +
            encodeURIComponent(params[key]);
        }).join('&');
      }

      // Derive a fetch URL from the current URL, sans the GraphQL parameters.
      var graphqlParamNames = {
        query: true,
        variables: true,
        operationName: true
      };

      var otherParams = {};
      for (var k in parameters) {
        if (parameters.hasOwnProperty(k) && graphqlParamNames[k] !== true) {
          otherParams[k] = parameters[k];
        }
      }
      var fetchURL = locationQuery(otherParams);


      function graphQLFetcher(graphQLParams) {
        return fetch(
          fetchURL,
          {
            method: 'post',
            headers: {
              Accept: 'application/json',
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(graphQLParams),
            credentials: 'omit',
          },
        ).then(function (response) {
          return response.json().catch(function () {
            return response.text();
          });
        });
      }

      ReactDOM.render(
        React.createElement(GraphiQL, {
          fetcher: graphQLFetcher,
          defaultVariableEditorOpen: true,
        }),
        document.getElementById('graphiql'),
      );
    </script>
  </body>
</html>'''

##__________________________________________________________________||
# From https://github.com/graphql/graphql-playground/blob/v1.8.10/packages/graphql-playground-html/minimal.html
PLAYGROUND_TEMPLATE = '''<!DOCTYPE html>
<html>

<head>
  <meta charset=utf-8/>
  <meta name="viewport" content="user-scalable=no, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, minimal-ui">
  <title>GraphQL Playground</title>
  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/graphql-playground-react/build/static/css/index.css" />
  <link rel="shortcut icon" href="//cdn.jsdelivr.net/npm/graphql-playground-react/build/favicon.png" />
  <script src="//cdn.jsdelivr.net/npm/graphql-playground-react/build/static/js/middleware.js"></script>
</head>

<body>
  <div id="root">
    <style>
      body {
        background-color: rgb(23, 42, 58);
        font-family: Open Sans, sans-serif;
        height: 90vh;
      }

      #root {
        height: 100%;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
      }

      .loading {
        font-size: 32px;
        font-weight: 200;
        color: rgba(255, 255, 255, .6);
        margin-left: 20px;
      }

      img {
        width: 78px;
        height: 78px;
      }

      .title {
        font-weight: 400;
      }
    </style>
    <img src='//cdn.jsdelivr.net/npm/graphql-playground-react/build/logo.png' alt=''>
    <div class="loading"> Loading
      <span class="title">GraphQL Playground</span>
    </div>
  </div>
  <script>window.addEventListener('load', function (event) {
      GraphQLPlayground.init(document.getElementById('root'), {
        // options as 'endpoint' belong here
      })
    })</script>
</body>

</html>'''

##__________________________________________________________________||
