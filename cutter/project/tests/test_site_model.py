import json
import unittest

from project import db
from project.resources.SiteModel import SiteModel
from project.tests.base import BaseTestCase
from project.tests.utils import add_site

class TestSiteModel(BaseTestCase):
    
    def test_add_site(self):
        site = add_site('google.com')
        self.assertTrue(site.id)
        self.assertTrue(site.full_link, 'google.com')
        self.assertTrue(site.is_working, True)
        self.assertTrue(site.expired_date)

