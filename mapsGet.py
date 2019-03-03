import urllib.request
import json


def getCoords(address):
	#address = '830+S.+Flower+Street,+Pasadena+CA'

	url = "https://maps.googleapis.com/maps/api/geocode/json?address="
	api_key = "&key=AIzaSyDisXGa754nT8E328j--7TMtNVxEzBynXI"
	newUrl = url + address.replace(" ", "+").replace("#", "") + api_key
	
	contents = json.load(urllib.request.urlopen(newUrl))

	coordinates = contents['results'][0]['geometry']['location']
		
	return [coordinates["lat"], coordinates["lng"]]









