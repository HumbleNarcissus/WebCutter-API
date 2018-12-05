import json
import unittest

from project import db
from project.resources.SiteModel import SiteModel
from project.tests.base import BaseTestCase
from project.tests.utils import add_site

class TestApi(BaseTestCase):
    """Test api"""

    def test_all_sites(self):
        """Ensure GET all sites works correctly"""
        add_site('google.com')
        add_site('amazon.com')
        with self.client:
            response = self.client.get('/sites')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['sites']), 2)
            self.assertIn('google.com', data['sites'][0]['full_link'])
            self.assertIn('amazon.com', data['sites'][1]['full_link'])
            self.assertIsNotNone(data['sites'][0]['short_link'])
            self.assertIsNotNone(data['sites'][1]['short_link'])
    
    def test_single_site(self):
        add_site('google.com')
        with self.client:
            response = self.client.get('/sites/google.com')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data), 1)
            self.assertIn('google.com', data['site']['full_link'])
            self.assertIsNotNone(data['site']['short_link'])





