def getData(end_la, end_lo):
	import json
	from uber_rides.session import Session
	from uber_rides.client import UberRidesClient
	session = Session(server_token="rLvqhp6YAeoa_DS20C_ROun-zvcBw5wzr9AageOL")
	client = UberRidesClient(session)
	response = client.get_price_estimates(
    	start_latitude=34.140,
    	start_longitude=-118.124,
    	end_latitude=end_la,
    	end_longitude=end_lo,
    	seat_count=2
    	)

	estimate = response.json.get('prices')


	cost = estimate[4]["estimate"]
	rideDuration = estimate[4]["duration"]//60

	out = {"cost": cost, "rideDuration": rideDuration}

	return out


#comment


