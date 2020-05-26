import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models import Product as ProductModel
from ..models import ProductRelation as ProductRelationModel
from ..models import ProductRelationType as ProductRelationTypeModel

from ..db.sa import sa
from ..db.backup import request_backup_db

from .filter_ import PFilterableConnectionField

##__________________________________________________________________||
class ProductRelationType(SQLAlchemyObjectType):
    class Meta:
        model = ProductRelationTypeModel
        interfaces = (graphene.relay.Node, )
        connection_field_factory = PFilterableConnectionField.factory

##__________________________________________________________________||
class CreateProductRelationTypeInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    indef_article = graphene.String()
    singular = graphene.String()
    plural = graphene.String()

##__________________________________________________________________||
class CreateProductRelationType(graphene.Mutation):
    class Arguments:
        input = CreateProductRelationTypeInput(required=True)

    ok = graphene.Boolean()
    product_relation_type = graphene.Field(lambda: ProductRelationType)

    def mutate(root, info, input):
        type_ = ProductRelationTypeModel(**input)
        sa.session.add(type_)
        sa.session.commit()
        ok = True
        request_backup_db()
        return CreateProductRelationType(product_relation_type=type_, ok=ok)

class DeleteProductRelationType(graphene.Mutation):
    class Arguments:
        type_id = graphene.Int()

    ok = graphene.Boolean()

    def mutate(root, info, type_id):
        type_ = ProductRelationTypeModel.query.filter_by(type_id=type_id).first()
        sa.session.delete(type_)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteProductRelationType(ok=ok)

##__________________________________________________________________||
