import re
from work import wishing, keyboard_controller, sound, locate_me
import pyperclip, webbrowser, wikipedia
import clipboard
from layla.engine_components import speak, take_command

"""
What things i am working on:
1. Scraping websites data
2. Training model to learn new commands as user speak
3. Working with OpenCV to work on vidoes and photos
4. Woriking with Database:
    1. Add all the data we scrap in database and delete that data after a week.
    2. Layla will take data from the database, and data will be updated everyweek.
    3. Working with Videos (play, sound, subtitles etc)
5. Find APIs as many as i can and use them.

Working with ❤/>
"""

def kali():
    speak("Hello World")


def wish_me():
    if 4 <= wishing.hour < 10:
        speak(wishing.morning_commands())
    elif 10 <= wishing.hour < 13:
        speak(wishing.noon_commands())
    elif 13 <= wishing.hour < 17:
        speak(wishing.afternoon_commands())
    elif 17 <= wishing.hour < 23:
        speak(wishing.evening_commands())
    else:
        speak(wishing.night_commands())


class website_control:
    '''
    Title = In this class all the websites related functions are being held.
    
    For Example, Opening Websites, Search On Websites, Doing Some Stuff, Taking Data from the websites...
    
    This class also consist of all the data which is being scraped from the internet.
    '''
    def __init__(self):
        return "Fuck You, You have no value nerd..."

    @staticmethod
    def google_search(query):
        if "search" in query:
            term = ' '.join(query.split()[1:])
            speak('searching ' + term + "on google")
            webbrowser.open("https://www.google.com/search?q=" + term)
        elif "no" in query:
            pass

    def google_map_search(query):
        if "search google map from clipboard" == query:
            query = pyperclip.paste()
        else:
            speak("which place do you want to see")
            query = take_command().lower()
        speak(f"Going to {query}...")
        webbrowser.open('https://www.google.com/maps/place/' + query)

    @staticmethod
    def search_websites(query):
        # search how to bake on google
        web_name = ''.join(query.split()[-1:])
        term = ' '.join(query.split()[1:-2])
        webbrowser.open("https://www." + web_name + ".com/search?q=" + term)

    @staticmethod
    def main(query):
        name = ' '.join(query.split()[1:])
        wbsite = ''.join(query.split()[1:])
        speak('opening ' + name + "dot com")
        webbrowser.open('https://www.' + wbsite + '.com')
        if query == "google":
            speak("Do you want to search anything on google")
            query = take_command().lower()
            google_search(query)
        
    @staticmethod
    def wikipedia_search(query):
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According To wikipedia")
        print(results)
        speak(results)


def change_volume(query):
    sound_value = [int(s) for s in query.split() if s.isdigit()][0]
    sound.Sound.volume_set(int(sound_value))
    speak("Volume changed to " + str(sound_value) + "percent")

def country_info(query):
    loc = locate_me.location_of_me()
    if "ip" in query:
        speak(f"The ip of this PC is {loc['ip']}")
    elif "continent code" in query:
        speak(f"The Continent code is {loc['continent_code']}")
    elif "country code" in query:
        speak(f"The Country code is {loc['country_code']}")
    elif "region code" in query:
        speak(f"The Region code is {loc['region_code']}")
    elif "region" in query:
        speak(f"The region name is {loc['region_name']}")
    elif "city" in query:
        speak(f"The city name is {loc['city']}")
    elif "continent" in query:
        speak(f"The name of continent is {loc['continent_name']}")
    elif "country" in query:
        speak(f"The name of continent is {loc['continent_name']}")


def weather_info(query):
    loc = locate_me.w_data
    if "temperature" in query:
        temp = ("{}°C".format(loc['main']['temp']))
        speak(temp)
    if "minimum temperature" in query:
        temp = ("{}°C".format(loc['main']['temp_min']))
        speak(temp)
    if "maximum temperature" in query:
        temp = ("{}°C".format(loc['main']['temp_max']))
        speak(temp)
    if "pressure" in query:
        pre = ("{} pascal".format(loc['main']['pressure']))
        speak(pre)
    if "humidity" in query:
        pre = ("today humidity level is {}".format(loc['main']['humidity']))
        speak(pre)
    elif "wind" in query:
        speed = loc['wind']['speed']
        speak(f"{speed} meter per second")
    elif "weather" in query:
        weather = loc['weather'][0]['main']
        speak(f"Sir it's {weather}")
    elif "coordinates" in query:
        latitude = loc['coord']['lat']
        longitude = loc['coord'][['lon']]
        speak(f"You are located on latitude {latitude} and longitude {longitude}")
    
class basic_functions:
    
    def lovecal(query):
        # Calculate love percentage between Imran Akbar and Laiba Sadaf
        f_split = query.split(' between ')
        f_split.pop(0)
        query = query.join(f_split)
        s_split = query.split(' and ')
        locate_me.love_calculator(s_split[0], s_split[1])
        # API didn't work, developing a new scratch function
        
    def urlshorten(query):
        # Short the url from my clipboard
        url = clipboard.paste()     # Note: Url Must start from https://
        finale = locate_me.url_shortner(url)
        clipboard.copy(finale)
        speak(f"url successfully shorten, and copid to your clipboard")
