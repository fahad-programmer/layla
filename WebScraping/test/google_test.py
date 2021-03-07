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
                print("1")
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
                print("2")
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
                print("3")
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
                print("4")
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
                print("5")
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
                print(ans.replace(". ", ".\n"))
                print("6")
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
                print("7")
                return
            else:
                pass
        except:
            pass
        # 13
        try:
            ans = soup.find('input', {'jsname': 'fPLMtf'}).get('value') # Give value after converstion like 1 year to weaks
            if len(ans) >= 1:
                print(ans)
                print("13")
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
                print("8")
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
                print('9')
                return
            else:
                pass
        except:
            pass
        # 10
        try:
            divs = soup.select("div.LwV4sf") # Founder's
            ans = self.founder_loop(divs)
            if len(ans) >=1:
                print("10")
                return
            else:
                pass
        except:
            pass
        # 11
        try:
            divs = soup.select("div.WGwSK") # Movies List
            ans = self.founder_loop(divs)
            if len(ans) >=1:
                print(11)
                return
            else:
                pass
        except:
            pass
        # 12
        try:
            divs = soup.select("div.VL3Jfb") # IP answer
            ans = self.for_loop(divs)
            if len(ans) >=1:
                print(ans)
                print("12")
                return
            else:
                pass
        except:
            pass
        # 14
        try:
            divs = soup.select("div.kno-rdesc") # Wikipedia answer
            ans = self.for_loop(divs)
            if len(ans) >=1:
                print(ans)
                print("14")
                return
            else:
                pass
        except:
            pass
        try:
            print("Nothing Found!")
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
                print(h3.get_text(), "\n")
        for div in divs:
            try:
                results = div.select("ol")
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
                results = div.select("ul")
                # Check if we have found a result
                if (len(results) >= 1):

                    # Print the title
                    h3 = results[0]
                    return(h3.get_text())
                else:pass
            except:pass
    
    def related_queries(self, soup) -> str:
        divs = soup.select("div.related-question-pair")
        for div in divs:
            results = div.select("div")

            # Check if we have found a result
            if (len(results) >= 1):

                # Print the title
                h3 = results[0]
                print(h3.get_text())
    
    def founder_loop(self, divs):
        for div in divs:
            results = div.select("div")

            # Check if we have found a result
            if (len(results) >= 1):

                # Print the title
                h3 = results[0]
                print(h3.get_text(separator=' '))
        return(h3.get_text())
    
    
    
    
    
    
# google_results("Does Russia have 2 capitals")
# google_results("Who was Elsa Where did she live?")
# google_results("american president")
# google_results("how to delete instagram account")
# google_results("Einstien Quotes")
# google_results("popular scientists")
# google_results("apple founders")
# google_results("marvel movies")
# google_results("how can i publish my book")
# google_results("How old is Joe Biden")
google_results("How many Tesla shares does Elon Musk own")
