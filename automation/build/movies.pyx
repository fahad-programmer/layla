from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import glob
import time
import os
import subprocess

driver = webdriver.Edge("msedgedriver.exe")
driver.get("https://yts.mx")

cpdef str get_trending_movies():
	
	"""This function takes no parameter and just simply return 4 movies that are trending on the yts"""


	cdef list divs = driver.find_elements_by_class_name('browse-movie-title')[:4]

	main_return = f"Following Are The Movies That Are Trending Right Now {divs[0].text} and {divs[1].text} and {divs[2].text} and {divs[3].text}".encode('utf-8')

	cdef str main_ret = main_return.decode('utf-8')

	return main_ret