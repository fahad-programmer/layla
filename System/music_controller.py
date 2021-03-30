import requests
import random
from os import listdir
from playsound import playsound
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

"""
Well the programs run fine in some conditions but there are some problems that we must take 
care off if we want this to work it correctly.

1 -> Ads In Web driver (Done)
2 -> Sometimes the driver select the channel instead of the video and i don't know why
3 -> we have to make it headless but because i use edge and can't have that imran can test it
out
4 -> i am avoiding the add video by not selecting the element with video id = 0 but soon will find a 
better way
5 -> Will have to improve the local files system soon integrate it with groove that will enable us
to also playlist

"""

internet_connection = True

def internet_connection_checker():
	url = 'https://google.com'
	timeout = 5
	try:
		request = requests.get(url)
	except (requests.ConnectionError, requests.Timeout) as Exception:
		internet_connection = False

internet_connection_checker()


def local_music():
	path = r'C:\\Users\\unexp\\Music'
	random_select = random.choice(listdir(path))
	playsound(f"{path}\\{random_select}")
	
def youtube_music():
	driver = webdriver.Edge("msedgedriver.exe")
	singers_choices = ["music", 'atif aslam', 'justin bieber', 'ed sheeran', 'drake', 'ali zafar', 'aima baig']
	driver.get(f'https://www.youtube.com/results?search_query={random.choice(singers_choices)}')
	driver.find_elements_by_id(id_='img')[random.choice([i for i in range(2, 10)])].click()
	while True:
		main_in = input('Please Enter Stop To Stop')
		if main_in == 'stop':
			driver.close()
			break

if internet_connection:
	youtube_music()
else:
	local_music()


