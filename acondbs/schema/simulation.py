import datetime
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import Simulation as SimulationModel
from ..models import SimulationFilePath as SimulationFilePathModel

from ..db.sa import sa
from ..db.backup import request_backup_db

from .common import CommonCreateProductInputFields, CommonUpdateProductInputFields

##__________________________________________________________________||
class Simulation(SQLAlchemyObjectType):
    class Meta:
        model = SimulationModel
        interfaces = (relay.Node, )

##__________________________________________________________________||
class CreateSimulationInput(graphene.InputObjectType, CommonCreateProductInputFields):
    pass

class UpdateSimulationInput(graphene.InputObjectType, CommonUpdateProductInputFields):
    pass

class CreateSimulation(graphene.Mutation):
    class Arguments:
        input = CreateSimulationInput(required=True)

    ok = graphene.Boolean()
    simulation = graphene.Field(lambda: Simulation)

    def mutate(root, info, input):
        paths = input.pop('paths', None)
        product = SimulationModel(**input)
        if paths:
            product.paths = ([SimulationFilePathModel(path=p) for p in paths])
        today = datetime.date.today()
        product.date_posted = today
        sa.session.add(product)
        sa.session.commit()
        ok = True
        request_backup_db()
        return CreateSimulation(simulation=product, ok=ok)

class UpdateSimulation(graphene.Mutation):
    class Arguments:
        product_id = graphene.Int()
        input = UpdateSimulationInput(required=True)

    ok = graphene.Boolean()
    simulation = graphene.Field(lambda: Simulation)

    def mutate(root, info, product_id, input):
        product = SimulationModel.query.filter_by(product_id=product_id).first()
        for k, v in input.items():
            setattr(product, k, v)
        today = datetime.date.today()
        product.date_updated = today
        sa.session.commit()
        ok = True
        request_backup_db()
        return UpdateSimulation(simulation=product, ok=ok)

class DeleteSimulation(graphene.Mutation):
    class Arguments:
        product_id = graphene.Int()

    ok = graphene.Boolean()

    def mutate(root, info, product_id):
        product = SimulationModel.query.filter_by(product_id=product_id).first()
        if product:
            for path in product.paths:
                sa.session.delete(path)
        sa.session.delete(product)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteSimulation(ok=ok)

##__________________________________________________________________||
