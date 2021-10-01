import graphene

from ....db.backup import request_backup_db

from .. import type_

from .... import ops


##__________________________________________________________________||
class CommonInputFields:
    name = graphene.String(
        required=True,
        description="The name of the field",
    )


class CreateFieldInput(graphene.InputObjectType, CommonInputFields):
    """Input to createField()"""
    type_ = type_.FieldType()


class UpdateFieldInput(graphene.InputObjectType, CommonInputFields):
    """Input to updateField()"""


##__________________________________________________________________||
class CreateField(graphene.Mutation):
    """Create a product type"""

    class Arguments:
        input = CreateFieldInput(required=True)

    ok = graphene.Boolean()
    field = graphene.Field(lambda: type_.Field)

    def mutate(root, info, input):
        model = ops.create_field(**input)
        ops.commit()
        ok = True
        request_backup_db()
        return CreateField(field=model, ok=ok)


class UpdateField(graphene.Mutation):
    """Update a product type"""

    class Arguments:
        field_id = graphene.Int(required=True)
        input = UpdateFieldInput(required=True)

    ok = graphene.Boolean()
    field = graphene.Field(lambda: type_.Field)

    def mutate(root, info, field_id, input):
        model = ops.update_field(field_id, input)
        ops.commit()
        ok = True
        request_backup_db()
        return UpdateField(field=model, ok=ok)


class DeleteField(graphene.Mutation):
    """Delete a product type"""

    class Arguments:
        field_id = graphene.Int(description="The fieldId of the field")

    ok = graphene.Boolean()

    def mutate(root, info, field_id):
        ops.delete_field(field_id)
        ops.commit()
        ok = True
        request_backup_db()
        return DeleteField(ok=ok)


##__________________________________________________________________||
