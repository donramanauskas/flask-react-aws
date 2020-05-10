# services/users/manage.py


import sys

from flask.cli import FlaskGroup

from project import create_app, db
from project.api.users.models import User


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    """
    Cretes few db entries for testing.
    """
    db.session.add(User(username="user1", email="user@gmail.com", password="supersecret"))
    db.session.add(User(username="user2", email="user3l@mherman.org", password="supersecret"))
    db.session.commit()


if __name__ == "__main__":
    cli()
