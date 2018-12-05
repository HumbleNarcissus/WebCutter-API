from project import db
from project.resources.SiteModel import SiteModel
from project.resources.sites import Sites

def add_site(full_link):
    short_link = Sites.create_shortcut()
    site = SiteModel(full_link=full_link, short_link=short_link)
    db.session.add(site)
    db.session.commit()
    return site