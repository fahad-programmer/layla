import keyboard
import time


def search(search_term) -> None:
    keyboard.press_and_release('alt+space')
    
    keyboard.write(search_term)
    keyboard.press_and_release('enter')


search('gifted')
