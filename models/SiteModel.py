from db import db
from datetime import datetime, timedelta

class SiteModel(db.Model):

    __tablename__ = "sites"

    id = db.Column(db.Integer, primary_key=True)
    full_link = db.Column(db.String, nullable=False)
    short_link = db.Column(db.String, nullable=False)
    expired_date = db.Column(db.DateTime, nullable=True)
    is_working = db.Column(db.Boolean, nullable=False)

    def __init__(self, full_link, short_link):
        self.full_link = full_link
        self.short_link = short_link
        self.expired_date = datetime.now() + timedelta(hours=1)
        self.is_working = True
    
    def __repr__(self):
        return 'full {}, short{}, expired{}, working{}'.format(self.full_link, self.short_link, self.expired_date.strftime("%Y-%m-%d %H:%M:%S"), self.is_working)
    
    def json(self):
        if isinstance(self.expired_date, datetime):
            return {'full_link': self.full_link, 'short_link': self.short_link, 'expired': self.expired_date.strftime("%Y-%m-%d %H:%M:%S"), 'working': self.is_working}
        else:
            return {'full_link': self.full_link, 'short_link': self.short_link, 'expired': None, 'working': self.is_working}
            

    @classmethod    
    def find_by_fullLink(cls, site_name):
        return SiteModel.query.filter_by(full_link=site_name).first()

    @classmethod
    def return_link(cls, shortcut):
        return SiteModel.query.filter_by(short_link=shortcut).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def check_dates(self):
        for item in SiteModel.query.all():
            if datetime.now() > item.expired_date:
                item.is_working = False
        db.session.commit()