import requests
import json
import socket
from requests import get
import clipboard, urllib.request

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
# print(cat)


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

def love_calculator(f_name, s_name):
  url = "https://love-calculator.p.rapidapi.com/getPercentage"

  querystring = {"fname":f_name,"sname":s_name}

  headers = {
      'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
      'x-rapidapi-host': "love-calculator.p.rapidapi.com"
      }

  response = requests.request("GET", url, headers=headers, params=querystring)

  yahoo = response.json()
  return(yahoo)

def url_shortner(copy_url):
  url = "https://url-shortener-service.p.rapidapi.com/shorten"

  payload = "url=" + copy_url
  headers = {
      'content-type': "application/x-www-form-urlencoded",
      'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
      'x-rapidapi-host': "url-shortener-service.p.rapidapi.com"
      }

  response = requests.request("POST", url, data=payload, headers=headers)

  yahoo = response.json()
  return(yahoo.get("result_url", "Not Found!"))

def jokes_v():
  url = "https://joke3.p.rapidapi.com/v1/joke"

  headers = {
      'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
      'x-rapidapi-host': "joke3.p.rapidapi.com"
      }

  response = requests.request("GET", url, headers=headers)

  yahoo = response.json()
  return(yahoo.get("content"))
  
def dictionary(word):
  url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word

  response = requests.request("GET", url)

  yahoo = response.json()
  return(yahoo[0]["meanings"][0]["definitions"][0]["definition"])

    
# word_def("what is a crab")
    
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
    
class web_search():
  """
  This Function can search any data on the internet.
  
  1. Autocomplete = to complete the word by all the suitable words
  2. ImageSearch = To search all the image related to query
  3. SpellCheck = to check weather the spelling is right or not
  4. WebSearch = Search the Web and show the results
  5. Google News = To show all the google news according to the condition
  
  
  """
  def auto_complete():
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/spelling/AutoComplete"

    querystring = {"text":"do"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
  def image_search():
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI"

    querystring = {"q":"taylor swift","pageNumber":"1","pageSize":"10","autoCorrect":"true"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
  def spell_check():
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/spelling/SpellCheck"

    querystring = {"text":"teylor swiift"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
  def web_search():
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI"

    querystring = {"q":"taylor swift","pageNumber":"1","pageSize":"10","autoCorrect":"true"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
  def google_news():
    url = "https://google-news1.p.rapidapi.com/topic-headlines"
    # url = "https://google-news1.p.rapidapi.com/geolocation"
    # url = "https://google-news1.p.rapidapi.com/search"
    # url = "https://google-news1.p.rapidapi.com/top-headlines"

    querystring = {"topic":"WORLD","country":"US","lang":"en"}
    # querystring = {"geo":"Alabama","country":"US","lang":"en"}
    # querystring = {"q":"Covid","country":"US","lang":"en"}
    # querystring = {"country":"US","lang":"en"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "google-news1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


class music_Cat:
  """
  This class consists of all the function which are associated with Music.
  
  It can be searching lyrics, billboard ranking, search for a song, or complete a song name.
  """
  def lyrics():
    url = "https://sridurgayadav-chart-lyrics-v1.p.rapidapi.com/apiv1.asmx/SearchLyricDirect"

    querystring = {"artist":"michael jackson","song":"bad"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "sridurgayadav-chart-lyrics-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
  def billboard():
    url = "https://billboard-api2.p.rapidapi.com/hot-100"
    # url = "https://billboard-api2.p.rapidapi.com/artist-100"
    # url = "https://billboard-api2.p.rapidapi.com/billboard-200"

    querystring = {"date":"2019-05-11","range":"1-10"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "billboard-api2.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
  def complete_song():
    url = "https://shazam.p.rapidapi.com/auto-complete"

    querystring = {"term":"kiss the","locale":"en-US"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
  def search():
    url = "https://shazam.p.rapidapi.com/search"

    querystring = {"term":"kiss the rain","locale":"en-US","offset":"0","limit":"5"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
class goe_data:
  """
  
  """
  def cities():
    """
    Following are some of the functions which can be done in this function.
    
    1. Search Information about cith by wikidataid
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/Q60"
    
    2. Nearby cities
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/Q60/nearbyCities"
    
    3. City Time 
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/Q60/time"
    
    
    """
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
    
    querystring = {"limit":"10","countryIds":"PK"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "wft-geo-db.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)
    
  def countries():
    """
    Following are some of the functions which can be done in this function.
    
    1. Search Information about Country by Countrycode
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries/US"
    
    2. Search Country region
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries/US/regions"
    
    3. And region Detail
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries/US/regions/CA"
    
    4. And Region Cities
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries/US/regions/CA/cities"
    """
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries"

    querystring = {"currencyCode":"PKR"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "wft-geo-db.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
  def city_distance():
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/Q1362/distance"

    querystring = {"fromCityId":"Q1362","distanceUnit":"KM","toCityId":"Q8660"}

    headers = {
        'x-rapidapi-key': "1378d3ada6mshc004440669521cfp1cc4b4jsnd7f48a863565",
        'x-rapidapi-host': "wft-geo-db.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text) 

