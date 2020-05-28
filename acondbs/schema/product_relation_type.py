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
    '''A type of relations between products'''
    class Meta:
        model = ProductRelationTypeModel
        interfaces = (graphene.relay.Node, )
        connection_field_factory = PFilterableConnectionField.factory

##__________________________________________________________________||
class CreateProductRelationTypeInput(graphene.InputObjectType):
    '''An input to createProductRelationTypes()'''
    name = graphene.String(
        required=True,
        description=('The name of the relation type'))
    indef_article = graphene.String(
        description=('The indefinite article placed before the singular noun "'
                     'i.e., "a" or "an". '))
    singular = graphene.String(
        description=('The singular noun, the relation type name in singular.'))
    plural = graphene.String(
        description=('The plural noun, the relation type name in plural.'))

##__________________________________________________________________||
class CreateProductRelationTypes(graphene.Mutation):
    '''Create a pair of product relation types'''
    class Arguments:
        type = CreateProductRelationTypeInput(
            required=True,
            description=('A relation type'))
        reverse = CreateProductRelationTypeInput(
            description=('The reverse relation type'))
        self_reverse = graphene.Boolean(
            description=('true if the reverse type is the same'))

    ok = graphene.Boolean()
    product_relation_type = graphene.Field(lambda: ProductRelationType)

    def mutate(root, info, type, reverse=None, self_reverse=False):
        if self_reverse and reverse:
            from graphql import GraphQLError
            raise GraphQLError('"reverse" is given when "self_reverse" is True')
        model = ProductRelationTypeModel(**type)
        if self_reverse:
            model.reverse = model
        else:
            reverse_ = ProductRelationTypeModel(**reverse)
            model.reverse = reverse_
        sa.session.add(model)
        sa.session.commit()
        ok = True
        request_backup_db()
        return CreateProductRelationTypes(product_relation_type=model, ok=ok)

class DeleteProductRelationTypes(graphene.Mutation):
    '''Delete a pair of product relation types'''
    class Arguments:
        type_id = graphene.Int(
            required=True,
            description=('The typeId of a relation type. The reverse relation '
                         'type will also be deleted.'))

    ok = graphene.Boolean()

    def mutate(root, info, type_id):
        model = ProductRelationTypeModel.query.filter_by(type_id=type_id).one()
        sa.session.delete(model)
        sa.session.commit()
        ok = True
        request_backup_db()
        return DeleteProductRelationTypes(ok=ok)

##__________________________________________________________________||
