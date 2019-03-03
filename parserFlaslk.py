from flask import Flask, request
from flask import render_template
from flask import jsonify, json
from uber_data_helper import getData


import mechanicalsoup
from bs4 import BeautifulSoup
import urllib3
import certifi


# app = Flask(__name__)
# @app.route('/search', methods=["GET","POST"])


def search():
	# if request.method == "POST":

	# 	query = request.form["query"]
	# 	zipcode = request.form["zipcode"]
	# 	searchRadius = request.form["searchRadius"]


	searchQuery = str(input("What are you searching for?\n"))
	zipCode = int(input("What is your zipcode?\n"))
	radius = int(input("What mile radius? (5,10,25,50,100,500)\n"))

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
	    addresses = soup.findAll('span', attrs={'itemprop', 'address'})
	    priceList = []
	    addressList = []

	    for price in prices:
	        priceList.append(price.text.strip("Price charged \n"))
	    print(priceList)

	    for address in addresses:
	        addressList.append(address.text.strip())
	    print(addressList)


	    i = 0
	    outputDict = {}
	    while i < len(priceList):
	    	outputDict[addressList[i]] = priceList[i]
	    	i +=1

	    print(outputDict)


	else:
	    print("Sorry, there were no reported results for prices in our database.")


	


# if __name__ == '__main__':
#     app.run()

search()

