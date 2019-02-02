from flask_restful import Resource, reqparse
from .SiteModel import SiteModel
from project.resources.utils import authenticate
import string
import random


class Sites(Resource):
    """
    Sites resources with all posted sites
    """
    # define request parser
    parser = reqparse.RequestParser()

    # define required argument
    parser.add_argument(
        'site',
        type=str,
        required=True,
        help="This field cannot be blank!"
    )

    @authenticate
    def get(self, resp):
        """
        GET /sites - getting all sites
        """
        SiteModel.check_dates(self)

        # return all sites as json
        return {'sites': [x.json() for x in SiteModel.query.filter_by(
            user_id=self).all()]}, 200

    @authenticate
    def post(self, resp):
        '''
        POST /sites - post new site
        '''

        args = Sites.parser.parse_args()

        # check if site exists
        result = SiteModel.find_by_fullLink(args['site'])

        if result is not None:
            return "Site already exists", 400

        # create unique site's code
        new_code = Sites.create_shortcut()

        sites = SiteModel(args['site'], new_code, self)
        sites.save_to_db()

        return 'Created new site', 201

    @staticmethod
    def create_shortcut():
        """
        Generate new random site code
        """
        new_code = ''.join(random.choices(
            string.ascii_uppercase + string.ascii_lowercase + string.digits,
            k=6)
        )

        for item in SiteModel.query.all():
            if item.short_link == new_code:
                return Sites.create_shortcut()

        return new_code


class Site(Resource):
    """
    Individual site recources
    """

    # create request parser
    parser = reqparse.RequestParser()
    parser.add_argument(
        'site',
        type=str,
        required=True,
        help="This field cannot be blank!"
    )

    @authenticate
    def get(self, resp, site):
        """
        Get /sites/<site_name>
        """
        querySite = SiteModel.find_by_fullLink(site)

        if querySite is None:
            return {"message": "Site does not exist"}, 404
        return {'site': querySite.json()}, 200

    @authenticate
    def put(self, resp, site):
        """
        Edit or enter new site
        """
        args = Site.parser.parse_args()

        # check if new site exists
        result = SiteModel.find_by_fullLink(args['site'])
        if result is not None:
            return "Site already exists", 409

        item = SiteModel.find_by_fullLink(site)

        # edit existing item or enter new one
        if item is None:
            item = SiteModel(site, Sites.create_shortcut(), self)
        else:
            item.full_link = args['site']

        item.save_to_db()

        return {"message": "Item edited"}, 200

    @authenticate
    def delete(self, resp, site):
        """
        DELETE /sites/<site_name>
        """
        item = SiteModel.find_by_fullLink(site)

        if item is None:
            return "Entered site dose not exist", 404
        else:
            item.delete_from_db()
            return {"message": "Item deleted"}, 200
