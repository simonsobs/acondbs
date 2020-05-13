import graphene
from graphene import relay
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import SimulationFilePath as SimulationFilePathModel

from ..db.sa import sa
from ..db.backup import request_backup_db

from .common import CommonCreateFilePathInputFields, CommonUpdateFilePathInputFields

##__________________________________________________________________||
class SimulationFilePath(SQLAlchemyObjectType):
    class Meta:
        model = SimulationFilePathModel
        interfaces = (relay.Node, )

##__________________________________________________________________||
class CreateSimulationFilePathInput(graphene.InputObjectType, CommonCreateFilePathInputFields):
    pass

class UpdateSimulationFilePathInput(graphene.InputObjectType, CommonUpdateFilePathInputFields):
    pass

class CreateSimulationFilePath(graphene.Mutation):
    class Arguments:
        input = CreateSimulationFilePathInput(required=True)

    ok = graphene.Boolean()
    simulationFilePath = graphene.Field(lambda: SimulationFilePath)

    def mutate(root, info, input):
        path = SimulationFilePathModel(**input)
        sa.session.add(path)
        sa.session.commit()
        ok = True
        request_backup_db()
        return CreateSimulationFilePath(simulationFilePath=path, ok=ok)

class UpdateSimulationFilePath(graphene.Mutation):
    class Arguments:
        path_id = graphene.Int()
        input = UpdateSimulationFilePathInput(required=True)

    ok = graphene.Boolean()
    simulationFilePath = graphene.Field(lambda: SimulationFilePath)

    def mutate(root, info, path_id, input):
        path = SimulationFilePathModel.query.filter_by(path_id=path_id).first()
        for k, v in input.items():
            setattr(path, k, v)
        sa.session.commit()
        ok = True
        request_backup_db()
        return UpdateSimulationFilePath(simulationFilePath=path, ok=ok)

class DeleteSimulationFilePath(graphene.Mutation):
    class Arguments:
        path_id = graphene.Int()

    ok = graphene.Boolean()

    def mutate(root, info, path_id):
        path = SimulationFilePathModel.query.filter_by(path_id=path_id).first()
        sa.session.delete(path)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteSimulationFilePath(ok=ok)

##__________________________________________________________________||
