import datetime
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import Beam as BeamModel

from ..db.sa import sa
from ..db.backup import request_backup_db

from .common import CommonCreateInputFields, CommonUpdateInputFields

##__________________________________________________________________||
class Beam(SQLAlchemyObjectType):
    class Meta:
        model = BeamModel
        interfaces = (relay.Node, )

# class BeamConnection(relay.Connection):
#      class Meta:
#          node = Beam

## The class "BeamConnection" is commented out because it causes the error
## "AssertionError: Found different types with the same name in the schema:
## BeamConnection, BeamConnection". In the class "Query" in schema.py
## "Beam._meta.connection" is used instead. This solution was mentioned in the
## issue
## https://github.com/graphql-python/graphene-sqlalchemy/issues/153#issuecomment-478744077

##__________________________________________________________________||
class CreateBeamInput(graphene.InputObjectType, CommonCreateInputFields):
    pass

class UpdateBeamInput(graphene.InputObjectType, CommonUpdateInputFields):
    pass

class CreateBeam(graphene.Mutation):
    class Arguments:
        input = CreateBeamInput(required=True)

    ok = graphene.Boolean()
    beam = graphene.Field(lambda: Beam)

    def mutate(root, info, input):
        beam = BeamModel(**input)
        today = datetime.date.today()
        beam.date_posted = today
        sa.session.add(beam)
        sa.session.commit()
        ok = True
        request_backup_db()
        return CreateBeam(beam=beam, ok=ok)

class UpdateBeam(graphene.Mutation):
    class Arguments:
        product_id = graphene.Int()
        input = UpdateBeamInput(required=True)

    ok = graphene.Boolean()
    beam = graphene.Field(lambda: Beam)

    def mutate(root, info, product_id, input):
        beam = BeamModel.query.filter_by(product_id=product_id).first()
        for k, v in input.items():
            setattr(beam, k, v)
        sa.session.commit()
        ok = True
        request_backup_db()
        return UpdateBeam(beam=beam, ok=ok)

class DeleteBeam(graphene.Mutation):
    class Arguments:
        product_id = graphene.Int()

    ok = graphene.Boolean()

    def mutate(root, info, product_id):
        beam = BeamModel.query.filter_by(product_id=product_id).first()
        sa.session.delete(beam)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteBeam(ok=ok)

##__________________________________________________________________||
