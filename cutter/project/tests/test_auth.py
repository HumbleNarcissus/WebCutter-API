import json
from project.tests.base import BaseTestCase
from project.tests.utils import add_user


class TestAuth(BaseTestCase):

    def test_login(self):
        """Ensure that user can log in"""
        add_user('mac', 'mac@mac.pl', '1234qwer')
        with self.client:
            response = self.client.post(
                '/login',
                data=json.dumps({
                    'username': 'mac',
                    'password': '1234qwer'
                }),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['status'], 'success')
            self.assertEqual(data['message'], 'Successfully logged in')
            self.assertIsNotNone(data['auth_token'])

    def test_user_registration_duplicate_email(self):
        add_user('mac', 'mac@mac.pl', '1234qwer')
        with self.client:
            response = self.client.post(
                '/register',
                data=json.dumps({
                    'username': 'mac',
                    'email': 'mac@mac.pl',
                    'password': '1234qwer'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('That user already exists.', data['message'])

    def test_user_registration_duplicate_username(self):
        add_user('mac', 'mac@mac.pl', '1234qwer')
        with self.client:
            response = self.client.post(
                '/register',
                data=json.dumps({
                    'username': 'mac',
                    'email': 'mac@mac.pl',
                    'password': '1234qwer'
                }),
                content_type='application/json',
            )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertIn('That user already exists.', data['message'])
