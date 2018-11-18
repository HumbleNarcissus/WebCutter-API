from flask import redirect
from flask_restful import Resource
from .SiteModel import SiteModel


class Shortcut(Resource):

    def get(self, short_link):
        """
        GET /<shortcut>
        """
        result = SiteModel.return_link(short_link)

        if result is None:
            return "Site does not exist", 404
        # check if link has expired
        elif not result.is_working:
            return "Link has expired", 405
        else:
            # redirect to site behind short link
            return redirect("http://" + result.full_link, code=302)
