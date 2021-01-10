import re
from work import wishing, sound, keyboard_controller
import pyperclip, webbrowser, wikipedia
from layla.engine_components import speak, take_command


def kali():
    return "Hello World"


def wishMe():
    if 4 <= wishing.hour < 10:
        return wishing.morning_commands()
    elif 10 <= wishing.hour < 13:
        return wishing.noon_commands()
    elif 13 <= wishing.hour < 17:
        return wishing.afternoon_commands()
    elif 17 <= wishing.hour < 23:
        return wishing.evening_commands()
    else:
        return wishing.night_commands()


def wikipedia_search(query):
    speak("Searching Wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According To wikipedia")
    print(results)
    return results


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
    return "Volume changed to " + sound_value + "percent"
