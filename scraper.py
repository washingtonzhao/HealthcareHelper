from flask import jsonify, json
from mapsGet import getCoords


import mechanicalsoup
from bs4 import BeautifulSoup
import urllib3
import certifi

def scrape(searchQuery, zipCode, radius):
	# 	query = request.form["query"]
	# 	zipcode = request.form["zipcode"]
	# 	searchRadius = request.form["searchRadius"]


	# searchQuery = str(input("What are you searching for?\n"))
	# zipCode = int(input("What is your zipcode?\n"))
	# radius = int(input("What mile radius? (5,10,25,50,100,500)\n"))

	browser = mechanicalsoup.StatefulBrowser()

	browser.open("https://clearhealthcosts.com")

	browser.select_form('form[action="/search"]')

	browser["query"] = searchQuery
	browser["zip_code"] = zipCode
	browser["radius"] = radius

	##browser.launch_browser()

	response = browser.submit_selected()

	##print(browser.get_url())

	http = urllib3.PoolManager(cert_reqs ='CERT_REQUIRED',ca_certs = certifi.where())
	response = http.request('GET', browser.get_url())
	soup = BeautifulSoup(response.data,'lxml')

	results = soup.find('span', 'ui orange circular label')

	numResults = int(results.text.strip())
	##print(numResults)

	if numResults > 0: 
	    prices = soup.findAll('div',attrs={'class','price-badge price-charged'})
	    addresses = soup.findAll('span', attrs={'itemprop', "address"})
	    hospName = soup.findAll('span', attrs={'class','provider'})
	    
	    priceList = []
	    addressList = []
	    hospList = []
	    coordsList = []

	    for price in prices:
	        priceList.append(price.text.strip("Price charged \n"))

	    for address in addresses:
	        addressList.append(address.text.strip())
	        coordsList.append(getCoords(address.text.strip()))

	    for hosp in hospName:
	    	hospList.append(hosp.text.strip())


	    i = 0
	    outputDict = {}
	    option = "option"
	    while i < len(priceList):
	    	outputDict[option + str(i+1)] = [hospList[i], addressList[i], coordsList[i], priceList[i]]
	    	i +=1

	    return outputDict


	else:
	    return "Sorry, there were no reported results in our database."