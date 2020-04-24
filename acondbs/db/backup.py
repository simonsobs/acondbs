"""Backup DB
"""
from pathlib import Path

from acondbs.db.ops import export_db_to_csv_files
from acondbs.misc import gitb

##__________________________________________________________________||
def backup_db_as_csv_to_github(repo_path):

    repo_path = Path(repo_path)

    for csv_file in repo_path.glob('*.csv'):
        csv_file.unlink()

    export_db_to_csv_files(repo_path)
    gitb.commit(repo_path)
    gitb.push(repo_path)

##__________________________________________________________________||
