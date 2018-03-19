from flask_restful import Resource, reqparse, abort
from models.SiteModel import SiteModel
from sqlalchemy import update
import string
import random

class Sites(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('site',
        type=str,
        required=True,
        help="This field cannot be blank!"
    )

    def get(self):
        SiteModel.check_dates(self)
        return {'sites': [x.json() for x in SiteModel.query.all()]}, 200

    def post(self):
        args = Sites.parser.parse_args()
        sites = SiteModel(args['site'], Sites.create_shortcut())
        sites.save_to_db()
        return '', 201
    
    @staticmethod
    def create_shortcut():
        return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))    


class Site(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('site',
        type=str,
        required=True,
        help="This field cannot be blank!"
    )
    def get(self, site):
        return {'site': SiteModel.find_by_fullLink(site).json()}, 200  

    def put(self, site):
        args = Site.parser.parse_args()
        item = SiteModel.find_by_fullLink(site)
        
        if item is None:
            item = SiteModel(site, Sites.create_shortcut())
        else:
            item.full_link = args['site']
        
        item.save_to_db()

        return "", 200

    def delete(self, site):
        pass
