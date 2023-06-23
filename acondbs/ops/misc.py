from acondbs.db.backup import request_backup_db
from acondbs.db.sa import sa


def commit():
    """Commit the changes to the DB"""
    sa.session.commit()
    request_backup_db()
