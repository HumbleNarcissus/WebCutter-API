from flask import redirect
from flask_restful import Resource, reqparse, abort
from models.SiteModel import SiteModel
from sqlalchemy import update
import string
import random

class Shortcut(Resource):

    def get(self, short_link):
        
        result = SiteModel.return_link(short_link)

        print("Result: {}".format(result.is_working))

        if result == None:
            return "Site does not exist", 404
        elif result.is_working == False:
            return "Link has expired", 405
        else:
            return redirect("http://" + result.full_link, code=302)
