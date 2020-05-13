import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import MapFilePath as MapFilePathModel

from ..db.sa import sa
from ..db.backup import request_backup_db

from .common import CommonCreateFilePathInputFields, CommonUpdateFilePathInputFields

##__________________________________________________________________||
class MapFilePath(SQLAlchemyObjectType):
    class Meta:
        model = MapFilePathModel
        interfaces = (relay.Node, )

##__________________________________________________________________||
class CreateMapFilePathInput(graphene.InputObjectType, CommonCreateFilePathInputFields):
    pass

class UpdateMapFilePathInput(graphene.InputObjectType, CommonUpdateFilePathInputFields):
    pass

class CreateMapFilePath(graphene.Mutation):
    class Arguments:
        input = CreateMapFilePathInput(required=True)

    ok = graphene.Boolean()
    mapFilePath = graphene.Field(lambda: MapFilePath)

    def mutate(root, info, input):
        mapFilePath = MapFilePathModel(**input)
        sa.session.add(mapFilePath)
        sa.session.commit()
        ok = True
        request_backup_db()
        return CreateMapFilePath(mapFilePath=mapFilePath, ok=ok)

class UpdateMapFilePath(graphene.Mutation):
    class Arguments:
        path_id = graphene.Int()
        input = UpdateMapFilePathInput(required=True)

    ok = graphene.Boolean()
    mapFilePath = graphene.Field(lambda: MapFilePath)

    def mutate(root, info, path_id, input):
        mapFilePath = MapFilePathModel.query.filter_by(path_id=path_id).first()
        for k, v in input.items():
            setattr(mapFilePath, k, v)
        sa.session.commit()
        ok = True
        request_backup_db()
        return UpdateMapFilePath(mapFilePath=mapFilePath, ok=ok)

class DeleteMapFilePath(graphene.Mutation):
    class Arguments:
        path_id = graphene.Int()

    ok = graphene.Boolean()

    def mutate(root, info, path_id):
        mapFilePath = MapFilePathModel.query.filter_by(path_id=path_id).first()
        sa.session.delete(mapFilePath)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteMapFilePath(ok=ok)

##__________________________________________________________________||
