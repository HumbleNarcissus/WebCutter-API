'''
Webcutter Api - RESTful aplication working like the Bitly. If you post some site eg. "google.com",
Webcutter will generate random short code for you to access that page.

Author: Maciej Tarach 
'''


#imports
from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from resources.sites import Sites, Site
from resources.shortcut import Shortcut
from models.SiteModel import SiteModel
from flask_cors import CORS

def create_app(config):
    '''
    Creating and configurating app
    '''
    app = Flask(__name__)

    #enable cors
    CORS(app)
    
    #config
    app.config.from_object(config)
    api = Api(app)

    #init recources routes
    api.add_resource(Sites, '/sites')
    api.add_resource(Site, '/site/<site>')
    api.add_resource(Shortcut, '/<short_link>')

    @app.route("/")
    def index():
        return render_template("index.html")

    from db import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)

    return app

if __name__ == '__main__':
    import os
    app = create_app(os.environ['APP_SETTINGS'])
    app.run()