import json
from uber_rides.session import Session

session = Session(server_token="rLvqhp6YAeoa_DS20C_ROun-zvcBw5wzr9AageOL")


from uber_rides.client import UberRidesClient
client = UberRidesClient(session)
response = client.get_price_estimates(
    start_latitude=34.140,
    start_longitude=-118.124,
    end_latitude=34.134,
    end_longitude=-118.152,
    seat_count=2
)

estimate = response.json.get('prices')

print(estimate[0]["estimate"])