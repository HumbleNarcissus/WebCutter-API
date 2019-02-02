import json
from project.tests.base import BaseTestCase
from project.tests.utils import add_user, add_site


class TestShortcut(BaseTestCase):

    def test_site_not_exist(self):
        """Ensure that shortcut for not existing site is not working"""
        add_user('mac', 'mac@mac.pl', '1234qwer')
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
                f'/asd123e',
                content_type='application/json',
                headers={'Authorization': f'Bearer {token}'}
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertEqual(data['message'], 'Site does not exist')

    def test_expiry_link(self):
        """Ensure that expiry site is not redirecting to another site"""
        user = add_user('mac', 'mac@mac.pl', '1234qwer')
        site = add_site('google.com', user_id=user.id)
        site.is_working = False
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
                f'/{site.short_link}',
                content_type='application/json',
                headers={'Authorization': f'Bearer {token}'}
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 405)
            self.assertEqual(data['message'], 'Link has expired')

    def test_shortcut_redirect(self):
        """Ensure that short link redirect to another site"""
        user = add_user('mac', 'mac@mac.pl', '1234qwer')
        site = add_site('google.com', user_id=user.id)
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
                f'/{site.short_link}',
                content_type='application/json',
                headers={'Authorization': f'Bearer {token}'}
            )
            self.assertEqual(response.status_code, 302)
