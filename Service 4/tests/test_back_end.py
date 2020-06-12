from flask import url_for
from flask_testing import TestCase
from application import app, db, routes
from application.models import Discounts
from os import getenv
from unittest.mock import patch
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

    def test_Mercedes(self):
        assert routes.discount() == "Congratulations!!! You have unlocked a Black Mercedes which has won you a discount of: 6% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a White Mercedes which has won you a discount of: 8% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Grey Mercedes which has won you a discount of: 10% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Blue Mercedes which has won you a discount of: 12% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Red Mercedes which has won you a discount of: 14% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Yellow Mercedes which has won you a discount of: 16% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Silver Mercedes which has won you a discount of: 18% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Snakeskin Mercedes which has won you a discount of: 7% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Leopard print Mercedes which has won you a discount of: 9% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Flames Mercedes which has won you a discount of: 11% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Two tone Mercedes which has won you a discount of: 13% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Green camo Mercedes which has won you a discount of: 15% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Steampunk Mercedes which has won you a discount of: 17% off!!"

    def test_Audi(self):
        assert routes.discount() == "Congratulations!!! You have unlocked a Black Audi which has won you a discount of: 11% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a White Audi which has won you a discount of: 13% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Grey Audi which has won you a discount of: 15% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Blue Audi which has won you a discount of: 17% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Red Audi which has won you a discount of: 19% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Yellow Audi which has won you a discount of: 21% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Silver Audi which has won you a discount of: 23% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Snakeskin Audi which has won you a discount of: 12% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Leopard print Audi which has won you a discount of: 14% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Flames Audi which has won you a discount of: 16% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Two tone Audi which has won you a discount of: 18% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Green camo Audi which has won you a discount of: 20% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Steampunk Audi which has won you a discount of: 22% off!!"
    
    def test_BMW(self):
        assert routes.discount() == "Congratulations!!! You have unlocked a Black BMW which has won you a discount of: 16% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a White BMW which has won you a discount of: 18% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Grey BMW which has won you a discount of: 20% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Blue BMW which has won you a discount of: 22% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Red BMW which has won you a discount of: 24% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Yellow BMW which has won you a discount of: 26% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Silver BMW which has won you a discount of: 28% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Snakeskin BMW which has won you a discount of: 17% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Leopard print BMW which has won you a discount of: 19% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Flames BMW which has won you a discount of: 21% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Two tone BMW which has won you a discount of: 23% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Green camo BMW which has won you a discount of: 25% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Steampunk BMW which has won you a discount of: 27% off!!"

    def test_Honda(self):
        assert routes.discount() == "Congratulations!!! You have unlocked a Black Honda which has won you a discount of: 26% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a White Honda which has won you a discount of: 28% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Grey Honda which has won you a discount of: 30% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Blue Honda which has won you a discount of: 32% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Red Honda which has won you a discount of: 34% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Yellow Honda which has won you a discount of: 36% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Silver Honda which has won you a discount of: 38% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Snakeskin Honda which has won you a discount of: 27% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Leopard print Honda which has won you a discount of: 29% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Flames Honda which has won you a discount of: 31% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Two tone Honda which has won you a discount of: 33% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Green camo Honda which has won you a discount of: 35% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Steampunk Honda which has won you a discount of: 37% off!!"

    def test_VW(self):
        assert routes.discount() == "Congratulations!!! You have unlocked a Black Volkswagen which has won you a discount of: 21% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a White Volkswagen which has won you a discount of: 23% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Grey Volkswagen which has won you a discount of: 25% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Blue Volkswagen which has won you a discount of: 27% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Red Volkswagen which has won you a discount of: 29% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Yellow Volkswagen which has won you a discount of: 31% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Silver Volkswagen which has won you a discount of: 33% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Snakeskin Volkswagen which has won you a discount of: 22% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Leopard print Volkswagen which has won you a discount of: 24% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Flames Volkswagen which has won you a discount of: 26% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Two tone Volkswagen which has won you a discount of: 28% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Green camo Volkswagen which has won you a discount of: 30% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Steampunk Volkswagen which has won you a discount of: 32% off!!"

    def test_Yamaha(self):
        assert routes.discount() == "Congratulations!!! You have unlocked a Black Yamaha which has won you a discount of: 8% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a White Yamaha which has won you a discount of: 10% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Grey Yamaha which has won you a discount of: 12% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Blue Yamaha which has won you a discount of: 14% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Red Yamaha which has won you a discount of: 16% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Yellow Yamaha which has won you a discount of: 18% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Silver Yamaha which has won you a discount of: 20% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Snakeskin Yamaha which has won you a discount of: 9% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Leopard print Yamaha which has won you a discount of:11% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Flames Yamaha which has won you a discount of: 13% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Two tone Yamaha which has won you a discount of: 15% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Green camo Yamaha which has won you a discount of: 17% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Steampunk Yamaha which has won you a discount of: 19% off!!"

    def test_Kawasaki(self):
        assert routes.discount() == "Congratulations!!! You have unlocked a Black Kawasaki which has won you a discount of: 13% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a White Kawasaki which has won you a discount of: 15% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Grey Kawasaki which has won you a discount of: 17% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Blue Kawasaki which has won you a discount of: 19% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Red Kawasaki which has won you a discount of: 21% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Yellow Kawasaki which has won you a discount of: 23% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Silver Kawasaki which has won you a discount of: 25% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Snakeskin Kawasaki which has won you a discount of: 14% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Leopard print Kawasaki which has won you a discount of: 16% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Flames Kawasaki which has won you a discount of: 18% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Two tone Kawasaki which has won you a discount of: 20% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Green camo Kawasaki which has won you a discount of: 22% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Steampunk Kawasaki which has won you a discount of: 24% off!!"
    
    def test_Ducati(self):
        assert routes.discount() == "Congratulations!!! You have unlocked a Black Ducati which has won you a discount of: 18% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a White Ducati which has won you a discount of: 20% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Grey Ducati which has won you a discount of: 22% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Blue Ducati which has won you a discount of: 24% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Red Ducati which has won you a discount of: 26% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Yellow Ducati which has won you a discount of: 28% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Silver Ducati which has won you a discount of: 30% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Snakeskin Ducati which has won you a discount of: 19% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Leopard print Ducati which has won you a discount of: 21% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Flames Ducati which has won you a discount of: 23% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Two tone Ducati which has won you a discount of: 25% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Green camo Ducati which has won you a discount of: 27% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Steampunk Ducati which has won you a discount of: 29% off!!"

    def test_Suzuki(self):
        assert routes.discount() == "Congratulations!!! You have unlocked a Black Suzuki which has won you a discount of: 28% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a White Suzuki which has won you a discount of: 30% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Grey Suzuki which has won you a discount of: 32% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Blue Suzuki which has won you a discount of: 34% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Red Suzuki which has won you a discount of: 36% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Yellow Suzuki which has won you a discount of: 38% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Silver Suzuki which has won you a discount of: 40% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Snakeskin Suzuki which has won you a discount of: 29% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Leopard print Suzuki which has won you a discount of: 31% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Flames Suzuki which has won you a discount of: 33% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Two tone Suzuki which has won you a discount of: 35% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Green camo Suzuki which has won you a discount of: 37% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Steampunk Suzuki which has won you a discount of: 39% off!!"

    def test_HarleyDavidson(self):
        assert routes.discount() == "Congratulations!!! You have unlocked a Black Harley Davidson which has won you a discount of: 23% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a White Harley Davidson which has won you a discount of: 25% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Grey Harley Davidson which has won you a discount of: 27% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Blue Harley Davidson which has won you a discount of: 29% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Red Harley Davidson which has won you a discount of: 31% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Yellow Harley Davidson which has won you a discount of: 33% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Silver Harley Davidson which has won you a discount of: 35% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Snakeskin Harley Davidson which has won you a discount of: 24% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Leopard print Harley Davidson which has won you a discount of: 26% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Flames Harley Davidson which has won you a discount of: 28% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Two tone Harley Davidson which has won you a discount of: 30% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Green camo Harley Davidson which has won you a discount of: 32% off!!"
        assert routes.discount() == "Congratulations!!! You have unlocked a Steampunk Harley Davidson which has won you a discount of: 34% off!!"