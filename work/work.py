import wishing, sound

def kali():
    speak("Hello World")

def wishMe():
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
        query = takeCommand().lower()
    speak(f"Going to {query}...")
    webbrowser.open('https://www.google.com/maps/place/' + query)
    
def change_volume(query):
    query = query.replace("change volume to", "")
    sound.Sound.volume_set(int(query))
    speak("Volume changed to " + query + "percent")