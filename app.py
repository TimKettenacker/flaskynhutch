from flask import Flask
from flask import render_template
from flask import request, jsonify
import csv

app = Flask(__name__)

@app.route('/')
def root():
    with open('example_data.csv', 'r') as f:
        # init dataset
        data = [dict(item) for item in csv.DictReader(f)]

        fieldnames = [key for key in data[0].keys()]

        return render_template('home.html', data=data, fieldnames=fieldnames, len=len)

@app.route('/api/v1/data', methods=['GET'])
def api_all():
    with open('example_data.csv', 'r') as f:
        # init dataset
        data = [dict(item) for item in csv.DictReader(f)]

        fieldnames = [key for key in data[0].keys()]

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)