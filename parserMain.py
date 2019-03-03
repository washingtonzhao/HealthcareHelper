from flask import Flask, request
from flask import render_template
from flask import jsonify, json
from uber_data_helper import getData
from scraper import scrape



app = Flask(__name__)
@app.route('/scraper', methods=["GET","POST"])

def scraper():
	query = request.args.get("query")
	zipcode = request.args.get("zipcode")
	radius = request.args.get("radius")


	out = []
	scraped = scrape(query,zipcode,radius)

	out.append(scraped)
	jsonOut = json.dumps(out)

	return jsonify(jsonOut)


	# searchQuery = str(input("What are you searching for?\n"))
	# zipCode = int(input("What is your zipcode?\n"))
	# radius = int(input("What mile radius? (5,10,25,50,100,500)\n"))


	


if __name__ == '__main__':
    app.run()
