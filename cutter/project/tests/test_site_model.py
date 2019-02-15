from datetime import datetime

from project.tests.base import BaseTestCase
from project.tests.utils import add_site, add_user
from project.resources.SiteModel import SiteModel
from project.resources.utils import create_shortcut


class TestSiteModel(BaseTestCase):

    def test_add_site(self):
        user = add_user('mac', 'mac@mac.pl', '1234qwer')
        site = add_site('google.com', user_id=user.id)
        self.assertTrue(site.id)
        self.assertTrue(site.full_link, 'google.com')
        self.assertTrue(site.is_working, True)
        self.assertTrue(site.expired_date)

    def test_find_by_fullLink(self):
        user = add_user('mac', 'mac@mac.pl', '1234qwer')
        site = add_site('google.com', user_id=user.id)

        result = SiteModel.find_by_fullLink(site.full_link)
        self.assertEqual(site.full_link, result.full_link)

    def test_to_json(self):
        """
        Ensure that to json works
        """
        user = add_user('mac', 'mac@mac.pl', '1234qwer')
        add_site('google.com', user_id=user.id)
        
        site = SiteModel.query.filter_by(full_link="google.com").first()

        json_site = site.json()

        self.assertEqual(1, json_site['id'])
        self.assertEqual("google.com", json_site['full_link'])
        self.assertEqual(6, len(json_site['short_link']))
        self.assertEqual(True, json_site['working'])
        self.assertTrue(isinstance(datetime.strptime(json_site["expiry_date"], "%Y-%m-%d %H:%M:%S"), datetime))

    def test_to_json_none(self):
        """
        Ensure that to json return None when no date
        """
        user = add_user('mac', 'mac@mac.pl', '1234qwer')
        add_site('google.com', user_id=user.id)
        
        site = SiteModel.query.filter_by(full_link="google.com").first()
        site.set_date(None)
        json_site = site.json()

        self.assertEqual(1, json_site['id'])
        self.assertEqual("google.com", json_site['full_link'])
        self.assertEqual(6, len(json_site['short_link']))
        self.assertEqual(True, json_site['working'])
        self.assertEqual(None, json_site['expiry_date'])

        