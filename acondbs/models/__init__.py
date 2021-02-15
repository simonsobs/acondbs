"""declare ORM models

In this packages, ORM (Object-relational mapping) models are declared.
One model is mapped to one table in the DB. Models are declared as
Python classes inheriting the Model class in Flask-SQLAlchemy.

"Declaring Models" in Flask-SQLAlchemy doc:
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

"Declare a Mapping" in SQLAlchemy doc:
https://docs.sqlalchemy.org/en/13/orm/tutorial.html#declare-a-mapping

"""

##__________________________________________________________________||
from .product import (
    ProductType,
    Product,
    ProductFilePath,
    ProductRelationType,
    ProductRelation
)

from .github import (
    GitHubToken,
    GitHubOrg,
    GitHubUser,
    GitHubOrgMembership
)

from .account import AccountAdmin

from .web import WebConfig

##__________________________________________________________________||
def init_app(app):
    _add_owners_to_db_as_admins(app)

##__________________________________________________________________||
def _add_owners_to_db_as_admins(app):
    import sqlalchemy
    from ..db.sa import sa

    # Test if tables are defined. For example, tables are not defined
    # when a migration version is being created.
    with app.app_context():
        try:
            _ = AccountAdmin.query.all()
        except sqlalchemy.exc.OperationalError as e:
            return

    with app.app_context():

        owners = app.config.get('ACONDBS_OWNERS_GITHUB_LOGINS', "")
        # e.g., "octocat,dojocat"

        owners = {e.strip() for e in owners.split(",")}
        # e.g., ["octocat", ["dojocat"]

        # remove empty strings
        owners = {e for e in owners if e}

        for owner in owners:
            if (admin := AccountAdmin.query.filter_by(git_hub_login=owner).one_or_none()) is None:
                admin = AccountAdmin(git_hub_login=owner)
                sa.session.add(admin)
        sa.session.commit()

##__________________________________________________________________||
