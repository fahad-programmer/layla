import re
from bs4 import BeautifulSoup
import requests

header = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
}


def scrap_capital(query):
    query = query.replace(" ", "+")
    url = f'https://google.com/search?q={query}'

    # Perform the request
    request = requests.get(url, header)

    # Set a normal User Agent header, otherwise Google will block the request.

    # The code to get the html contents here.

    soup = BeautifulSoup(request.content, 'lxml')
    print(soup)

    # Find all the search result divs
    # divs = soup.select("div.Z0LcW")       # One Word Answer > a
    # divs = soup.select("div.kno-rdesc")     # Wikipedia answer
    # divs = soup.select("div.LGOjhe")        # Info Box Answer
    # divs = soup.select("div.c4bQHf")        # population
    # divs = soup.select("div.related-question-pair") # Related Queries
    # divs = soup.select("div.sL6Rbf")      # Local Time
    # divs = soup.select("div.dAassd")      # Founders
    # divs = soup.select("div.LwV4sf")      # Founder's 2
    # divs = soup.select("div.HwtpBd")      # Answer in one word and below is explainantion
    # divs = soup.select("div.di3YZe")        # List data > div to get the heading, li to get the list
    # divs = soup.select("div.lMmzdb")  # Distance between two places > div
    divs = soup.select(
        "div.vk_bk"
    )  # Distance between two countries or two cities in diffrent countries > div
    for div in divs:
        # Search for a h3 tag
        # results = div.select("a")
        # results = div.select("span")
        # results = div.select("li")
        results = div.select("div")

        # Check if we have found a result
        if (len(results) >= 1):

            # Print the title
            h3 = results[0]
            print(h3.get_text())


# scrap_capital("what is the capital of russia")
scrap_capital("what is distance between new york and moscow in km")
