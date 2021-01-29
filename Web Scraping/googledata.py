from bs4 import BeautifulSoup
import urllib.request

class google_results:

    def __init__(self, query):
        self.query = query
        link = self.query.replace(" ", "+")
        url = f'https://google.com/search?q={link}'

        # Perform the request
        request = urllib.request.Request(url)
    
        # Set a normal User Agent header, otherwise Google will block the request.
        request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
        raw_response = urllib.request.urlopen(request).read()

        # Read the repsonse as a utf-8 string
        html = raw_response.decode("utf-8")
        # The code to get the html contents here.

        soup = BeautifulSoup(html, 'lxml')
        self.scrap_capital(soup)
        print("\n\nRelated Queries: ")
        self.related_queries(soup)
    
    def scrap_capital(self, soup) -> str:

        # Find all the search result divs
        # 1
        try:
            divs = soup.select("div.Z0LcW") # One Word Answer > a
            ans = self.for_loop(divs)
            if len(ans) >=1:
                print(ans)
                return
            else:
                pass
        except:
            pass
        # 2
        try:
            divs = soup.select("div.HwtpBd") # Answer in one word and below is explainantion > a
            ans = self.for_loop(divs)
            if len(ans) >=1:
                print(ans)
                return
            else:
                pass
        except:
            pass
        # 3
        try:
            divs = soup.select("div.LGOjhe") # Info Box Answer > span
            ans = self.for_loop(divs)
            if len(ans) >=1:
                print(ans)
                return
            else:
                pass
        except:
            pass
        # 4
        try:
            divs = soup.select("div.c4bQHf") # population
            ans = self.for_loop(divs)
            if len(ans) >=1:
                print(ans)
                return
            else:
                pass
        except:
            pass
        # 5
        try:
            divs = soup.select("div.sL6Rbf") # Local Time
            ans = self.for_loop(divs)
            if len(ans) >=1:
                print(ans)
                return
            else:
                pass
        except:
            pass
        # 6
        try:
            divs = soup.select("div.di3YZe") # List data > divto get the heading, li to get the list
            ans = self.list_loop(divs)
            if len(ans) >=1:
                print(ans)
                return
            else:
                pass
        except:
            pass
        # 7
        try:
            divs = soup.select("div.lMmzdb") # Distance between two places > div
            ans = self.for_loop(divs)
            if len(ans) >=1:
                print(ans)
                return
            else:
                pass
        except:
            pass
        # 8
        try:
            divs = soup.select("div.vk_c") # Distance between two countries or two cities in diffrent countries > div
            ans = self.for_loop(divs)
            if len(ans) >=1:
                print(ans)
                return
            else:
                pass
        except:
            pass
        # 9
        try:
            divs = soup.select("div.YwqY0") # Quotes
            ans = self.for_loop(divs)
            if len(ans) >=1:
                print(ans)
                return
            else:
                pass
        except:
            pass
        # 10
        try:
            divs = soup.select("div.dAassd") # Founders
            ans = self.for_loop(divs)
            if len(ans) >=1:
                print(ans)
                return
            else:
                pass
        except:
            pass
        # 11
        try:
            divs = soup.select("div.LwV4sf") # Founder's 2
            ans = self.for_loop(divs)
            if len(ans) >=1:
                print(ans)
                return
            else:
                pass
        except:
            pass
        # 12
        try:
            divs = soup.select("div.dAassd") # Movies List
            ans = self.for_loop(divs)
            if len(ans) >=1:
                print(ans)
                return
            else:
                pass
        except:
            pass
        # 13
        try:
            divs = soup.select("div.kno-rdesc") # Wikipedia answer
            ans = self.for_loop(divs)
            if len(ans) >=1:
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
                    return(h3.get_text())
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
                    return(h3.get_text())
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
                    return(h3.get_text())
                else:
                    pass
            except:
                pass
    
    def list_loop(self, divs):
        for div in divs:
            results = div.select("div")

            # Check if we have found a result
            if (len(results) >= 1):

                # Print the title
                h3 = results[0]
                print(h3.get_text())
        i = 0
        for div in divs:
            results = div.select("ol")
            # Check if we have found a result
            if (len(results) >= 1):

                # Print the title
                h3 = results[0]
                return(h3.get_text())
    
    def related_queries(self, soup) -> str:
        divs = soup.select("div.related-question-pair")
        for div in divs:
            results = div.select("div")

            # Check if we have found a result
            if (len(results) >= 1):

                # Print the title
                h3 = results[0]
                print(h3.get_text())
            
# google_results("Does Russia have 2 capitals")
# google_results("Who was Elsa Where did she live?")
# google_results("american president")
# google_results("how to delete instagram account")
google_results("Einstien Quotes")
