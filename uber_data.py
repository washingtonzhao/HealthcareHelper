from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')



def getData():
	import json
	from uber_rides.session import Session
	from uber_rides.client import UberRidesClient
	session = Session(server_token="rLvqhp6YAeoa_DS20C_ROun-zvcBw5wzr9AageOL")
	client = UberRidesClient(session)
	response = client.get_price_estimates(
    	start_latitude=34.140,
    	start_longitude=-118.124,
    	end_latitude=34.134,
    	end_longitude=-118.152,
    	seat_count=2
    	)

	estimate = response.json.get('prices')


	cost = estimate[4]["estimate"]
	rideDuration = estimate[4]["duration"]//60

	out = {"cost": cost, "rideDuration": rideDuration}

	return render_template("index.html", name=out)

if __name__ == "__main__":
	app.run()



