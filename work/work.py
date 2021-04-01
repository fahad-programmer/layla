"""
This file consists all the functions which is to be performed by the System.
Including games, services and answers
We are using If/Else statement but soon will be minimized by ML and AI

Classes:

    website_control
    video_controls
    basic_functions
    f_keyboard

Functions:

    kali()
    wish_me()
    country_info(query)
    answer_engine(query)
    unable_recognize() -> str
    flip_coin()
    roll_dice()
    play_tactactoe()
    play_rps()
    song_lyrics_finder(query)
    syst_info()
    audio_recorder()

Misc variables:

    None
    
Last Updated: TU/23/3/2021
By: imran-prog
"""

#Importing Builtin Modules
import re
import pyperclip, webbrowser, wikipedia, keyboard
import clipboard, urllib.request, json
from functools import lru_cache
import random, datetime
import pyaudio
import wave
import win32gui, win32api
import http.server
import socket, socketserver
import pyqrcode
from pyqrcode import QRCode
import png, os
# Importing user made Modules
from work import wishing, keyboard_controller, sound, locate_me, main_api, tictactoe, rps_game, sys_info
from work.dice import dice_roller
from layla.engine_components import speak, take_command
from work.background_changer import background_change
from WebScraping.lyrics import LyricsFinder
from work import search_web
"""
What things We am working on:
1. Scraping websites data
2. Training model to learn new commands as user speak
3. Working with OpenCV to work on vidoes and photos
4. Woriking with Database:
    1. Add all the data we scrap in database and delete that data after a week.
    2. Layla will take data from the database, and data will be updated everyweek.
    3. Working with Videos (play, sound, subtitles etc)
5. Add many algorithms
    

Working with ❤/>
"""

# App Id For Search API function answer_engine()
app_id = 'A6JUQ4-JEAGJ3A583'

# File Starts Here
def kali():
    '''
    Returns the sum of two decimal numbers in binary digits.

        Parameters:
            a (int): A decimal integer
            b (int): Another decimal integer

        Returns:
            binary_sum (str): Binary string of the sum of a and b
    '''
    speak("Hello World")


