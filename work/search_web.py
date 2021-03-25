import webbrowser
import sys
from layla.engine_components import speak


# Search On Internet
class search_internet:
    def __init__(self, query) -> None:
        self.query = query
        self.term = ' '.join(self.query.split()[1:-2])
        self.name = ' '.join(self.query.split()[-1:])

    def give_url(self) -> str:
        """
        Input: Name of Website
        Output: Return Str -> search url
        """
        if self.name == "youtube":
            return ("results?search_query=")
        elif self.name == "pinterest":
            return ("search/pins/?q=")
        elif self.name == "linkedin":
            return ("search/results/all/?keywords=")
        elif self.name == "tumblr" or self.name == "dailymotion":
            return ("search/")
        elif self.name == "imdb":
            return ("find?q=")
        else:
            return ("search?q=")

    def web_search(self) -> None:
        print('searching ' + self.term + " on " + self.name)
        speak('searching ' + self.term + " on " + self.name)
        webbrowser.open("https://www." + self.name + ".com/" +
                        self.give_url() + self.term)


# goog = search_internet("search python on quora")
# goog.web_search()
