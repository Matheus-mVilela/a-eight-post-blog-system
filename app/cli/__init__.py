import click
from sqlalchemy_utils import create_database, database_exists

from app.database import DB_URL


@click.group()
def main():
    """root"""
    pass


@main.command()
def create_db():
    if not database_exists(DB_URL):
        try:
            create_database(DB_URL)
        except Exception as exc:
            print(exc)
        else:
            print('Created database')
    else:
        print('Database already exists')
