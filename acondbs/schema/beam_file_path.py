import graphene
from graphene import relay
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import BeamFilePath as BeamFilePathModel

from ..db.sa import sa
from ..db.backup import request_backup_db

from .common import CommonCreateFilePathInputFields, CommonUpdateFilePathInputFields

##__________________________________________________________________||
class BeamFilePath(SQLAlchemyObjectType):
    class Meta:
        model = BeamFilePathModel
        interfaces = (relay.Node, )

##__________________________________________________________________||
class CreateBeamFilePathInput(graphene.InputObjectType, CommonCreateFilePathInputFields):
    pass

class UpdateBeamFilePathInput(graphene.InputObjectType, CommonUpdateFilePathInputFields):
    pass

class CreateBeamFilePath(graphene.Mutation):
    class Arguments:
        input = CreateBeamFilePathInput(required=True)

    ok = graphene.Boolean()
    beamFilePath = graphene.Field(lambda: BeamFilePath)

    def mutate(root, info, input):
        path = BeamFilePathModel(**input)
        sa.session.add(path)
        sa.session.commit()
        ok = True
        request_backup_db()
        return CreateBeamFilePath(beamFilePath=path, ok=ok)

class UpdateBeamFilePath(graphene.Mutation):
    class Arguments:
        path_id = graphene.Int()
        input = UpdateBeamFilePathInput(required=True)

    ok = graphene.Boolean()
    beamFilePath = graphene.Field(lambda: BeamFilePath)

    def mutate(root, info, path_id, input):
        path = BeamFilePathModel.query.filter_by(path_id=path_id).first()
        for k, v in input.items():
            setattr(path, k, v)
        sa.session.commit()
        ok = True
        request_backup_db()
        return UpdateBeamFilePath(beamFilePath=path, ok=ok)

class DeleteBeamFilePath(graphene.Mutation):
    class Arguments:
        path_id = graphene.Int()

    ok = graphene.Boolean()

    def mutate(root, info, path_id):
        path = BeamFilePathModel.query.filter_by(path_id=path_id).first()
        sa.session.delete(path)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteBeamFilePath(ok=ok)

##__________________________________________________________________||
