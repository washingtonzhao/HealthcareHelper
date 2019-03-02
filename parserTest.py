import mechanicalsoup
from bs4 import BeautifulSoup
import urllib3

searchQuery = "19543X Blood test -- cholesterol lipids"
zipCode = 90089
radius = "5"

browser = mechanicalsoup.StatefulBrowser()

browser.open("https://clearhealthcosts.com")

browser.select_form('form[action="/search"]')

browser["query"] = searchQuery
browser["zip_code"] = zipCode
browser["radius"] = radius

browser.launch_browser()

response = browser.submit_selected()

print(browser.get_url())

http = urllib3.PoolManager()
response = http.request('GET', browser.get_url())

soup = BeautifulSoup(response.data)

## need to be able to get multiple addresses
name_box = soup.find_all('span', attrs={'class': 'address'},recursive=False)
for name in name_box:
    print(name)
