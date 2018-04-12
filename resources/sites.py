from flask_restful import Resource, reqparse, abort
from models.SiteModel import SiteModel
from sqlalchemy import update
import string
import random

class Sites(Resource):
    '''
    Sites resources with all posted sites
    '''

    #define request parser
    parser = reqparse.RequestParser()

    #define required argument
    parser.add_argument('site',
        type=str,
        required=True,
        help="This field cannot be blank!"
    )

    def get(self):
        '''
        GET /sites - getting all sites
        '''
        SiteModel.check_dates(self)
        #return all sites as json
        return {'sites': [x.json() for x in SiteModel.query.all()]}, 200

    def post(self):
        '''
        POST /sites - post new site
        '''

        args = Sites.parser.parse_args()

        #check if site exists
        result = SiteModel.find_by_fullLink(args['site'])

        if result != None:
            return "Site already exists", 400

        sites = SiteModel(args['site'], Sites.create_shortcut())
        sites.save_to_db()

        return 'Created new site', 201
    
    @staticmethod
    def create_shortcut():
        '''
        Generate new random site code
        '''
        return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))    


class Site(Resource):
    '''
    Individual site recources
    '''

    #create request parser
    parser = reqparse.RequestParser()
    parser.add_argument('site',
        type=str,
        required=True,
        help="This field cannot be blank!"
    )

    def get(self, site):
        '''
        Get /site/<site_name>
        '''
        return {'site': SiteModel.find_by_fullLink(site).json()}, 200  

    def put(self, site):
        '''
        Edit or enter new site
        '''
        args = Site.parser.parse_args()

        #check if site exists
        result = SiteModel.find_by_fullLink(args['site'])
        if result != None:
            return "Site already exists", 400

        item = SiteModel.find_by_fullLink(site)
        
        #edit existing item or enter new one
        if item is None:
            item = SiteModel(site, Sites.create_shortcut())
        else:
            item.full_link = args['site']
        
        item.save_to_db()

        return "", 200

    def delete(self, site):
        '''
        DELETE /site/<site_name>
        '''
        args = Site.parser.parse_args()
        item = SiteModel.find_by_fullLink(site)

        if item is None:
            return "Entered site dose not exist", 404
        else:
            item.delete_from_db()
            return "Item deleted", 201
        
