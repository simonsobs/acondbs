# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_define_tables_start_with_empty_db 1'] = {
    'product_file_paths': GenericRepr("Table('product_file_paths', MetaData(bind=None), Column('path_id', INTEGER(), table=<product_file_paths>, primary_key=True, nullable=False), Column('path', TEXT(), table=<product_file_paths>), Column('note', TEXT(), table=<product_file_paths>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<product_file_paths>), schema=None)"),
    'product_relation_types': GenericRepr("Table('product_relation_types', MetaData(bind=None), Column('type_id', INTEGER(), table=<product_relation_types>, primary_key=True, nullable=False), Column('name', TEXT(), table=<product_relation_types>, nullable=False), schema=None)"),
    'product_relations': GenericRepr("Table('product_relations', MetaData(bind=None), Column('relation_id', INTEGER(), table=<product_relations>, primary_key=True, nullable=False), Column('type_id', INTEGER(), ForeignKey('product_relation_types.type_id'), table=<product_relations>), Column('self_product_id', INTEGER(), ForeignKey('products.product_id'), table=<product_relations>), Column('other_product_id', INTEGER(), ForeignKey('products.product_id'), table=<product_relations>), Column('reverse_relation_id', INTEGER(), ForeignKey('product_relations.relation_id'), table=<product_relations>), schema=None)"),
    'product_types': GenericRepr("Table('product_types', MetaData(bind=None), Column('type_id', INTEGER(), table=<product_types>, primary_key=True, nullable=False), Column('name', TEXT(), table=<product_types>, nullable=False), schema=None)"),
    'products': GenericRepr("Table('products', MetaData(bind=None), Column('product_id', INTEGER(), table=<products>, primary_key=True, nullable=False), Column('type_id', INTEGER(), ForeignKey('product_types.type_id'), table=<products>), Column('name', TEXT(), table=<products>, nullable=False), Column('contact', TEXT(), table=<products>), Column('date_produced', DATE(), table=<products>), Column('produced_by', TEXT(), table=<products>), Column('date_posted', DATE(), table=<products>), Column('posted_by', TEXT(), table=<products>), Column('date_updated', DATE(), table=<products>), Column('updated_by', TEXT(), table=<products>), Column('note', TEXT(), table=<products>), schema=None)")
}

snapshots['test_define_tables_start_with_nonempty_db 1'] = {
    'product_file_paths': GenericRepr("Table('product_file_paths', MetaData(bind=None), Column('path_id', INTEGER(), table=<product_file_paths>, primary_key=True, nullable=False), Column('path', TEXT(), table=<product_file_paths>), Column('note', TEXT(), table=<product_file_paths>), Column('product_id', INTEGER(), ForeignKey('products.product_id'), table=<product_file_paths>), schema=None)"),
    'product_relation_types': GenericRepr("Table('product_relation_types', MetaData(bind=None), Column('type_id', INTEGER(), table=<product_relation_types>, primary_key=True, nullable=False), Column('name', TEXT(), table=<product_relation_types>, nullable=False), schema=None)"),
    'product_relations': GenericRepr("Table('product_relations', MetaData(bind=None), Column('relation_id', INTEGER(), table=<product_relations>, primary_key=True, nullable=False), Column('type_id', INTEGER(), ForeignKey('product_relation_types.type_id'), table=<product_relations>), Column('self_product_id', INTEGER(), ForeignKey('products.product_id'), table=<product_relations>), Column('other_product_id', INTEGER(), ForeignKey('products.product_id'), table=<product_relations>), Column('reverse_relation_id', INTEGER(), ForeignKey('product_relations.relation_id'), table=<product_relations>), schema=None)"),
    'product_types': GenericRepr("Table('product_types', MetaData(bind=None), Column('type_id', INTEGER(), table=<product_types>, primary_key=True, nullable=False), Column('name', TEXT(), table=<product_types>, nullable=False), schema=None)"),
    'products': GenericRepr("Table('products', MetaData(bind=None), Column('product_id', INTEGER(), table=<products>, primary_key=True, nullable=False), Column('type_id', INTEGER(), ForeignKey('product_types.type_id'), table=<products>), Column('name', TEXT(), table=<products>, nullable=False), Column('contact', TEXT(), table=<products>), Column('date_produced', DATE(), table=<products>), Column('produced_by', TEXT(), table=<products>), Column('date_posted', DATE(), table=<products>), Column('posted_by', TEXT(), table=<products>), Column('date_updated', DATE(), table=<products>), Column('updated_by', TEXT(), table=<products>), Column('note', TEXT(), table=<products>), schema=None)")
}
