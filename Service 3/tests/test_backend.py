import unittest
from flask import url_for
from flask_testing import TestCase
from application import app, routes
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        return app

class TestViews(TestBase):

    def test_home_view(self):
        response = self.client.get(url_for('paintjob_type'))
        self.assertEqual(response.status_code, 200)
