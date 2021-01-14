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
  
url_shortner()

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
