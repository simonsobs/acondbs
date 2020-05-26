import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import Product as ProductModel
from ..models import ProductRelation as ProductRelationModel
from ..models import ProductRelationType as ProductRelationTypeModel

from ..db.sa import sa
from ..db.backup import request_backup_db

from .filter_ import PFilterableConnectionField

##__________________________________________________________________||
class ProductRelation(SQLAlchemyObjectType):
    class Meta:
        model = ProductRelationModel
        interfaces = (graphene.relay.Node, )
        connection_field_factory = PFilterableConnectionField.factory

##__________________________________________________________________||
class CreateProductRelationInput(graphene.InputObjectType):
    type_id = graphene.Int(required=True)
    self_product_id = graphene.Int(required=True)
    other_product_id = graphene.Int(required=True)

##__________________________________________________________________||
class CreateProductRelation(graphene.Mutation):
    class Arguments:
        input = CreateProductRelationInput(required=True)

    ok = graphene.Boolean()
    product_relation = graphene.Field(lambda: ProductRelation)

    def mutate(root, info, input):
        type_ = ProductRelationTypeModel.query.filter_by(type_id=input['type_id']).one()
        self_ = ProductModel.query.filter_by(product_id=input['self_product_id']).one()
        other = ProductModel.query.filter_by(product_id=input['other_product_id']).one()

        relation = ProductRelationModel()
        relation.type_ = type_
        relation.self_ = self_
        relation.other = other

        sa.session.add(relation)
        sa.session.commit()
        ok = True
        request_backup_db()
        return CreateProductRelation(product_relation=relation, ok=ok)

class DeleteProductRelation(graphene.Mutation):
    class Arguments:
        relation_id = graphene.Int()

    ok = graphene.Boolean()

    def mutate(root, info, relation_id):
        relation = ProductRelationModel.query.filter_by(relation_id=relation_id).one_or_none()
        sa.session.delete(relation)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteProductRelation(ok=ok)

##__________________________________________________________________||
