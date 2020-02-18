import os

from flask import Flask
from flask_cors import CORS

##__________________________________________________________________||
DEFAULT_CONFIG_DICT = dict(
    SECRET_KEY='dev',
    SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

##__________________________________________________________________||
def create_app(config_path=None, **kwargs):

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_mapping(**DEFAULT_CONFIG_DICT)

    if config_path is not None:
        if not os.path.isabs(config_path):
            # If `config_path` is relative, it is considered relative
            # to the current working directory.
            config_path = os.path.join(os.getcwd(), config_path)

            # Note: `app.config.from_pyfile()` treats a relative path
            # either a) relative to the top directory of the app,
            # i.e., the directory in which this file is, if
            # `instance_relative_config` is `False`, or b) relative to
            # the "instance folder", a specific directory described in
            # https://flask.palletsprojects.com/en/1.1.x/config/#instance-folders),
            # if `instance_relative_config` is `True`.

        app.config.from_pyfile(config_path, silent=False)

    app.config.from_mapping(**kwargs)

    from . import db
    db.init_app(app)

    from . import bpquery
    bpquery.init_app(app)

    from . import bpgraphql
    bpgraphql.init_app(app)

    CORS(app, resources={r'/*': {'origins': '*'}})

    return app

##__________________________________________________________________||

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
