import requests
import json
import socket
from requests import get


def location_of_me():
    """
    {
      "ip": "134.201.250.155",
      "hostname": "134.201.250.155",
      "type": "ipv4",
      "continent_code": "NA",
      "continent_name": "North America",
      "country_code": "US",
      "country_name": "United States",
      "region_code": "CA",
      "region_name": "California",
      "city": "Los Angeles",
      "zip": "90013",
      "latitude": 34.0453,
      "longitude": -118.2413,
      "location": {
        "geoname_id": 5368361,
        "capital": "Washington D.C.",
        "languages": [
            {
              "code": "en",
              "name": "English",
              "native": "English"
            }
        ],
        "country_flag": "https://assets.ipstack.com/images/assets/flags_svg/us.svg",
        "country_flag_emoji": "🇺🇸",
        "country_flag_emoji_unicode": "U+1F1FA U+1F1F8",
        "calling_code": "1",
        "is_eu": false
      },
      "time_zone": {
        "id": "America/Los_Angeles",
        "current_time": "2018-03-29T07:35:08-07:00",
        "gmt_offset": -25200,
        "code": "PDT",
        "is_daylight_saving": true
      },
      "currency": {
        "code": "USD",
        "name": "US Dollar",
        "plural": "US dollars",
        "symbol": "$",
        "symbol_native": "$"
      },
      "connection": {
        "asn": 25876,
        "isp": "Los Angeles Department of Water & Power"
      },
      "security": {
        "is_proxy": false,
        "proxy_type": null,
        "is_crawler": false,
        "crawler_name": null,
        "crawler_type": null,
        "is_tor": false,
        "threat_level": "low",
        "threat_types": null
      }
    }
    """
    ip = get('https://api.ipify.org').text
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    send_url = "http://api.ipstack.com/" + ip + "?access_key=7cd335b5d7a832f1c08b66e758797dc4"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    return geo_json
    # city = geo_json['city']
    # return city


# cat = location_of_me()
# print(cat['location']['languages'][0]['native'])


# Weather Data


def weather_data(query):
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?' +
                       query +
                       '&APPID=0142515b87702fb26174239fb8b60b09&units=metric')
    # lat = "33.6007"
    # lon = "73.0679"
    # res = requests.get('http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat=' + lat + '&lon=' + lon + '&appid=0142515b87702fb26174239fb8b60b09')
    return res.json()


cat = location_of_me()
city = cat['city']
query = 'q=' + str(city)
w_data = weather_data(query)

# print(w_data)

def love_calculator():
  url = "https://love-calculator.p.rapidapi.com/getPercentage"

  querystring = {"fname":"Fahad Malik","sname":"Gulalay"}

  headers = {
      'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
      'x-rapidapi-host': "love-calculator.p.rapidapi.com"
      }

  response = requests.request("GET", url, headers=headers, params=querystring)

  print(response.text)
  
# love_calculator()

def url_shortner():
  url = "https://url-shortener-service.p.rapidapi.com/shorten"

  payload = "url=https://www.amazon.com"
  headers = {
      'content-type': "application/x-www-form-urlencoded",
      'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
      'x-rapidapi-host': "url-shortener-service.p.rapidapi.com"
      }

  response = requests.request("POST", url, data=payload, headers=headers)

  print(response.text)
  
# url_shortner()

def currency_converter():
  """
  0:"SGD"
  1:"MYR"
  2:"EUR"
  3:"USD"
  4:"AUD"
  5:"JPY"
  6:"CNH"
  7:"HKD"
  8:"CAD"
  9:"INR"
  10:"DKK"
  11:"GBP"
  12:"RUB"
  13:"NZD"
  14:"MXN"
  15:"IDR"
  16:"TWD"
  17:"THB"
  18:"VND"
  """
  url = "https://currency-exchange.p.rapidapi.com/exchange"

  querystring = {"from":"SGD","to":"MYR","q":"1.0"}

  headers = {
    
      'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
      'x-rapidapi-host': "currency-exchange.p.rapidapi.com"
      }

  response = requests.request("GET", url, headers=headers, params=querystring)

  print(response.text)

