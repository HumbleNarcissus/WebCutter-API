from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from .SiteModel import SiteModel
from .utils import create_shortcut


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

    @classmethod
    @jwt_required
    def get(cls):
        """
        GET /sites - getting all sites
        """
        SiteModel.check_dates()
        _user_id = get_jwt_identity()

        # return all sites as json
        return {'sites': [x.json() for x in SiteModel.query.filter_by(
            user_id=_user_id).all()]}, 200

    @classmethod
    @jwt_required
    def post(cls):
        '''
        POST /sites - post new site
        '''

        args = Sites.parser.parse_args()
        _user_id = get_jwt_identity()

        # check if site exists
        result = SiteModel.query.filter_by(
            user_id=_user_id,
            full_link=args['site']
        ).first()

        if result is not None:
            return {"message": "Site already exists"}, 409

        if not args['site']:
            return {"message": "Cannot add an empty site"}, 409

        # create unique site's code
        new_code = create_shortcut()

        sites = SiteModel(args['site'], new_code, _user_id)
        sites.save_to_db()

        return {"message": "Created new site"}, 201


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

    @classmethod
    @jwt_required
    def get(cls, site):
        """
        Get /sites/<site_name>
        """
        querySite = SiteModel.find_by_fullLink(site)

        if querySite is None:
            return {"message": "Site does not exist"}, 404
        return {'site': querySite.json()}, 200

    @classmethod
    @jwt_required
    def put(cls, site):
        """
        Edit or enter new site
        """
        args = Site.parser.parse_args()
        _user_id = get_jwt_identity()

        # check if new site exists
        result = SiteModel.find_by_fullLink(args['site'])
        if result is not None:
            return {"message": "Site already exists"}, 409

        if not args['site']:
            return {"message": "Cannot add an empty site"}, 409

        item = SiteModel.find_by_fullLink(site)

        # edit existing item or enter new one
        if item is None:
            item = SiteModel(site, create_shortcut(), _user_id)
        else:
            item.full_link = args['site']

        item.save_to_db()
        return {"message": "Item edited"}, 200

    @classmethod
    @jwt_required
    def delete(cls, site):
        """
        DELETE /sites/<site_name>
        """
        item = SiteModel.find_by_fullLink(site)

        if item is None:
            return {"message": "Entered site does not exist"}, 404
        else:
            item.delete_from_db()
            return {"message": "Item deleted"}, 200