def wish_me():
    '''
    Speaks a statement when run for the first time. It checks the time of the day and make it's choice as per the time of the day.

        Parameters:
            None

        Speak:
            The statement as per the day time
    '''
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
    ...

    Attributes
    ----------
    query : str
        Command given by the user to open ors search on websites

    Methods
    -------
    __init__(self):
        Prints a joke

    web_search(self, query):
        Search Google for the query
        
    google_map_search(self, query):
        opens google map and find the location which user has said to.
        
    main(self, query):
        To Open any website in the browser with .com domain
    
    wikipedia_search(self, query):
        Search wikipedia and display the best answer for the query
        
    '''
    def __init__(self):
        '''
        This function is not used anywhere. 
        It's just represents that this function is not being used anywhere.
        '''
        self.message = "Fuck You, You have no value nerd..."

    def web_search(self, query):
        '''
        It's search the statement on the any website. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google
                > search how to make spotify account on yahoo

            Output:
                Search query on the given website. and open the link in the browser.
                
        '''
        search_content = search_web.search_internet(self.query)
        search_content.web_search()
    
    def google_map_search(self, query):
        '''
        Open's Google map in browser and take's the user to the given location

            Parameters:
                query (string): Statement given by the user to perform this function
                
            Conditions:
                -> query (From clipboard): Get the location name from the clipboard of the user
                -> query (From Input) : Get the location name from thespeak input

            Output:
                Browser with the Google map website and the location user searched for.
                
        '''
        if "search google map from clipboard" == self.query:
            self.query = pyperclip.paste()
        else:
            speak("which place do you want to see")
            self.query = take_command().lower()
        speak(f"Going to {self.query}...")
        webbrowser.open('https://www.google.com/maps/place/' + self.query)


    def main(self, query):
        '''
        This function will open any website which has .com domain. 
        and if any of the website's from the list come's as a query
        It will go to the web_serch() function to search for it.

            Parameters:
                query (string): Website name
                
            Input Form:
                > open google
                > open facebook

            Output:
                Open the browser with the website user asked to open.
                otherwise if website name matched with the list item it will prompt to search too.
                
        '''
        self.name = ' '.join(query.split()[1:])
        self.website = ''.join(query.split()[1:])
        self.website_names = ["google", "youtube", "pinterest", "linkedin", "tumblr", "imdb", "dailymotion", "yahoo", "duckduckgo", "twitter", "amazon", "alibaba"]
        for self.item in self.website_names:
            if self.name == self.website:
                speak("Do you want to search anything on" + self.name)
                self.query = take_command().lower()
                self.web_search(query)
                return
        speak('opening ' + self.name + "dot com")
        webbrowser.open('https://www.' + self.website + '.com')

    def wikipedia_search(self, query):
        '''
        This function is used to get the answer to the question or any kind of information from the wikipedia.

            Parameters:
                query (string): user given string to search on wiki
                
            Input Form:
                > wikipedia imran khan
                > tell me about indus valley

            Return:
                self.results (string): First few lines of wikipedia article
                
        '''
        speak("Searching Wikipedia...")
        if "wikipedia" in self.query:
            self.query = self.query.replace("wikipedia", "")
        elif "tell me about" in query:
            self.query = self.query.replace("tell me about", "")
        self.results = wikipedia.summary(query, sentences=2)
        speak("According To wikipedia")
        return self.results


class video_controls:
    '''
    Title = In this class all the system sound functions are going to perform.
    
    For Example, Volume Up, Volume Down, Set Volume to, etc...
    ...

    Attributes
    ----------
    query : str
        Command given by the user to change the sound

    Methods
    -------
    change_volume(query): static method
        It will change the system volume to the given integer 0-100

    mute(query): static method
        It will set the volume to zero
        
    max_sound(query): static method
        It will set the volume to 100
        
    increase_vol(): static method
        It will increase the volume of system by 5
    
    decrease_vol(): static method
        It will decrease the volume by 5
        
    '''
    @staticmethod
    def change_volume(query):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        sound_value = [int(s) for s in query.split() if s.isdigit()][0]
        sound.Sound.volume_set(int(sound_value))
        speak("Volume changed to " + str(sound_value) + "percent")

    @staticmethod
    def mute(query):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        sound.Sound.volume_set(0)

    @staticmethod
    def max_sound(query):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        sound.Sound.volume_set(100)

    @staticmethod
    def increase_vol():
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        sound.Sound.volume_up()
    
    @staticmethod
    def decrease_vol():
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        sound.Sound.volume_down()
    
    @staticmethod
    def pause_play():
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        VK_MEDIA_PLAY_PAUSE = 0xB3
        hwcode = win32api.MapVirtualKey(VK_MEDIA_PLAY_PAUSE, 0)
        win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, hwcode)
    
    @staticmethod
    def previous_track():
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        VK_MEDIA_PREVIOUS = 0xB1
        hwcode = win32api.MapVirtualKey(VK_MEDIA_PREVIOUS, 0)
        win32api.keybd_event(VK_MEDIA_PREVIOUS, hwcode)
        
    @staticmethod
    def next_track():
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        VK_MEDIA_PLAY_NEXT = 0xB0
        hwcode = win32api.MapVirtualKey(VK_MEDIA_PLAY_NEXT, 0)
        win32api.keybd_event(VK_MEDIA_PLAY_NEXT, hwcode)

@lru_cache()
def country_info(query):
    '''
    Returns the sum of two decimal numbers in binary digits.

        Parameters:
            a (int): A decimal integer
            b (int): Another decimal integer

        Returns:
            binary_sum (str): Binary string of the sum of a and b
    '''
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
    '''
    Returns the sum of two decimal numbers in binary digits.

        Parameters:
            a (int): A decimal integer
            b (int): Another decimal integer

        Returns:
            binary_sum (str): Binary string of the sum of a and b
    '''
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
    '''
    Title = In this class all the websites related functions are being held.
    
    For Example, Opening Websites, Search On Websites, Doing Some Stuff, Taking Data from the websites...
    
    This class also consist of all the data which is being scraped from the internet.
    ...

    Attributes
    ----------
    query : str
        Command given by the user to open ors search on websites

    Methods
    -------
    __init__(self):
        Prints a joke

    google_search(self, query):
        Search Google for the query
        
    google_map_search(self, query):
        opens google map and find the location which user has said to.
        
    main(self, query):
        To Open any website in the browser with .com domain
    
    wikipedia_search(self, query):
        Search wikipedia and display the best answer for the query
        
    '''
    @staticmethod
    def lovecal(query):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        # Calculate love percentage between # and #
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

    @staticmethod
    def urlshorten(query):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        # Short the url from my clipboard
        url = clipboard.paste()  # Note: Url Must start from https://
        finale = locate_me.url_shortner(url)
        if finale == "Not Found!":
            speak("Url Error")
        else:
            clipboard.copy(finale)
            speak(f"url successfully shorten, and copied to your clipboard")

    @staticmethod
    def jokes(query):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        finale = locate_me.jokes_v()
        speak(finale)

    @staticmethod
    def word_def(query):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
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
    '''
    Returns the sum of two decimal numbers in binary digits.

        Parameters:
            a (int): A decimal integer
            b (int): Another decimal integer

        Returns:
            binary_sum (str): Binary string of the sum of a and b
    '''
    main_query = query.replace(" ", "+")
    api = main_api.waAPI(app_id)
    spoken = api.spoken_results(i=main_query)
    return spoken


def unable_recognize() -> str:
    '''
    Returns the sum of two decimal numbers in binary digits.

        Parameters:
            a (int): A decimal integer
            b (int): Another decimal integer

        Returns:
            binary_sum (str): Binary string of the sum of a and b
    '''
    return "Sorry I Wasn't Able To Recoginze The Command"


def flip_coin():
    '''
    Returns the sum of two decimal numbers in binary digits.

        Parameters:
            a (int): A decimal integer
            b (int): Another decimal integer

        Returns:
            binary_sum (str): Binary string of the sum of a and b
    '''
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
    '''
    Returns the sum of two decimal numbers in binary digits.

        Parameters:
            a (int): A decimal integer
            b (int): Another decimal integer

        Returns:
            binary_sum (str): Binary string of the sum of a and b
    '''
    dice_roller.window()


def play_tactactoe():
    '''
    Returns the sum of two decimal numbers in binary digits.

        Parameters:
            a (int): A decimal integer
            b (int): Another decimal integer

        Returns:
            binary_sum (str): Binary string of the sum of a and b
    '''
    tictactoe.start_game()


def play_rps():
    '''
    Returns the sum of two decimal numbers in binary digits.

        Parameters:
            a (int): A decimal integer
            b (int): Another decimal integer

        Returns:
            binary_sum (str): Binary string of the sum of a and b
    '''
    rps_game.rps_window()


class f_keyboard:
    '''
    Title = In this class all the websites related functions are being held.
    
    For Example, Opening Websites, Search On Websites, Doing Some Stuff, Taking Data from the websites...
    
    This class also consist of all the data which is being scraped from the internet.
    ...

    Attributes
    ----------
    query : str
        Command given by the user to open ors search on websites

    Methods
    -------
    __init__(self):
        Prints a joke

    google_search(self, query):
        Search Google for the query
        
    google_map_search(self, query):
        opens google map and find the location which user has said to.
        
    main(self, query):
        To Open any website in the browser with .com domain
    
    wikipedia_search(self, query):
        Search wikipedia and display the best answer for the query
        
    '''
    @staticmethod
    def sys_func(query):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
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

    @staticmethod
    def doc_func(query):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
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

    @staticmethod
    def desk_func(query):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
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

    @staticmethod
    def key_func(query):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        if "take screenshot" in query:
            keyboard.press_and_release('win + shift + s')
        elif "show clipboard" in query:
            keyboard.press_and_release('win + v')
        elif "show emoji panel" in query:
            keyboard.press_and_release('win + .')
        elif "new folder" in query:
            keyboard.press_and_release('ctrl + shift + n')
        elif "space" in query:
            keyboard.press_and_release('space')
        elif "capital" in query:
            keyboard.press_and_release('caps lock')
        elif "enter" in query:
            keyboard.press_and_release('enter')
        elif "tab" in query:
            keyboard.press_and_release('tab')


@lru_cache()
def song_lyrics_finder(query):
    '''
    Returns the sum of two decimal numbers in binary digits.

        Parameters:
            a (int): A decimal integer
            b (int): Another decimal integer

        Returns:
            binary_sum (str): Binary string of the sum of a and b
    '''
    main_class = LyricsFinder(query)
    print(main_class.lyrics_finder())  #Solved


@lru_cache()
def syst_info():
    '''
    Returns the sum of two decimal numbers in binary digits.

        Parameters:
            a (int): A decimal integer
            b (int): Another decimal integer

        Returns:
            binary_sum (str): Binary string of the sum of a and b
    '''
    sys_info.syst()
    
class chrome_func:
    '''
    Title = In this class all the websites related functions are being held.
    
    For Example, Opening Websites, Search On Websites, Doing Some Stuff, Taking Data from the websites...
    
    This class also consist of all the data which is being scraped from the internet.
    ...

    Attributes
    ----------
    query : str
        Command given by the user to open ors search on websites

    Methods
    -------
    __init__(self):
        Prints a joke

    web_search(self, query):
        Search Google for the query
        
    google_map_search(self, query):
        opens google map and find the location which user has said to.
        
    main(self, query):
        To Open any website in the browser with .com domain
    
    wikipedia_search(self, query):
        Search wikipedia and display the best answer for the query
        
    '''
    def __init__(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        self.w=win32gui
        self.window_name = self.w.GetWindowText (self.w.GetForegroundWindow())
    
    def bookmark(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('ctrl + d')
            
    def bookmark_manager(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('ctrl + shift + o')
            
    def history(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('ctrl + h')
    
    def search(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        VK_MEDIA_PLAY_NEXT = 0xAA
        hwcode = win32api.MapVirtualKey(VK_MEDIA_PLAY_NEXT, 0)
        win32api.keybd_event(VK_MEDIA_PLAY_NEXT, hwcode)
    
    def home(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        VK_MEDIA_PLAY_NEXT = 0xAC
        hwcode = win32api.MapVirtualKey(VK_MEDIA_PLAY_NEXT, 0)
        win32api.keybd_event(VK_MEDIA_PLAY_NEXT, hwcode)
    
    def back(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        VK_MEDIA_PLAY_NEXT = 0xA6
        hwcode = win32api.MapVirtualKey(VK_MEDIA_PLAY_NEXT, 0)
        win32api.keybd_event(VK_MEDIA_PLAY_NEXT, hwcode)
    
    def forward(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        VK_MEDIA_PLAY_NEXT = 0xA7
        hwcode = win32api.MapVirtualKey(VK_MEDIA_PLAY_NEXT, 0)
        win32api.keybd_event(VK_MEDIA_PLAY_NEXT, hwcode)
    
    def new_window(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('ctrl + n')
            
    def incognito(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('ctrl + shift + n')
            
    def new_tab(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('ctrl + t')
            
    def page_source(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('ctrl + u')
    
    def reopen_tab(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('ctrl + shift + t')


class youtube_func:
    '''
    Title = In this class all the websites related functions are being held.
    
    For Example, Opening Websites, Search On Websites, Doing Some Stuff, Taking Data from the websites...
    
    This class also consist of all the data which is being scraped from the internet.
    ...

    Attributes
    ----------
    query : str
        Command given by the user to open ors search on websites

    Methods
    -------
    __init__(self):
        Prints a joke

    web_search(self, query):
        Search Google for the query
        
    google_map_search(self, query):
        opens google map and find the location which user has said to.
        
    main(self, query):
        To Open any website in the browser with .com domain
    
    wikipedia_search(self, query):
        Search wikipedia and display the best answer for the query
        
    '''
    def mute_video(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('m')
        
    def next_video(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('shift + n')
        
    def previous_video(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('shift + p')
        
    def skip_further(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('l')
        
    def skip_back(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('j')
        
    def speed_up(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('>')
        
    def speed_down(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('<')
        
    def end_video(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('end')
        
    def start_again(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('home')
        
    def search(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('/')
        
    def fullscreen(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('f')
        
    def subtitles(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('c')
        
    def miniplayler(self):
        '''
        It's search the statement on the google search engine. Statement is given by the user as a query.

            Parameters:
                query (string): User input statement to search
                
            Input Form:
                > Search python on google

            Output:
                Search query on the google search. and open the link in the browser.
        '''
        keyboard.press_and_release('i')
    

@lru_cache()
def audio_recorder():
    '''
    Returns the sum of two decimal numbers in binary digits.

        Parameters:
            a (int): A decimal integer
            b (int): Another decimal integer

        Returns:
            binary_sum (str): Binary string of the sum of a and b
    '''
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

@lru_cache()
def file_sharing():
    '''
    Returns the sum of two decimal numbers in binary digits.

        Parameters:
            a (int): A decimal integer
            b (int): Another decimal integer

        Returns:
            binary_sum (str): Binary string of the sum of a and b
    '''
    # assinging the appropriate port value
    PORT = 8010
    # this finds the name of the computer user
    os.environ['USERPROFILE']
    
    
    # changing the directory to access the files desktop
    # with the help of os module
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),
                        'OneDrive')
    os.chdir(desktop)
    
    
    # creating a http request
    Handler = http.server.SimpleHTTPRequestHandler
    # returns, host name of the system under
    # which Python interpreter is executed
    hostname = socket.gethostname()
    
    
    # finding the IP address of the PC
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
    link = IP
    
    
    # converting the IP address into the form of a QRcode
    # with the help of pyqrcode module
    
    # converts the IP address into a Qrcode
    url = pyqrcode.create(link)
    # saves the Qrcode inform of svg
    url.svg("myqr.svg", scale=8)
    # opens the Qrcode image in the web browser
    webbrowser.open('myqr.svg')
    
    
    # Creating the HTTP request and  serving the
    # folder in the PORT 8010,and the pyqrcode is generated
    
    # continuous stream of data between client and server
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        print("Type this in your Browser", IP)
        print("or Use the QRCode")
        httpd.serve_forever()

if __name__ == '__main__':
    """
    To test the functions working.
    """
    website_control.web_search(0,"search pythonon google")
