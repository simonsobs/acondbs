import datetime
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import Map as MapModel
from ..models import MapFilePath as MapFilePathModel

from ..db.sa import sa
from ..db.backup import request_backup_db

from .common import CommonCreateProductInputFields, CommonUpdateProductInputFields

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

class UpdateMapInput(graphene.InputObjectType, CommonUpdateProductInputFields):
    pass

class CreateMap(graphene.Mutation):
    class Arguments:
        input = CreateMapInput(required=True)

    ok = graphene.Boolean()
    map = graphene.Field(lambda: Map)

    def mutate(root, info, input):
        paths = input.pop('paths', None)
        product = MapModel(**input)
        if paths:
            product.paths = ([MapFilePathModel(path=p) for p in paths])
        today = datetime.date.today()
        product.date_posted = today
        sa.session.add(product)
        sa.session.commit()
        ok = True
        request_backup_db()
        return CreateMap(map=product, ok=ok)

class UpdateMap(graphene.Mutation):
    class Arguments:
        product_id = graphene.Int()
        input = UpdateMapInput(required=True)

    ok = graphene.Boolean()
    map = graphene.Field(lambda: Map)

    def mutate(root, info, product_id, input):
        product = MapModel.query.filter_by(product_id=product_id).first()
        for k, v in input.items():
            setattr(product, k, v)
        today = datetime.date.today()
        product.date_updated = today
        sa.session.commit()
        ok = True
        request_backup_db()
        return UpdateMap(map=product, ok=ok)

class DeleteMap(graphene.Mutation):
    class Arguments:
        product_id = graphene.Int()

    ok = graphene.Boolean()

    def mutate(root, info, product_id):
        product = MapModel.query.filter_by(product_id=product_id).first()
        if product:
            for path in product.paths:
                sa.session.delete(path)
        sa.session.delete(product)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteMap(ok=ok)

##__________________________________________________________________||
