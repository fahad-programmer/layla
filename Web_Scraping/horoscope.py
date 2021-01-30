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


class Horoscope:

    sign_number = 0

    def __init__(self, star_sign) -> None:
        self.star_sign = star_sign
        self.sign_checker()

    def sign_checker(self):

        star_sign = self.star_sign

        if star_sign == 'aries':
            self.sign_number = 1
        elif star_sign == 'tarus':
            self.sign_number = 2
        elif star_sign == 'gemini':
            self.sign_number = 3
        elif star_sign == 'cancer':
            self.sign_number = 4
        elif star_sign == 'leo':
            self.sign_number = 5
        elif star_sign == 'virgo':
            self.sign_number = 6
        elif star_sign == 'libra':
            self.sign_number = 7
        elif star_sign == 'scorpio':
            self.sign_number = 8
        elif star_sign == 'sagittarius':
            self.sign_number = 9
        elif star_sign == 'capricon':
            self.sign_number = 10
        elif star_sign == 'aquarius':
            self.sign_number = 11
        elif star_sign == 'pisces':
            self.sign_number = 12
        else:
            return "Please Tell A Valid Star Name"

    def daily_horoscope(self) -> str:
        url = f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={self.sign_number}"
        try:
            req = requests.get(url, headers)
            soup = BeautifulSoup(req.content, 'lxml')
            global tag_find
            tag_find = soup.find('p').get_text()
        except Exception as e:
            return "Some Internal Error Occured Try Later"
        return tag_find

    def daily_tommorow(self) -> str:
        url = f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-tomorrow.aspx?sign={self.sign_number}"
        try:
            req = requests.get(url, headers)
            soup = BeautifulSoup(req.content, 'lxml')
            global tag_find
            tag_find = soup.find('p').get_text()
        except Exception as e:
            return "Some Internal Error Occured Try Later"
        return tag_find

    def weekly_horoscope(self) -> str:
        url = f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-weekly.aspx?sign={self.sign_number}"
        try:
            req = requests.get(url, headers)
            soup = BeautifulSoup(req.content, 'lxml')
            global tag_find
            tag_find = soup.find('p').get_text()
        except Exception as e:
            return "Some Internal Error Occured Try Later"
        return tag_find

    def daily_love(self) -> str:
        url = f"https://www.horoscope.com/us/horoscopes/love/horoscope-love-daily-today.aspx?sign={self.sign_number}"
        try:
            req = requests.get(url, headers)
            soup = BeautifulSoup(req.content, 'lxml')
            global tag_find
            tag_find = soup.find('p').get_text()
        except Exception as e:
            return "Some Internal Error Occured Try Later"
        return tag_find

    def tomorrow_love(self) -> str:
        url = f"https://www.horoscope.com/us/horoscopes/love/horoscope-love-daily-tomorrow.aspx?sign={self.sign_number}"
        try:
            req = requests.get(url, headers)
            soup = BeautifulSoup(req.content, 'lxml')
            global tag_find
            tag_find = soup.find('p').get_text()
        except Exception as e:
            return "Some Internal Error Occured Try Later"
        return tag_find

    def love_weekly(self) -> str:
        url = f"https://www.horoscope.com/us/horoscopes/love/horoscope-love-weekly-single.aspx?sign={self.sign_number}"
        try:
            req = requests.get(url, headers)
            soup = BeautifulSoup(req.content, 'lxml')
            global tag_find
            tag_find = soup.find('p').get_text()
        except Exception as e:
            return "Some Internal Error Occured Try Later"
        return tag_find
