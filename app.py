"""
Imports
"""
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from resources.sites import Sites, Site
from resources.shortcut import Shortcut
from models.SiteModel import SiteModel
from flask_cors import CORS

def create_app(config):
    app = Flask(__name__)
    CORS(app)
    
    #config
    app.config.from_object(config)
    api = Api(app)

    api.add_resource(Sites, '/sites')
    api.add_resource(Site, '/site/<site>')
    api.add_resource(Shortcut, '/<short_link>')


    from db import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)

    return app

if __name__ == '__main__':
    import os
    app = create_app(os.environ['APP_SETTINGS'])
    app.run()