import graphene

from sqlalchemy import MetaData

from ..db.sa import sa

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
def resolve_alembic_version(parent, info):
    tbl_name = "alembic_version"
    engine = sa.engine
    metadata = MetaData()
    metadata.reflect(bind=engine)
    print([tbl.name for tbl in metadata.sorted_tables])
    if tbl_name not in metadata.tables:
        return None
    tbl = metadata.tables[tbl_name]
    print('here')
    result_proxy = engine.execute(tbl.select())
    result_dict = [dict(r) for r in result_proxy] # e.g., [{'version_num': '63033c01def0'}]
    if result_dict:
        return result_dict[0].get('version_num')
    return None

alembic_version_field = graphene.Field(
    graphene.String,
    description='The version of Alembic migration',
    resolver=resolve_alembic_version
)

##__________________________________________________________________||
