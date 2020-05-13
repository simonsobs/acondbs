import datetime
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import Map as MapModel

from ..db.sa import sa
from ..db.backup import request_backup_db

from .common import CommonCreateProductInputFields, CommonUpdateInputFields

##__________________________________________________________________||
class Map(SQLAlchemyObjectType):
    class Meta:
        model = MapModel
        interfaces = (relay.Node, )

# class MapConnection(relay.Connection):
#     class Meta:
#         node = Map

## Map._meta.connection is used instead
## https://github.com/graphql-python/graphene-sqlalchemy/issues/153#issuecomment-478744077

##__________________________________________________________________||
class CreateMapInput(graphene.InputObjectType, CommonCreateProductInputFields):
    pass

class UpdateMapInput(graphene.InputObjectType, CommonUpdateInputFields):
    pass

class CreateMap(graphene.Mutation):
    class Arguments:
        input = CreateMapInput(required=True)

    ok = graphene.Boolean()
    map = graphene.Field(lambda: Map)

    def mutate(root, info, input):
        map = MapModel(**input)
        today = datetime.date.today()
        map.date_posted = today
        sa.session.add(map)
        sa.session.commit()
        ok = True
        request_backup_db()
        return CreateMap(map=map, ok=ok)

class UpdateMap(graphene.Mutation):
    class Arguments:
        product_id = graphene.Int()
        input = UpdateMapInput(required=True)

    ok = graphene.Boolean()
    map = graphene.Field(lambda: Map)

    def mutate(root, info, product_id, input):
        map = MapModel.query.filter_by(product_id=product_id).first()
        for k, v in input.items():
            setattr(map, k, v)
        today = datetime.date.today()
        map.date_updated = today
        sa.session.commit()
        ok = True
        request_backup_db()
        return UpdateMap(map=map, ok=ok)

class DeleteMap(graphene.Mutation):
    class Arguments:
        product_id = graphene.Int()

    ok = graphene.Boolean()

    def mutate(root, info, product_id):
        map = MapModel.query.filter_by(product_id=product_id).first()
        sa.session.delete(map)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteMap(ok=ok)

##__________________________________________________________________||
