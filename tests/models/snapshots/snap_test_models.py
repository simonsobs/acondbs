# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_models 1'] = {
    'product_file_paths': GenericRepr("Table('product_file_paths', MetaData(bind=None), Column('path_id', Integer(), table=<product_file_paths>, primary_key=True, nullable=False), Column('path', Text(), table=<product_file_paths>), Column('note', Text(), table=<product_file_paths>), Column('product_id', Integer(), ForeignKey('products.product_id'), table=<product_file_paths>), schema=None)"),
    'product_relation_types': GenericRepr("Table('product_relation_types', MetaData(bind=None), Column('type_id', Integer(), table=<product_relation_types>, primary_key=True, nullable=False), Column('name', Text(), table=<product_relation_types>, nullable=False), schema=None)"),
    'product_relations': GenericRepr("Table('product_relations', MetaData(bind=None), Column('relation_id', Integer(), table=<product_relations>, primary_key=True, nullable=False), Column('type_id', Integer(), ForeignKey('product_relation_types.type_id'), table=<product_relations>), Column('self_product_id', Integer(), ForeignKey('products.product_id'), table=<product_relations>), Column('other_product_id', Integer(), ForeignKey('products.product_id'), table=<product_relations>), Column('reverse_relation_id', Integer(), ForeignKey('product_relations.relation_id'), table=<product_relations>), schema=None)"),
    'product_types': GenericRepr("Table('product_types', MetaData(bind=None), Column('type_id', Integer(), table=<product_types>, primary_key=True, nullable=False), Column('name', Text(), table=<product_types>, nullable=False), schema=None)"),
    'products': GenericRepr("Table('products', MetaData(bind=None), Column('product_id', Integer(), table=<products>, primary_key=True, nullable=False), Column('type_id', Integer(), ForeignKey('product_types.type_id'), table=<products>), Column('name', Text(), table=<products>, nullable=False), Column('contact', Text(), table=<products>), Column('date_produced', Date(), table=<products>), Column('produced_by', Text(), table=<products>), Column('date_posted', Date(), table=<products>), Column('posted_by', Text(), table=<products>), Column('date_updated', Date(), table=<products>), Column('updated_by', Text(), table=<products>), Column('note', Text(), table=<products>), schema=None)")
}
