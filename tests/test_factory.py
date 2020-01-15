# Tai Sakuma <tai.sakuma@gmail.com>
from acondbs import create_app

##__________________________________________________________________||
def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

##__________________________________________________________________||
