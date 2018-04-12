from flask import redirect
from flask_restful import Resource, reqparse, abort
from models.SiteModel import SiteModel
from sqlalchemy import update
import string
import random

class Shortcut(Resource):

    def get(self, short_link):
        '''
        GET /<shortcut>
        '''
        result = SiteModel.return_link(short_link)

        if result == None:
            return "Site does not exist", 404
        #check if link has expired
        elif result.is_working == False:
            return "Link has expired", 405
        else:
            #redirect to site behind short link
            return redirect("http://" + result.full_link, code=302)
