from db import db

class SiteModel(db.Model):

    __tablename__ = "sites"

    id = db.Column(db.Integer, primary_key=True)
    full_link = db.Column(db.String, nullable=False)
    short_link = db.Column(db.String, nullable=False)

    def __init__(self, full_link, short_link):
        self.full_link = full_link
        self.short_link = short_link
    
    def __repr__(self):
        return 'full {}, short{}'.format(self.full_link, self.short_link)
    
    def json(self):
        return {'full_link': self.full_link, 'short_link': self.short_link}

    @classmethod    
    def find_by_fullLink(cls, site_name):
        return SiteModel.query.filter_by(full_link=site_name).first()

    @classmethod
    def return_link(cls, shortcut):
        return SiteModel.query.filter_by(short_link=shortcut).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

