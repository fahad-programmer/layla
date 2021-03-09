from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import glob
import time
import os
import subprocess


driver = webdriver.Edge("msedgedriver.exe")
driver.get("https://yts.mx")


def get_trending_movies() -> str:

	"""This function takes no parameter and just simply return 4 movies that are trending on the yts"""

	try:
		divs = driver.find_elements_by_class_name('browse-movie-title')[:4]
	except Exception as e:
		pass

	main_return = f"Following Are The Movies That Are Trending Right Now {divs[0].text} and {divs[1].text} and {divs[2].text} and {divs[3].text}"

	return main_return

def download_movies(movie_name) -> None:

	"""This function takes in a movie name in as a parameter"""


	def opening_the_file():
		list_of_files = glob.glob(r'C:\\Users\\Dell\\Downloads\\*.torrent')
		latest_file = max(list_of_files, key=os.path.getctime)
		os.startfile(r'' + latest_file)

	try:
		search_box = driver.find_element_by_id('quick-search-input')
		search_box.send_keys(movie_name)
		driver.implicitly_wait(5)
		item_selected = driver.find_element_by_class_name('ac-item-selected')
		link = item_selected.find_element_by_tag_name('a')
		link.click()
		driver.implicitly_wait(10)
		download_button = driver.find_element_by_class_name('torrent-modal-download')
		download_button.click()
		main_download = driver.find_element_by_class_name('download-torrent')
		main_download.click()
		time.sleep(6)
		opening_the_file()

	except Exception as e:
		print(e)

	



	return None

download_movies("iron man")
