import datetime
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import Beam as BeamModel
from ..models import BeamFilePath as BeamFilePathModel

from ..db.sa import sa
from ..db.backup import request_backup_db

from .common import CommonCreateProductInputFields, CommonUpdateProductInputFields

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
class CreateBeamInput(graphene.InputObjectType, CommonCreateProductInputFields):
    pass

class UpdateBeamInput(graphene.InputObjectType, CommonUpdateProductInputFields):
    pass

class CreateBeam(graphene.Mutation):
    class Arguments:
        input = CreateBeamInput(required=True)

    ok = graphene.Boolean()
    beam = graphene.Field(lambda: Beam)

    def mutate(root, info, input):
        paths = input.pop('paths', None)
        product = BeamModel(**input)
        if paths:
            product.paths = ([BeamFilePathModel(path=p) for p in paths])
        today = datetime.date.today()
        product.date_posted = today
        sa.session.add(product)
        sa.session.commit()
        ok = True
        request_backup_db()
        return CreateBeam(beam=product, ok=ok)

class UpdateBeam(graphene.Mutation):
    class Arguments:
        product_id = graphene.Int()
        input = UpdateBeamInput(required=True)

    ok = graphene.Boolean()
    beam = graphene.Field(lambda: Beam)

    def mutate(root, info, product_id, input):
        product = BeamModel.query.filter_by(product_id=product_id).first()
        for k, v in input.items():
            setattr(product, k, v)
        today = datetime.date.today()
        product.date_updated = today
        sa.session.commit()
        ok = True
        request_backup_db()
        return UpdateBeam(beam=product, ok=ok)

class DeleteBeam(graphene.Mutation):
    class Arguments:
        product_id = graphene.Int()

    ok = graphene.Boolean()

    def mutate(root, info, product_id):
        product = BeamModel.query.filter_by(product_id=product_id).first()
        if product:
            for path in product.paths:
                sa.session.delete(path)
        sa.session.delete(product)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteBeam(ok=ok)

##__________________________________________________________________||
