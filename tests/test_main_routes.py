import unittest
from flask import url_for
from app import create_app


class MainRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    def test_index(self):
        self.assertTrue(self.client.get(url_for('main.index')))

    def test_testing(self):
        self.assertTrue(self.client.get(url_for('testing.testing')))

    def test_products(self):
        self.assertTrue(self.client.get(url_for('main.products')))

    def test_contact_us(self):
        self.assertTrue(self.client.get(url_for('main.contact')))

    def test_register(self):
        self.assertTrue(self.client.get(url_for('auth.register')))

    def test_login(self):
        self.assertTrue(self.client.get(url_for('auth.login')))

    def test_logout(self):
        self.assertTrue(self.client.get(url_for('auth.logout')))
