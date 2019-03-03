from flask import jsonify, json
from bs4 import BeautifulSoup, NavigableString
import requests

def scrape(searchQuery, zipCode, radius):
	# 	query = request.form["query"]
	# 	zipcode = request.form["zipcode"]
	# 	searchRadius = request.form["searchRadius"]


	# searchQuery = str(input("What are you searching for?\n"))
	# zipCode = int(input("What is your zipcode?\n"))
	# radius = int(input("What mile radius? (5,10,25,50,100,500)\n"))

	###browser = mechanicalsoup.StatefulBrowser()


def parser(search, zipCode, radius):
    url = 'https://clearhealthcosts.com/search/?query='
    response = requests.get(f"{url}{search}&zip_code={zipCode}&radius={radius}&submit=")
    soup = BeautifulSoup(response.text, 'lxml')
    results = soup.find('span', 'ui orange circular label')

    numResults = int(results.text.strip())
    dictionary = {}

    if numResults == 0:
        return dictionary

    parent = soup.find('div', 'ui sixteen wide mobile thirteen wide computer column')
    child = parent.contents[0]
    while child.name != 'h3':
        child = child.next_sibling
    child = child.next_sibling

    while len(parent.contents) > 0:

        if child.name == 'h4':

            name = child.getText()
            locations = []
            child = child.next_sibling

            while child is not None and child.name != 'h4':

                if isinstance(child, NavigableString):
                    child = child.next_sibling
                    continue

                latitude = child.find('meta', {'itemprop': 'latitude'})['content']
                longitude = child.find('meta', {'itemprop': 'longitude'})['content']
                youPay = child.find('div', 'price-badge price-paid').contents[3].getText()

                locations.append({
                    'latitude': latitude,
                    'longitude': longitude,
                    'youPay': youPay
                })

                child = child.next_sibling

            dictionary[name] = locations
        if child is None:
            break
        else:
            child = child.next_sibling
	
    return dictionary
