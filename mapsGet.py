import urllib.request
import json


def getCoords(address):
	#address = '830+S.+Flower+Street,+Pasadena+CA'

	url = "https://maps.googleapis.com/maps/api/geocode/json?address="
	api_key = "&key=AIzaSyCs01kG6fg52B9YuvUp9RCc9XYwRtURdW0"
	newUrl = url + address.replace(" ", "+") + api_key
	
	contents = json.load(urllib.request.urlopen(newUrl))

	coordinates = contents['results'][0]['geometry']['location']
		
	return [coordinates["lat"], coordinates["lng"]]

print(getCoords("1600+Amphitheatre+Parkway,+Mountain+View,+CA"))









