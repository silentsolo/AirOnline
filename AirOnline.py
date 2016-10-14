import json
from flask import Flask, render_template, request
from acess_data import distrit_data
from flask import jsonify
app = Flask(__name__)


@app.route('/')
def index():
    # return 'Hello World!'
    return render_template('index.html')

@app.route('/about')
def aboutme():
    # return 'Hello World!'
    return render_template('about.html')

@app.route('/regions')
def regions_map():
    # data = distrit_data('geo')
    # print data
    return render_template('regions_map.html')

@app.route('/Getdata', methods=['POST', 'GET'])
def get_data():
    req = json.loads(request.data)
    kind = req.get('kind', 'geo')
    # print kind
    # print jsonify(distrit_data(kind))
    return json.dumps(distrit_data(kind))

@app.route('/evregion', methods=['GET'])
def region_index():
    return render_template('regions_index.html')

@app.route('/region/<regioname>')
def region_one(regioname):
    return render_template('city_map.html', regioname=regioname)

if __name__ == '__main__':
    app.run()
