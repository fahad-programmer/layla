# This file is made to scrap all the data from the websites using Beautiful Soup Module, We are going to scrap every fucking information from the internet.
import requests
from bs4 import BeautifulSoup

def scrap_answers(query):
    query = query.replace(" ", "%20")
    url = "https://www.google.com/search?q=" + query
    print(url)
    res  = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.content, "html.parser")
    data = soup.find('span', class_="hgKElc")
    print(data.text.strip())
    
scrap_answers("At what age do most people in your country get married?")