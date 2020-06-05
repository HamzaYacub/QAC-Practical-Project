from application import app
from flask import request, Response
from random import choice
import csv

@app.route('/paintjobs/type', methods=['GET'])
def vehicle_type():

    with open('paintjobs.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['red', 'blue', 'yellow'])
        csv_writer.writerow(['snakeskin', 'leopard print', 'flames'])

    with open('paintjobs.csv', newline='') as f:
        csv_reader = csv.reader(f)
        paintjobs = list(csv_reader)
        colours = paintjobs[0]
        designs = paintjobs[1]

    random_paintjob = choice(paintjobs)
    #random_colour = choice(colours)
    #random_design = choice(designs)

    return random_paintjob