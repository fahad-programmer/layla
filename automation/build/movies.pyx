from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import glob
import time
import os

driver = webdriver.Chrome()

driver.get("https://yts.mx")



cpdef unicode get_trending_movies():
	
	"""This function takes no parameter and just simply return 4 movies that are trending on the yts"""

	cdef list divs = driver.find_elements_by_class_name('browse-movie-title')[:4]

	cdef unicode main_ret = f"Following Are The Movies That Are Trending Right Now {divs[0].text} and {divs[1].text} and {divs[2].text} and {divs[3].text}"

	driver.close()

	return main_ret

cpdef void download_movies(movie_name):
	"""This function takes in a movie name in as a parameter"""
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
	driver.close()
	time.sleep(6)	
	cdef list list_of_files = glob.glob('C:\\Users\\Dell\\Downloads\\*.torrent')
	cdef str latest_file = max(list_of_files, key=os.path.getctime)
	os.startfile(r'' + latest_file)