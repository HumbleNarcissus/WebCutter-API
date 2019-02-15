from project.tests.base import BaseTestCase
from project.resources.utils import create_shortcut

class TestUtils(BaseTestCase):

    def test_create_shortcut(self):
        """Ensure that shortcut is created and is 6 characters long"""

        self.assertEqual(6, len(create_shortcut()))
        self.assertTrue(isinstance(create_shortcut(), str))
