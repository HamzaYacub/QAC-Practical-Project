import unittest

from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Discounts
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_SFIA2_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        vehicle1 = Discounts(
            vehicle_type = 'Honda', 
            paintjob_type = 'Silver', 
            discount_percent = 38
            )

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

class TestRepr(TestBase):

    def test_discount_repr(self):
        test1 = Discounts()
        assert test1 == 'Honda'