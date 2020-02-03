from flask import Flask
from flask_cors import CORS

##__________________________________________________________________||
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    from . import db
    db.init_app(app)

    from . import bpquery
    bpquery.init_app(app)

    from . import bpgraphql
    bpgraphql.init_app(app)

    CORS(app, resources={r'/*': {'origins': '*'}})

    return app

##__________________________________________________________________||
