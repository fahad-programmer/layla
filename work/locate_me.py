import requests
import json
import socket
from requests import get

def location_of_me():
    ip = get('https://api.ipify.org').text
    hostname = socket.gethostname() 
    IPAddr = socket.gethostbyname(hostname)
    send_url = "http://api.ipstack.com/"+ ip +"?access_key=7cd335b5d7a832f1c08b66e758797dc4"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    return geo_json
    # city = geo_json['city']
    # return city

# cat = location_of_me()
# print(cat['location']['languages'][0]['native'])

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

# Weather Data

def weather_data(query):
    res = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?' + query + '&APPID=0142515b87702fb26174239fb8b60b09&units=metric')
    # lat = "33.6007"
    # lon = "73.0679"
    # res = requests.get('http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat=' + lat + '&lon=' + lon + '&appid=0142515b87702fb26174239fb8b60b09')
    return res.json()

cat = location_of_me()
city = cat['city']
query = 'q=' + city
w_data = weather_data(query)

# print(w_data)