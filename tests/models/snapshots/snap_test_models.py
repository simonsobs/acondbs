# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_models 1'] = {
    'beam_file_paths': GenericRepr("Table('beam_file_paths', MetaData(bind=None), Column('path_id', Integer(), table=<beam_file_paths>, primary_key=True, nullable=False), Column('path', Text(), table=<beam_file_paths>), Column('note', Text(), table=<beam_file_paths>), Column('product_id', Integer(), ForeignKey('beams.product_id'), table=<beam_file_paths>), schema=None)"),
    'beams': GenericRepr("Table('beams', MetaData(bind=None), Column('product_id', Integer(), table=<beams>, primary_key=True, nullable=False), Column('name', Text(), table=<beams>, nullable=False), Column('contact', Text(), table=<beams>), Column('date_produced', Date(), table=<beams>), Column('produced_by', Text(), table=<beams>), Column('date_posted', Date(), table=<beams>), Column('posted_by', Text(), table=<beams>), Column('date_updated', Date(), table=<beams>), Column('updated_by', Text(), table=<beams>), Column('note', Text(), table=<beams>), Column('input_map_product_id', Integer(), ForeignKey('maps.product_id'), table=<beams>), Column('input_beam_product_id', Integer(), ForeignKey('beams.product_id'), table=<beams>), schema=None)"),
    'map_file_paths': GenericRepr("Table('map_file_paths', MetaData(bind=None), Column('path_id', Integer(), table=<map_file_paths>, primary_key=True, nullable=False), Column('path', Text(), table=<map_file_paths>), Column('note', Text(), table=<map_file_paths>), Column('product_id', Integer(), ForeignKey('maps.product_id'), table=<map_file_paths>), schema=None)"),
    'maps': GenericRepr("Table('maps', MetaData(bind=None), Column('product_id', Integer(), table=<maps>, primary_key=True, nullable=False), Column('name', Text(), table=<maps>, nullable=False), Column('contact', Text(), table=<maps>), Column('date_produced', Date(), table=<maps>), Column('produced_by', Text(), table=<maps>), Column('date_posted', Date(), table=<maps>), Column('posted_by', Text(), table=<maps>), Column('date_updated', Date(), table=<maps>), Column('updated_by', Text(), table=<maps>), Column('note', Text(), table=<maps>), schema=None)"),
    'product_file_paths': GenericRepr("Table('product_file_paths', MetaData(bind=None), Column('path_id', Integer(), table=<product_file_paths>, primary_key=True, nullable=False), Column('path', Text(), table=<product_file_paths>), Column('note', Text(), table=<product_file_paths>), Column('product_id', Integer(), ForeignKey('products.product_id'), table=<product_file_paths>), schema=None)"),
    'product_types': GenericRepr("Table('product_types', MetaData(bind=None), Column('product_type_id', Integer(), table=<product_types>, primary_key=True, nullable=False), Column('name', Text(), table=<product_types>, nullable=False), schema=None)"),
    'products': GenericRepr("Table('products', MetaData(bind=None), Column('product_id', Integer(), table=<products>, primary_key=True, nullable=False), Column('product_type_id', Integer(), ForeignKey('product_types.product_type_id'), table=<products>), Column('name', Text(), table=<products>, nullable=False), Column('contact', Text(), table=<products>), Column('date_produced', Date(), table=<products>), Column('produced_by', Text(), table=<products>), Column('date_posted', Date(), table=<products>), Column('posted_by', Text(), table=<products>), Column('date_updated', Date(), table=<products>), Column('updated_by', Text(), table=<products>), Column('note', Text(), table=<products>), schema=None)"),
    'simulation_file_paths': GenericRepr("Table('simulation_file_paths', MetaData(bind=None), Column('path_id', Integer(), table=<simulation_file_paths>, primary_key=True, nullable=False), Column('path', Text(), table=<simulation_file_paths>), Column('note', Text(), table=<simulation_file_paths>), Column('product_id', Integer(), ForeignKey('simulations.product_id'), table=<simulation_file_paths>), schema=None)"),
    'simulations': GenericRepr("Table('simulations', MetaData(bind=None), Column('product_id', Integer(), table=<simulations>, primary_key=True, nullable=False), Column('name', Text(), table=<simulations>, nullable=False), Column('contact', Text(), table=<simulations>), Column('date_produced', Date(), table=<simulations>), Column('produced_by', Text(), table=<simulations>), Column('date_posted', Date(), table=<simulations>), Column('posted_by', Text(), table=<simulations>), Column('date_updated', Date(), table=<simulations>), Column('updated_by', Text(), table=<simulations>), Column('note', Text(), table=<simulations>), schema=None)")
}
