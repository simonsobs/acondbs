import graphene
from alembic.migration import MigrationContext

from acondbs.db.sa import sa


def resolve_version(parent, info):
    from acondbs.__about__ import __version__

    return __version__


version_field = graphene.Field(
    graphene.String,
    description="The version of Acondbs",
    resolver=resolve_version,
)


def resolve_alembic_version(parent, info):
    with sa.engine.connect() as conn:
        context = MigrationContext.configure(conn)
        ret = context.get_current_revision()
    # e.g., "35e6ddccd22a"
    return ret


alembic_version_field = graphene.Field(
    graphene.String,
    description="The version of Alembic migration",
    resolver=resolve_alembic_version,
)
