import keyboard
import time
import sys
sys.path.append('../layla/')
from engine_components import take_command


def search() -> None:
    query = input("Please Tell What You Want To Search")
    keyboard.press_and_release('windows')
    time.sleep(2)
    keyboard.write(query)
    while True:
        query = take_command().lower()
        if query == 'move down':
            keyboard.press_and_release('down')
        elif query == 'move up':
            keyboard.press_and_release('up')
        elif query == 'launch':
            keyboard.press_and_release('enter')
            break
        else:
            print("something Occured")


search()
