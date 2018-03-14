from flask import redirect
from flask_restful import Resource, reqparse, abort
from models.SiteModel import SiteModel
from sqlalchemy import update
from db import db
import string
import random

class Shortcut(Resource):

    def get(self, short_link):
        
        result = SiteModel.return_link(short_link)

        if result == None:
            return "", 404
        else:
            return redirect("http://" + result.full_link, code=302)
