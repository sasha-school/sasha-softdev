import csv
import random
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "HOMEPAGE nav to /wdywtbwygp"

@app.route("/wdywtbwygp") 
def occupations():
    occupations_table = []
    with open('data/occupations.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            item = [(row[0].strip()),(row[1].strip())]
            occupations_table.append(item)
            
    occupations = {}
    with open('data/occupations.csv', mode='r') as file:
        csv_reader = csv.reader(file)  # use csv.reader to handle quoted lines bc they exist in our file
        next(csv_reader)  # skip header
        for row in csv_reader:
            if len(row) == 2:  # check if we have exactly two elements (occupation, percentage)
                occupation = row[0].strip()
                percentage = float(row[1].strip())
                occupations[occupation] = percentage
    del occupations['Total']
    occupation_list = list(occupations.keys())
    weights = list(occupations.values())
    selected_occupation = random.choices(occupation_list, weights=weights, k=1)
    return render_template('tablified.html', randomly_selected=selected_occupation[0])

if __name__ == "__main__":
    app.debug = True
    app.run()