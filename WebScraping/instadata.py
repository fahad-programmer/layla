from bs4 import BeautifulSoup
import urllib.request


class insta_results:
    
    def __init__(self, query):
        self.query = query
        link = self.query.replace(" ", "+")
        url = f'https://instagram.com/'

        # Perform the request
        request = urllib.request.Request(url)

        # Set a normal User Agent header, otherwise Google will block the request.
        request.add_header(
            'User-Agent',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        )
        raw_response = urllib.request.urlopen(request).read()

        # Read the repsonse as a utf-8 string
        html = raw_response.decode("utf-8")
        # The code to get the html contents here.

        soup = BeautifulSoup(html, 'lxml')
        print(soup)
        # self.scrap_capital(soup)
        
    def scrap_capital(self, soup) -> str:

        # Find all the search result divs
        # 1
        try:
            divs = soup.select("div.o64aR")  # One Word Answer > a
            ans = self.for_loop(divs)
            if len(ans) >= 1:
                print(ans)
                return
            else:
                pass
        except:
            pass
    
    def for_loop(self, divs):
        for div in divs:
            # Search for a h3 tag
            try:
                results = div.select("div")

                # Check if we have found a result
                if (len(results) >= 1):

                    # Print the title
                    h3 = results[0]
                    return (h3.get_text())
                else:
                    pass
            except:
                pass
            try:
                results = div.select("span")

                # Check if we have found a result
                if (len(results) >= 1):

                    # Print the title
                    h3 = results[0]
                    return (h3.get_text())
                else:
                    pass
            except:
                pass
            try:
                results = div.select("a")

                # Check if we have found a result
                if (len(results) >= 1):

                    # Print the title
                    h3 = results[0]
                    return (h3.get_text())
                else:
                    pass
            except:
                pass
            
insta_results("do i have any messages")