"""
Webcutter Api - RESTful aplication working like the Bitly. If you post some site eg. "google.com",
Webcutter will generate random short code for you to access that page.

Author: Maciej Tarach
"""

# imports
import os
from flask import Flask, render_template
from flask_restful import Api
import flask_cors
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(script_info=None):
    """
    Creating and configurating app
    """
    app = Flask(__name__)

    # enable cors
    flask_cors.CORS(app)

    # config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    api = Api(app)

    # init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # init resources routes
    from project.resources.sites import Sites, Site
    from project.resources.shortcut import Shortcut
    api.add_resource(Sites, '/sites')
    api.add_resource(Site, '/sites/<site>')
    api.add_resource(Shortcut, '/<short_link>')

    @app.route("/")
    def index():
        return render_template("index.html")

    # import sys
    # print(app.config, file=sys.stderr)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
