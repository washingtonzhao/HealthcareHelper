from flask import Flask, request
from flask import render_template
from flask import jsonify, json
from uber_data_helper import getData
from scraper import scrape

from mapsGet import getCoords



app = Flask(__name__)
@app.route('/scraper', methods=["GET"])

def scraper():
	query = request.args.get("query")
	zipcode = request.args.get("zipcode")
	radius = request.args.get("radius")


	out = []
	scraped = scrape(query,zipcode,radius)

	out.append(scraped)
	#jsonOut = json.dumps(out)

	return jsonify(out)


	# searchQuery = str(input("What are you searching for?\n"))
	# zipCode = int(input("What is your zipcode?\n"))
	# radius = int(input("What mile radius? (5,10,25,50,100,500)\n"))

@app.route('/uber')

def uber():
	address = request.args.get('address')

	coords = getCoords(address)

	out = []

	uberData = getData(coords[0], coords[1])
	
	out.append(uberData)
	#jsonOut = json.dumps(out)

	return jsonify(out)


@app.route('/coords')

def coords():
	address = request.args.get('address')

	coords = getCoords(address)

	coordsDict = {"lat": coords[0], "lng": coords[1]}

	out = []

	out.append(coordsDict)
	#jsonOut = json.dumps(out)

	return jsonify(out)


	


if __name__ == '__main__':
    app.run()

#comment