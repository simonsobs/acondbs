from acondbs import create_app

##__________________________________________________________________||
def test_create_app_fixture(app):
    assert app.testing

##__________________________________________________________________||
def test_create_app_no_config():
    assert not create_app().testing

##__________________________________________________________________||
