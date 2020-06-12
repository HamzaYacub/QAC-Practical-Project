from application import app, db
from flask import render_template, redirect, url_for, request
from application.models import Discounts
import requests

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    discountsData = Discounts.query.distinct()
    discount_response = requests.get('http://service_4:5004').text
    
    return render_template('home.html', title='Home', discounts=discountsData, discount_res=discount_response)