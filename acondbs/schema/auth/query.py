import graphene

from ... import auth

is_signed_in_field = graphene.Field(
    graphene.Boolean, resolver=lambda *_: auth.is_signed_in()
)

is_admin_field = graphene.Field(graphene.Boolean, resolver=lambda *_: auth.is_admin())
