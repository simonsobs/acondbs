from acondbs.db.sa import sa

# __________________________________________________________________||
def test_models(app):
    '''test the models declared
    '''
    expected = {'simulations', 'simulation_path', 'maps', 'beams', 'map_file_paths'}
    model_names = sa.Model.metadata.tables.keys()
    assert expected == model_names

# __________________________________________________________________||
