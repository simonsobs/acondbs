import graphene

##__________________________________________________________________||
def resolve_version(parent, info):
    from .. import __version__
    return __version__

version_field = graphene.Field(graphene.String, resolver=resolve_version)

##__________________________________________________________________||
