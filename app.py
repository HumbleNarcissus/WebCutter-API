"""
Imports
"""
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from resources.sites import Sites, Site
from resources.shortcut import Shortcut
from models.SiteModel import SiteModel

app = Flask(__name__)

#config
app.config.from_object('configs.DevelopmentConfig')

api = Api(app)


api.add_resource(Sites, '/sites')
api.add_resource(Site, '/site/<site>')
api.add_resource(Shortcut, '/<short_link>')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run()

