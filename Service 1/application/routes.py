from application import app, db
from flask import render_template, redirect, url_for, request
from application.models import Discounts
from requests import get

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    discountsData = Discounts.query.all()
    
    return render_template('home.html', title='Home', discount=discountsData)

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    discount = requests.get('http://service_4:5004').text

    return render_template('generate.html', title='Generate discount', discount_response=discount)