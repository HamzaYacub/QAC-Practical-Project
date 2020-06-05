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
        p_list = list(csv_reader)
        colours = p_list[0]
        designs = p_list[1]
        paintjobs = colours + designs

    random_paintjob = choice(paintjobs)
    random_colour = choice(colours)
    random_design = choice(designs)

    return random_paintjob