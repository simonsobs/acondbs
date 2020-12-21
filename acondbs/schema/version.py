import graphene

##__________________________________________________________________||
def resolve_version(parent, info):
    from .. import __version__
    return __version__

version_field = graphene.Field(
    graphene.String,
    description='The version of Acondbs',
    resolver=resolve_version
    )

##__________________________________________________________________||
