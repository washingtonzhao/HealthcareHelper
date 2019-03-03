from flask import Flask, request
from flask import render_template
from flask import jsonify, json
from uber_data_helper import getData

from mapsGet import getCoords

app = Flask(__name__)
@app.route('/data')


def data():
	address = request.args.get('address')

	coords = getCoords(address)

	out = []

	uberData = getData(coords[0], coords[1])
	
	out.append(uberData)
	jsonOut = json.dumps(out)

	return jsonify(jsonOut)


if __name__ == '__main__':
    app.run()



