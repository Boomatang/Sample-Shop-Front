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

    def test_products(self):
        self.assertTrue(self.client.get(url_for('main.products')))
