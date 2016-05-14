import unittest
import os


class SystemTestCase(unittest.TestCase):

    def test_mail_username(self):
        self.assertFalse(os.environ.get('MAIL_USERNAME') is None)

    def test_mail_password(self):
        self.assertFalse(os.environ.get('MAIL_PASSWORD') is None)

    def test_secret_key(self):
        self.assertFalse(os.environ.get('SECRET_KEY') is None)

    def test_site_admin(self):
        self.assertFalse(os.environ.get('SITE_ADMIN') is None)



