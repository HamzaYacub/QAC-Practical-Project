from application import app, db
from flask import request, Response
import requests
from random import choice
from application.models import Discounts

@app.route('/', methods=['GET', 'POST'])
def discount():
    
    vehicle = requests.get('http://service_2:5002').text
    paintjob = requests.get('http://service_3:5003').text
    v_discount = 0
    p_discount = 0
    total_discount = 0
    generous = True

    if vehicle == 'Mercedes':
        v_discount = 5
    elif vehicle == 'Audi':
        v_discount = 10
    elif vehicle == 'BMW':
        v_discount = 15
    elif vehicle == 'Volkswagen':
        v_discount = 20
    elif vehicle == 'Honda':
        v_discount = 25
    elif vehicle == 'Yamaha':
        v_discount = 7
    elif vehicle == 'Kawasaki':
        v_discount = 12
    elif vehicle == 'Ducati':
        v_discount = 17
    elif vehicle == 'Harley Davidson':
        v_discount = 22
    elif vehicle == 'Suzuki':
        v_discount = 27
    else:
        v_discount = 0

    if paintjob == 'Black':
        p_discount = 1
    elif paintjob == 'White':
        p_discount = 3
    elif paintjob == 'Grey':
        p_discount = 5
    elif paintjob == 'Blue':
        p_discount = 7
    elif paintjob == 'Red':
        p_discount = 9
    elif paintjob == 'Yellow':
        p_discount = 11
    elif paintjob == 'Silver':
        p_discount = 13
    elif paintjob == 'Snakeskin':
        p_discount = 2
    elif paintjob == 'Leopard print':
        p_discount = 4
    elif paintjob == 'Flames':
        p_discount = 6
    elif paintjob == 'Two tone':
        p_discount = 8
    elif paintjob == 'Green camo':
        p_discount = 10
    elif paintjob == 'Steampunk':
        p_discount = 12
    else:
        p_discount = 0

    if not generous:

        total_discount = v_discount + p_discount

        discount_amount = Discounts(
            vehicle_type = vehicle,
            paintjob_type = paintjob,
            discount_percent = total_discount
        )

        db.session.add(discount_amount)
        db.session.commit()

        return "Congratulations!!! You have unlocked a " + paintjob + " " + vehicle + " which has won you a discount of: " + str(total_discount) + "% off!!"
    elif generous:
        
        total_discount = v_discount + p_discount
        total_discount = total_discount * 1.25

        discount_amount = Discounts(
            vehicle_type = vehicle,
            paintjob_type = paintjob,
            discount_percent = round(total_discount)
        )

        db.session.add(discount_amount)
        db.session.commit()

        return "Congratulations!!! You have unlocked a " + paintjob + " " + vehicle + " which has won you a super discount of: " + str(round(total_discount)) + "% off!!!!!"