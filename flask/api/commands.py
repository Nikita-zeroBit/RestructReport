import click
from flask import Flask, current_app, g

from .database import DBTools


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    # from api.auth.models import UserRole, User, Profile, Role
    DBTools.init_db()
    click.echo('Initialized the database.')


def load_commands(app: Flask) -> None:
    from api.database import db
    app.cli.add_command(init_db_command)
