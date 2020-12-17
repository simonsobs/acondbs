import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import WebConfig as WebConfigModel

from .connection import CountedConnection
from .filter_ import PFilterableConnectionField

##__________________________________________________________________||
class WebConfig(SQLAlchemyObjectType):
    '''Web configuration'''
    class Meta:
        model = WebConfigModel
        interfaces = (graphene.relay.Node, )
        connection_class = CountedConnection
        connection_field_factory = PFilterableConnectionField.factory

def resolve_web_config(parent, info, **kwargs):
    return WebConfig.get_query(info).one_or_none()

web_config_field = graphene.Field(WebConfig, resolver=resolve_web_config)

##__________________________________________________________________||
