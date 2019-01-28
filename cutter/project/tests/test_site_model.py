import json
import unittest

from project import db
from project.resources.SiteModel import SiteModel
from project.tests.base import BaseTestCase
from project.tests.utils import add_site, add_user


class TestSiteModel(BaseTestCase):

    def test_add_site(self):
        user = add_user('mac', 'mac@mac.pl', '1234qwer')
        site = add_site('google.com', user_id=user.id)
        self.assertTrue(site.id)
        self.assertTrue(site.full_link, 'google.com')
        self.assertTrue(site.is_working, True)
        self.assertTrue(site.expired_date)
