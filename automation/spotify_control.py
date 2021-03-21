import keyboard
from sys import platform as _platform
import time

class spotify:
    
    def __init__(self, query):
        self.query = query
        self.functions_per()
    
    def functions_per(self):
        if _platform == "linux" or _platform == "linux2":
            self.win_func()
        elif _platform == "darwin":
            self.win_func()
        elif _platform == "win32":
            self.win_func()
        elif _platform == "win64":
            self.mac_func()
    
    def mac_func(self):
        if "new playlist" in self.query:
            keyboard.press_and_release('cmd + n')
        elif "play" in self.query or "pause" in self.query:
            keyboard.press_and_release('space')
        elif "repeat" in self.query:
            keyboard.press_and_release('cmd + r')
        elif "shuffle" in self.query:
            keyboard.press_and_release('cmd + s')
        elif "next" in self.query:
            keyboard.press_and_release('ctrl + cmd + right')
        elif "previous" in self.query:
            keyboard.press_and_release('ctrl + cmd + left')
        elif "volume up" in self.query:
            keyboard.press_and_release('cmd + up')
        elif "volume down" in self.query:
            keyboard.press_and_release('cmd + down')
        elif "mute" in self.query:
            keyboard.press_and_release('cmd + shift + down')
        elif "max volume" in self.query:
            keyboard.press_and_release('cmd + shift + up')
        elif "search" in self.query:
            keyboard.press_and_release('cmd + l')
    
    def win_func(self):
        if "new playlist" in self.query:
            keyboard.press_and_release('ctrl + n')
        elif "play" in self.query or "pause" in self.query:
            keyboard.press_and_release('space')
        elif "repeat" in self.query:
            keyboard.press_and_release('ctrl + r')
        elif "shuffle" in self.query:
            keyboard.press_and_release('ctrl + s')
        elif "next" in self.query:
            keyboard.press_and_release('ctrl +  right')
        elif "previous" in self.query:
            keyboard.press_and_release('ctrl +  left')
        elif "volume up" in self.query:
            keyboard.press_and_release('ctrl + up')
        elif "volume down" in self.query:
            keyboard.press_and_release('ctrl + down')
        elif "mute" in self.query:
            keyboard.press_and_release('ctrl + shift + down')
        elif "max volume" in self.query:
            keyboard.press_and_release('ctrl + shift + up')
        elif "search" in self.query:
            keyboard.press_and_release('ctrl + l')
            
time.sleep(4)
spotify("spotify play")