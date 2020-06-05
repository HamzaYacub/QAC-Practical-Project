from application import app
from flask import request, Response
from random import choice
import csv

@app.route('/vehicle/type', methods=['GET'])
def vehicle_type():

    with open('vehicle.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['car1', 'car2', 'car3'])
        csv_writer.writerow(['motorbike1', 'motorbike2', 'motorbike3'])

    with open('vehicle.csv', newline='') as f:
        csv_reader = csv.reader(f)
        vehicles = list(csv_reader)
        cars = vehicles[0]
        motorbikes = vehicles[1]

    random_vehicle = choice(vehicles)
    #random_car = choice(cars)
    #random_bike = choice(motorbikes)

    return random_vehicle