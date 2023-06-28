from flask import Flask

from acondbs.github.ops import update_org_member_lists


def test_call(app: Flask) -> None:
    with app.app_context():
        # update_org_member_lists()
        pass
