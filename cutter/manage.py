"""
Run database migrations etc.
"""

from flask.cli import FlaskGroup
from project import create_app, db

app = create_app()
cli = FlaskGroup()


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()
