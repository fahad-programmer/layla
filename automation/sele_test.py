from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

# executor_url = driver.command_executor._url
# session_id = driver.session_id

driver = webdriver.Firefox()  #python

url = driver.command_executor._url       #"http://127.0.0.1:60622/hub"
session_id = driver.session_id            #'4e167f26-dc1d-4f51-a207-f761eaf73c31'

driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.close()   # this prevents the dummy browser
driver.session_id = session_id

driver.get("http://www.instagram.com")