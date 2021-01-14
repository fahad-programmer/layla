# This file is made to scrap all the data from the websites using Beautiful Soup Module, We are going to scrap every fucking information from the internet.
import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions/58015534/how-to-select-all-text-in-a-web-page-using-python"
req = requests.get(url)
soup_object = BeautifulSoup(req.text, "html.parser")
for question_content in soup_object.find_all("div", "post-text"):
    print(question_content.text)
for comment_content in soup_object.find_all("span", "comment-copy"):
    print(comment_content.text)