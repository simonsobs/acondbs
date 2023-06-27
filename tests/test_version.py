import acondbs


def test_version() -> None:
    '''test if the version string is attached to the module'''
    assert acondbs.__version__
