from project import db
from project.resources.SiteModel import SiteModel
from project.resources.sites import Sites
from project.resources.user_model import User


def add_site(full_link, user_id):
    short_link = Sites.create_shortcut()
    site = SiteModel(
        full_link=full_link,
        short_link=short_link,
        user_id=user_id
    )
    db.session.add(site)
    db.session.commit()
    return site


def add_user(username, email, password):
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user
