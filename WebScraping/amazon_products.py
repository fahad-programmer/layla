# importing libraries
from bs4 import BeautifulSoup
import requests
  
def main(url):
    # openning our output file in append mode
  
    # specifying user agent, You can use other user agents
    # available on the internet
    HEADERS = ({'Access-Control-Allow-Origin':
    '*',
    'Access-Control-Allow-Methods':
    'GET',
    'Access-Control-Allow-Headers':
    'Content-Type',
    'Access-Control-Max-Age':
    '3600',
    'User-Agent':
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
  
    # Making the HTTP Request
    webpage = requests.get(url, headers=HEADERS)
  
    # Creating the Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")
  
    # retreiving product title
    try:
        # Outer Tag Object
        title = soup.find("span", 
                          attrs={"id": 'productTitle'})
  
        # Inner NavigableString Object
        title_value = title.string
  
        # Title as a string value
        title_string = title_value.strip().replace(',', '')
  
    except AttributeError:
        title_string = "NA"
    print("product Title = ", title_string)
  
    # saving the title in the file
    print(f"{title_string},")
  
    # retreiving price
    try:
        price = soup.find(
            "span", attrs={'id': 'priceblock_ourprice'}).string.strip().replace(',', '')
        # we are omitting unnecessary spaces
        # and commas form our string
    except AttributeError:
        price = "NA"
    print("Products price = ", price)
  
    # saving
    print(f"{price},")
  
    # retreiving product rating
    try:
        rating = soup.find("i", attrs={
                           'class': 'a-icon a-icon-star a-star-4-5'}).string.strip().replace(',', '')
  
    except AttributeError:
  
        try:
            rating = soup.find(
                "span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
        except Exception:
            rating = "NA"
    print("Overall rating = ", rating)
  
    print(f"{rating},")
  
    try:
        review_count = soup.find(
            "span", attrs={'id': 'acrCustomerReviewText'}).string.strip().replace(',', '')
  
    except AttributeError:
        review_count = "NA"
    print("Total reviews = ", review_count)
    print(f"{review_count},")
  
    # print availiblility status
    try:
        available = soup.find("div", attrs={'id': 'availability'})
        available = available.find("span").string.strip().replace(',', '')
  
    except AttributeError:
        available = "NA"
    print("Availability = ", available)
  
    # saving the availibility and closing the line
    print(f"{available},\n")
  
  
if __name__ == '__main__':
  # openning our url file to access URLs
    links = input("paste the url of product: ")
    main(links)