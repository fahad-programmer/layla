import re
from work import wishing, keyboard_controller, sound, locate_me
import pyperclip, webbrowser, wikipedia
from layla.engine_components import speak, take_command


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


def wikipedia_search(query):
    speak("Searching Wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According To wikipedia")
    print(results)
    speak(results)


def google_map_search(query):
    if "search google map from clipboard" == query:
        query = pyperclip.paste()
    else:
        speak("which place do you want to see")
        query = take_command().lower()
    speak(f"Going to {query}...")
    webbrowser.open('https://www.google.com/maps/place/' + query)


def change_volume(query):
    sound_value = [int(s) for s in query.split() if s.isdigit()][0]
    sound.Sound.volume_set(int(sound_value))
    speak("Volume changed to " + query + "percent")

def my_country_info(query):
    loc = locate_me.location_of_me()
    if "ip" in query:
        speak(f"The ip of this PC is {loc['ip']}")
    elif "city" in query:
        speak(f"The city name is {loc['city']}")
    elif "continent" in query:
        speak(f"The name of continent is {loc['continent_name']}")
        
    
