import json
import unittest

from project import db
from project.resources.SiteModel import SiteModel
from project.tests.base import BaseTestCase
from project.tests.utils import add_site, add_user


class TestApi(BaseTestCase):
    """Test api"""

    def test_all_sites(self):
        """Ensure GET all sites works correctly"""
        user = add_user('mac', 'mac@mac.pl', '1234qwer')
        add_site('google.com', user_id=user.id)
        add_site('amazon.com', user_id=user.id)
        with self.client:
            resp_login = self.client.post(
                '/login',
                data=json.dumps({
                    'username': 'mac',
                    'password': '1234qwer'
                }),
                content_type='application/json'
            )
            token = json.loads(resp_login.data.decode())['auth_token']
            response = self.client.get(
                '/sites',
                content_type='application/json',
                headers={'Authorization': f'Bearer {token}'}
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['sites']), 2)
            self.assertIn('google.com', data['sites'][0]['full_link'])
            self.assertIn('amazon.com', data['sites'][1]['full_link'])
            self.assertIsNotNone(data['sites'][0]['short_link'])
            self.assertIsNotNone(data['sites'][1]['short_link'])

    def test_single_site(self):
        user = add_user('mac', 'mac@mac.pl', '1234qwer')
        add_site('google.com', user_id=user.id)
        with self.client:
            resp_login = self.client.post(
                '/login',
                data=json.dumps({
                    'username': 'mac',
                    'password': '1234qwer'
                }),
                content_type='application/json'
            )
            token = json.loads(resp_login.data.decode())['auth_token']

            response = self.client.get(
                '/sites/google.com',
                content_type='application/json',
                headers={'Authorization': f'Bearer {token}'}
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data), 1)
            self.assertIn('google.com', data['site']['full_link'])
            self.assertIsNotNone(data['site']['short_link'])
