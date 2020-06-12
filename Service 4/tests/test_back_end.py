from flask import url_for
from flask_testing import TestCase
from application import app, db, routes
from application.models import Discounts
from os import getenv
import unittest


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


    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestRepr(TestBase):

    def test_discount_repr(self):
        test1 = Discounts()
        assert test1 == 'Honda'

class TestData(TestBase):

    def test_Mercedes_and_Paintjobs(self):
        assert routes.discount('Black', 'Mercedes', False) == "Congratulations!!! You have unlocked a Black Mercedes which has won you a discount of: 6% off!!"
        assert routes.discount('White', 'Mercedes', False) == "Congratulations!!! You have unlocked a White Mercedes which has won you a discount of: 8% off!!"
        assert routes.discount('Grey', 'Mercedes', False) == "Congratulations!!! You have unlocked a Grey Mercedes which has won you a discount of: 10% off!!"
        assert routes.discount('Blue', 'Mercedes', False) == "Congratulations!!! You have unlocked a Blue Mercedes which has won you a discount of: 12% off!!"
        assert routes.discount('Red', 'Mercedes', False) == "Congratulations!!! You have unlocked a Red Mercedes which has won you a discount of: 14% off!!"
        assert routes.discount('Yellow', 'Mercedes', False) == "Congratulations!!! You have unlocked a Yellow Mercedes which has won you a discount of: 16% off!!"
        assert routes.discount('Silver', 'Mercedes', False) == "Congratulations!!! You have unlocked a Silver Mercedes which has won you a discount of: 18% off!!"
        assert routes.discount('Snakeskin', 'Mercedes', False) == "Congratulations!!! You have unlocked a Snakeskin Mercedes which has won you a discount of: 7% off!!"
        assert routes.discount('Leopard print', 'Mercedes', False) == "Congratulations!!! You have unlocked a Leopard print Mercedes which has won you a discount of: 9% off!!"
        assert routes.discount('Flames', 'Mercedes', False) == "Congratulations!!! You have unlocked a Flames Mercedes which has won you a discount of: 11% off!!"
        assert routes.discount('Two tone', 'Mercedes', False) == "Congratulations!!! You have unlocked a Two tone Mercedes which has won you a discount of: 13% off!!"
        assert routes.discount('Green camo', 'Mercedes', False) == "Congratulations!!! You have unlocked a Green camo Mercedes which has won you a discount of: 15% off!!"
        assert routes.discount('Steampunk', 'Mercedes', False) == "Congratulations!!! You have unlocked a Steampunk Mercedes which has won you a discount of: 17% off!!"

    def test_Audi(self):
        assert routes.discount('Black', 'Audi', False) == "Congratulations!!! You have unlocked a Black Audi which has won you a discount of: 11% off!!"
    
    def test_BMW(self):
        assert routes.discount('Black', 'BMW', False) == "Congratulations!!! You have unlocked a Black BMW which has won you a discount of: 16% off!!"

    def test_Honda(self):
        assert routes.discount('Black', 'Honda', False) == "Congratulations!!! You have unlocked a Black Honda which has won you a discount of: 26% off!!"

    def test_VW(self):
        assert routes.discount('Black', 'Volkswagen', False) == "Congratulations!!! You have unlocked a Black Volkswagen which has won you a discount of: 21% off!!"

    def test_Yamaha(self):
        assert routes.discount('Black', 'Yamaha', False) == "Congratulations!!! You have unlocked a Black Yamaha which has won you a discount of: 8% off!!"

    def test_Kawasaki(self):
        assert routes.discount('Black', 'Kawasaki', False) == "Congratulations!!! You have unlocked a Black Kawasaki which has won you a discount of: 13% off!!"
    
    def test_Ducati(self):
        assert routes.discount('Black', 'Ducati', False) == "Congratulations!!! You have unlocked a Black Ducati which has won you a discount of: 18% off!!"

    def test_Suzuki(self):
        assert routes.discount('Black', 'Suzuki', False) == "Congratulations!!! You have unlocked a Black Suzuki which has won you a discount of: 28% off!!"

    def test_HarleyDavidson(self):
        assert routes.discount('Black', 'Harley Davidson', False) == "Congratulations!!! You have unlocked a Black Harley Davidson which has won you a discount of: 23% off!!"

    def test_superdiscount(self):
        assert routes.discount('Black', 'Mercedes', True) == "Congratulations!!! You have unlocked a Black Mercedes which has won you a super discount of: 8% off!!!!!"
