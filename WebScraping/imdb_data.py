from bs4 import BeautifulSoup
import requests

#Showing that we are legit and avoiding being blocked from the site
headers = {
    'Access-Control-Allow-Origin':
    '*',
    'Access-Control-Allow-Methods':
    'GET',
    'Access-Control-Allow-Headers':
    'Content-Type',
    'Access-Control-Max-Age':
    '3600',
    'User-Agent':
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}


class imdb_movies:

    def top_picks(self) -> str:
        url = "https://www.imdb.com/"
        try:
            req = requests.get(url, headers)
            soup = BeautifulSoup(req.content, 'lxml')
            global tag_find
            tag_find = soup.find_all['div', "ipc-title__description"]
        except Exception:
            return "Some Internal Error Occured Try Later"
        return tag_find

main = imdb_movies()
print(main.top_picks())

