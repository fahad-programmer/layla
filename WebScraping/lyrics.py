import requests
from bs4 import BeautifulSoup

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


def LyricsFinder(artist_name, track_name) -> str:
    """[This Function Is Used To Generate Lyrics Of Songs Using The Lyrics Finder Site And Beautiful Soap]

            Args:
                artist_name ([str]): [The Artist Name Who Has Sung The Song]
                track_name ([str]): [The Name Of The Song That You Want Lyrics For]

            Returns:
                [type]: [This Function Returns Lyrics Of The Song Based On The Args Given Above]
            """

    artist_name = ''
    track_name = ''

    def __init__(self, query) -> None:
        self.query = query
        self.query_cleaner()

    def query_cleaner(self):
        set_query = self.query
        filter_query = set_query.replace("Find Lyrics Of", "")
        main_query = filter_query.rsplit("by")
        self.track_name = main_query[0].strip().replace(" ", '-')
        self.artist_name = main_query[1].strip().replace(" ", '-')

    def lyrics_finder(self) -> str:
        """

        :rtype: str
        """
        url = f"https://www.lyricfinder.org/lyrics/{self.artist_name}?track={self.track_name}"
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'lxml')
        tag_find = soup.select('.col-lg-6')[0].get_text()
        return tag_find





# a = LyricsFinder("Find Lyrics Of Earth by Lil Dicky")
# print(a.lyrics_finder())


