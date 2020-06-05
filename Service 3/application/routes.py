from application import app
from flask import request, Response
from random import choice
import csv

@app.route('/paintjobs/type', methods=['GET'])
def vehicle_type():

    with open('paintjobs.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Black', 'White', 'Grey', 'Blue', 'Red', 'Yellow', 'Silver'])
        csv_writer.writerow(['Snakeskin', 'Leopard print', 'Flames', 'Two tone', 'Green Camo', 'Steampunk'])

    with open('paintjobs.csv', newline='') as f:
        csv_reader = csv.reader(f)
        paintjobs = list(csv_reader)
        colours = paintjobs[0]
        designs = paintjobs[1]

    random_paintjob = choice(paintjobs)
    random_colour = choice(colours)
    random_design = choice(designs)

    return random_colour