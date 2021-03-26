"""
All The Github Related Data Will Be Here Like Following

1 -> Followers Following
2 -> Number Of Repositories
3 -> Contributions
4 -> Bio

"""
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

def github_follower(username) -> str:
	url = f"https://github.com/{username}"
	try:
		req = requests.get(url, headers)
		soup = BeautifulSoup(req.content, 'lxml')
		tag_find = soup.find_all(class_='text-bold')[0]
	except Exception as e:
		pass
	return f"You Have {tag_find.get_text()} followers on github"

def github_following(username) -> str:
	url = f"https://github.com/{username}"
	try:
		req = requests.get(url, headers)
		soup = BeautifulSoup(req.content, 'lxml')
		tag_find = soup.find_all(class_='text-bold')[1]
	except Exception as e:
		pass
	return f"You Have {tag_find.get_text()} following on github"


def number_of_repo(username) -> str:
	url = f"https://github.com/{username}"
	try:
		req = requests.get(url, headers)
		soup = BeautifulSoup(req.content, 'lxml')
		tag_find = soup.find_all(class_='Counter')[0]
	except Exception as e:
		pass
	return f"You Have {tag_find.get_text()} visible repositories on github"

def github_contributions(username) -> str:
	url = f"https://github.com/{username}"
	try:
		req = requests.get(url, headers)
		soup = BeautifulSoup(req.content, 'lxml')
		tag_find = soup.find_all(class_='text-normal')[29]
	except Exception as e:
		pass
	return f"You Have {tag_find.get_text()}"

def github_contributions(username) -> str:
	url = f"https://github.com/{username}"
	try:
		req = requests.get(url, headers)
		soup = BeautifulSoup(req.content, 'lxml')
		tag_find = soup.find(class_='user-profile-bio')
	except Exception as e:
		pass
	return f"You Bio Is Following {tag_find.get_text()}"

print(github_contributions('fahad-programmer'))