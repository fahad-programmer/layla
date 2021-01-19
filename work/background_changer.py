# get current wallpaper's path
# import modules
from wallpaper import set_wallpaper
import os
import random

path = "D:\Personal\wallpaper\\"  #This is just temporary

files = os.listdir(path)
d = random.choice(files)

a = f"{path}{d}"
# set your photo
set_wallpaper(a)
