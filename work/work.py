import re
from work import wishing, keyboard_controller, sound, locate_me, main_api, tictactoe, rps_game, sys_info
from work.dice import dice_roller
import pyperclip, webbrowser, wikipedia, keyboard
import clipboard, urllib.request, json
from layla.engine_components import speak, take_command
from functools import lru_cache
from work.background_changer import background_change
from WebScraping.lyrics import LyricsFinder
import random
import pyaudio
import wave
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

#App Id
app_id = 'A6JUQ4-JEAGJ3A583'


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
        if "wikipedia" in query:
            query = query.replace("wikipedia", "")
        elif "tell me about" in query:
            query = query.replace("tell me about", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According To wikipedia")
        return results


class video_controls:
    def change_volume(query):
        sound_value = [int(s) for s in query.split() if s.isdigit()][0]
        sound.Sound.volume_set(int(sound_value))
        speak("Volume changed to " + str(sound_value) + "percent")

    def mute(query):
        sound.Sound.volume_set(0)

    def max_sound(query):
        sound.Sound.volume_set(100)

    def increase_vol():
        sound.Sound.volume_up()

    def decrease_vol():
        sound.Sound.volume_down()


@lru_cache()
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
        return f"The city name is {loc['city']}"
    elif "continent" in query:
        speak(f"The name of continent is {loc['continent_name']}")
    elif "country" in query:
        speak(f"The name of continent is {loc['country_name']}")


@lru_cache()
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
        speak(
            f"You are located on latitude {latitude} and longitude {longitude}"
        )


class basic_functions:
    def lovecal(query):
        # Calculate love percentage between Imran Akbar and Laiba Sadaf
        print("done")
        f_split = query.split(' between ')
        f_split.pop(0)
        query = query.join(f_split)
        s_split = query.split(' and ')
        cat = locate_me.love_calculator(s_split[0], s_split[1])
        speak(
            cat.get("result") + " the love percentage between " +
            cat.get("fname") + " and " + cat.get("sname") + " is " +
            cat.get("percentage") + " percent")

    def urlshorten(query):
        # Short the url from my clipboard
        url = clipboard.paste()  # Note: Url Must start from https://
        finale = locate_me.url_shortner(url)
        if finale == "Not Found!":
            speak("Url Error")
        else:
            clipboard.copy(finale)
            speak(f"url successfully shorten, and copied to your clipboard")

    def jokes(query):
        finale = locate_me.jokes_v()
        speak(finale)

    def word_def(query):
        # What is meant by Cobra
        # meaning of Cobra
        # What is a radio
        if "by" in query:
            f_split = query.split(' by ')
            f_split.pop(0)
            query = query.join(f_split)
            finale = locate_me.dictionary(query)
        elif "of" in query:
            f_split = query.split(' of ')
            f_split.pop(0)
            query = query.join(f_split)
            finale = locate_me.dictionary(query)
        elif "is a" in query:
            f_split = query.split(' a ')
            f_split.pop(0)
            query = query.join(f_split)
            finale = locate_me.dictionary(query)
        speak(finale)

    # More Coming Soon


def answer_engine(query):
    main_query = query.replace(" ", "+")
    api = main_api.waAPI(app_id)
    spoken = api.spoken_results(i=main_query)
    return spoken


def unable_recognize():
    return "Sorry I Wasn't Able To Recoginze The Command"


def flip_coin():
    while True:
        flip = random.randint(0, 1)
        if (flip == 0):
            print("Heads")
            speak("heads")
        else:
            print("Tails")
            speak("tails")
        speak("Do you want to flip again")
        opt = take_command().lower()
        if opt == "yes":
            continue
        else:
            break


def roll_dice():
    dice_roller.window()


def play_tactactoe():
    tictactoe.start_game()


def play_rps():
    rps_game.rps_window()


class f_keyboard:
    def sys_func(query):
        # Shortcut Keys
        if "lock" in query:
            keyboard.press_and_release("win + l")
        elif "setting" in query:
            keyboard.press_and_release("win + i")
        elif "desktop" in query or "minimise all" in query:
            keyboard.press_and_release("win + d")
        elif "minimise" in query:
            keyboard.press_and_release("win + m")
        elif "start" in query:
            keyboard.press_and_release("win")
        elif "rename" in query:
            keyboard.press_and_release("f2")
        elif "search" in query:
            keyboard.press_and_release("f3")
        elif "refresh" in query:
            keyboard.press_and_release("f5")
        elif "properties" in query:
            keyboard.press_and_release("alt + enter")
        elif "display open apps" in query:
            keyboard.press_and_release("ctrl + alt + tab")
        elif "task manager" in query:
            keyboard.press_and_release("ctrl + shift + esc")
        elif "file explorer" in query:
            keyboard.press_and_release("win + e")

    def doc_func(query):
        if "undo" in query:
            keyboard.press_and_release('ctrl + z')
        elif "redo" in query:
            keyboard.press_and_release("ctrl + y")
        elif "paste" in query:
            keyboard.press_and_release("ctrl + v")
        elif "copy" in query:
            keyboard.press_and_release("ctrl + c")
        elif "cut" in query:
            keyboard.press_and_release("ctrl + x")
        elif "save" in query:
            keyboard.press_and_release("ctrl + s")
        elif "select all" in query:
            keyboard.press_and_release("ctrl + a")
        elif "go to end" in query:
            keyboard.press_and_release("ctrl + end")

    def desk_func(query):
        if "application" in query:
            if "next" in query:
                keyboard.press_and_release('alt + tab')
            elif "previous" in query:
                keyboard.press_and_release('alt + shift + tab')
        elif "desktop" in query:
            if "next" in query:
                keyboard.press_and_release('win + ctrl + right')
            elif "previous" in query:
                keyboard.press_and_release('win + ctrl + left')

    def chrome_func(query):
        if "new tab" in query:
            keyboard.press_and_release('ctrl + t')
        elif "reopen tab" in query:
            keyboard.press_and_release('ctrl + shift + t')
        elif "go back" in query:
            keyboard.press_and_release('alt + left')
        elif "go forward" in query:
            keyboard.press_and_release('alt + right')
        elif "take screenshot" in query:
            keyboard.press_and_release('win + shift + s')
        elif "show clipboard" in query:
            keyboard.press_and_release('win + v')
        elif "show emoji panel" in query:
            keyboard.press_and_release('win + .')
        elif "new folder" in query:
            keyboard.press_and_release('ctrl + shift + n')


@lru_cache()
def song_lyrics_finder(query):
    main_class = LyricsFinder(query)
    print(main_class.lyrics_finder())  #Solved


@lru_cache()
def syst_info():
    sys_info.syst()


@lru_cache()
def audio_recorder():
    current_date_and_time = datetime.datetime.now()
    current_date_and_time_string = str(current_date_and_time)
    extension = ".wav"
    # the file name output you want to record into
    filename = "recorded" + current_date_and_time_string + extension
    # set the chunk size of 1024 samples
    chunk = 1024
    # sample format
    FORMAT = pyaudio.paInt16
    # mono, change to 2 if you want stereo
    channels = 1
    # 44100 samples per second
    sample_rate = 44100
    record_seconds = 5
    # initialize PyAudio object
    p = pyaudio.PyAudio()
    # open stream object as input & output
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)
    frames = []
    print("Recording...")
    for i in range(int(44100 / chunk * record_seconds)):
        data = stream.read(chunk)
        # if you want to hear your voice while recording
        # stream.write(data)
        frames.append(data)
    print("Finished recording.")
    # stop and close stream
    stream.stop_stream()
    stream.close()
    # terminate pyaudio object
    p.terminate()
    # save audio file
    # open the file in 'write bytes' mode
    wf = wave.open(filename, "wb")
    # set the channels
    wf.setnchannels(channels)
    # set the sample format
    wf.setsampwidth(p.get_sample_size(FORMAT))
    # set the sample rate
    wf.setframerate(sample_rate)
    # write the frames as bytes
    wf.writeframes(b"".join(frames))
    # close the file
    wf.close()
