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
class CreateProductRelationTypes(graphene.Mutation):
    class Arguments:
        type = CreateProductRelationTypeInput(required=True)
        reverse = CreateProductRelationTypeInput()
        self_reverse = graphene.Boolean()

    ok = graphene.Boolean()
    product_relation_type = graphene.Field(lambda: ProductRelationType)

    def mutate(root, info, type, reverse=None, self_reverse=False):
        if self_reverse and reverse:
            from graphql import GraphQLError
            raise GraphQLError('"reverse" is given when "self_reverse" is True')
        type_ = ProductRelationTypeModel(**type)
        if self_reverse:
            type_.reverse = type_
        else:
            reverse_ = ProductRelationTypeModel(**reverse)
            type_.reverse = reverse_
        sa.session.add(type_)
        sa.session.commit()
        ok = True
        request_backup_db()
        return CreateProductRelationTypes(product_relation_type=type_, ok=ok)

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
