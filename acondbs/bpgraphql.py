from flask import Blueprint, request

from .db import get_db

##__________________________________________________________________||
bp = Blueprint('graphql', __name__)

##__________________________________________________________________||
def init_app(app):
    app.register_blueprint(bp)

##__________________________________________________________________||
@bp.route('/graphql')
def graphql():
    return ""

##__________________________________________________________________||
