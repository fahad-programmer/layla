from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge("msedgedriver.exe")
driver.get("https://yts.mx")


def get_trending_movies():
    divs = driver.find_elements_by_class_name('browse-movie-title')[:3]
    for div in divs:
        print(div.text)