class SkyScanner:
  
  def __init__(self):
    return ("SkyScanner")
  
  def main():
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/referral/v1.0/America/dollar/Miami/Miami/Miami/2021-01/2021-02"

    querystring = {"shortapikey":"ra66933236979928","apiKey":"{shortapikey}"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
    
    
class cocktail:
  
  def main():
    url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"
    
    response = requests.request("GET", url)
    
    print(response.text)
    
  def apis():
    """
    Search cocktail by name
    https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita

    List all cocktails by first letter
    https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a

    Search ingredient by name
    https://www.thecocktaildb.com/api/json/v1/1/search.php?i=vodka

    Lookup full cocktail details by id
    https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=11007

    Lookup ingredient by ID
    https://www.thecocktaildb.com/api/json/v1/1/lookup.php?iid=552

    Lookup a random cocktail
    https://www.thecocktaildb.com/api/json/v1/1/random.php
    
    Search by ingredient
    https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=Gin
    https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=Vodka
    
    Filter by alcoholic
    https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Alcoholic
    https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Non_Alcoholic

    Filter by Category
    https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Ordinary_Drink
    https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail

    Filter by Glass
    https://www.thecocktaildb.com/api/json/v1/1/filter.php?g=Cocktail_glass
    https://www.thecocktaildb.com/api/json/v1/1/filter.php?g=Champagne_flute
    
    """
    
# cocktail.main()

class world_info:
  
  def main():
    # To Gel information of all the countries
    url = "https://restcountries-v1.p.rapidapi.com/all"

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "restcountries-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)
  
  def apis():
    """
    Filter by Country name
    https://restcountries-v1.p.rapidapi.com/name/pakistan
    
    Filter by Country Code
    https://restcountries-v1.p.rapidapi.com/alpha/pk
    
    Filter by Calling Code
    https://restcountries-v1.p.rapidapi.com/callingcode/57
    
    Filter by Capital City
    https://restcountries-v1.p.rapidapi.com/capital/islamabad
    
    Filter by Currency
    https://restcountries-v1.p.rapidapi.com/currency/PKR
    
    Filter by Language
    https://restcountries-v1.p.rapidapi.com/lang/ur
    
    Filter by Region
    https://restcountries-v1.p.rapidapi.com/region/asia
    
    Filter by Subregion
    https://restcountries-v1.p.rapidapi.com/subregion/western%2520asia
    """
    
# world_info.main()

class yahoo_finance:
  
  def main():
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail"

    querystring = {"symbol":"TSLA","region":"US"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
# yahoo_finance.main()

class number_facts():
  """
  An API for interesting facts about numbers. Provides trivia, math, date, and year facts about numbers.

  For example, "5 is the number of platonic solids", "42 is the number of little squares forming the left side trail of Microsoft's Windows 98 logo", "February 27th is the day in 1964 that the government of Italy asks for help to keep the Leaning Tower of Pisa from toppling over"

  1. Get fact by a date
  2. Get fact about math by giving an years
  3. Get random fact from any type
  4. Get a trivia
  5. Get a fact by year
  
  """
  def date_fact():
    url = "https://numbersapi.p.rapidapi.com/6/21/date"

    querystring = {"fragment":"true","json":"true"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "numbersapi.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
  def math_fact():
    url = "https://numbersapi.p.rapidapi.com/1729/math"

    querystring = {"fragment":"true","json":"true"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "numbersapi.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
  def random_number_fact():
    url = "https://numbersapi.p.rapidapi.com/random/trivia"

    querystring = {"max":"20","fragment":"true","min":"10","json":"true"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "numbersapi.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
  def trivia_fact():
    url = "https://numbersapi.p.rapidapi.com/42/trivia"

    querystring = {"fragment":"true","notfound":"floor","json":"true"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "numbersapi.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
  def year_fact():
    url = "https://numbersapi.p.rapidapi.com/1492/year"

    querystring = {"fragment":"true","json":"true"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "numbersapi.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
class movie_entertain:
  
  def look_by_name():
    url = "https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/lookup"

    querystring = {"term":"bojack","country":"uk"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com"
        }
    
  def look_by_id():
    url = "https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/idlookup"

    querystring = {"source_id":"tt3398228","source":"imdb","country":"us"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
