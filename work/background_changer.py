# # get current wallpaper's path
# # import modules
# from wallpaper import set_wallpaper
# import os
# import random

# path = "D:\\Personal\\wallpaper\\"  #This is just temporary


# def background_change():
#     files = os.listdir(path)
#     d = random.choice(files)

#     a = f"{path}{d}"
#     # set your photo
#     return set_wallpaper(a)

import requests
import os
import datetime
import time
from random import randrange
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from wallpaper import set_wallpaper

# set a path for downloaded image to be saved to
wallpaper_path = os.environ['HOMEPATH'] + "/daily_image.png"
# initialize the list of URLs and append websites for the wallpaper
wallpaper_urls = []
wallpaper_urls.append("https://unsplash.com/wallpapers/screen/1920x1080")
wallpaper_urls.append("https://wallpaperscraft.com/all/1920x1080")

def updated_today(file_path):
    """Return whether wallpaper_path has been updated today."""
    # if downloaded wallpaper exists
    if os.path.exists(wallpaper_path):     
        # query os module for the last modified time of the file
        last_mod_time = os.path.getmtime(file_path) 
        # convert last_mod_time to a date format
        last_mod_date = datetime.datetime.fromtimestamp(last_mod_time)
        # return true if the wallpaper was updated today
        return last_mod_date.date() == datetime.datetime.now().date() 
    else:
        # if file doesn't exist, wallpaper has never been updated
        return False
    
def get_page(url):
    """Return full source code of provided url."""
    try:
        # get the code and save it as text 
        web_page_contents = requests.get(url).text
    except:
        web_page_contents = None
    return web_page_contents

def find_rand_image(html_content):
    """ Return a random image URL"""
    images = []
    # BeautifulSoup allows for easy parsing of HTML content
    html_tree = BeautifulSoup(html_content, features='html.parser') 
    # iterate over every wallpaper image
    for attribute in html_tree.findAll('img'): 
        # use a try-except block in case an img tag isn't properly formatted
        try: 
            # svgs aren't supported for Mac wallpaper
            if "svg" not in attribute['src']: 
                images.append(attribute['src'])
        except:
            # if image doesn't have a src attribute, move on to the next one
            pass 
    # grab a random image URL from the list
    random_num = randrange(0,len(images)) 
    return images[random_num]

def download_image(image_url):
    """Rename current wallpaper and download new one to the wallpaper_path.""" 
    # rename file so OS will realize the background changed
    if os.path.exists(wallpaper_path):   
        os.rename(wallpaper_path, wallpaper_path + ".old") 
    f = open(wallpaper_path,'wb')
    # use requests.get.content since we want the data to be saved as-is
    f.write(requests.get(image_url).content) 
    f.close()
    
# def set_desktop_image():
#     """ Tell OS where to look for old background and point the OS to new path."""
#     if os.path.exists(wallpaper_path + ".old"): 
#         # point to this .old filepath for the wallpaper
#         app('Finder').desktop_picture.set(mactypes.File(WALLPAPER_PATH + ".old")) 
#     # trigger OS to notice a new path so it refreshes the desktop background
#     app('Finder').desktop_picture.set(mactypes.File(WALLPAPER_PATH))

if not updated_today(wallpaper_path):
    # randomly select one of the URLs provided for wallpapers
    random_wallpaper_url = randrange(0,len(wallpaper_urls)) 
    wallpaper_url = wallpaper_urls[random_wallpaper_url]
    # get the source code of the wallpaper URL
    page_contents = get_page(wallpaper_url) 
    # if web request didn't fail
    if page_contents != None:
        # select a random image URL from the page
        random_image = find_rand_image(page_contents) 
        download_image(urljoin(wallpaper_url, random_image))
        print("Setting image to " + urljoin(wallpaper_url, random_image)) 
        # update desktop background
        # set_desktop_image()