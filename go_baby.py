# Importing Files to run
from _Core_Components import core_func
from work import web_blocker
# Include the modules
from threading import Thread
import os

# Change Voice number in engine component file*

if __name__ == '__main__':
    # Main Program
    # Opeing a new CMD and run a new file
    web_blocker_cmd = "start cmd /K python work\\web_blocker.py"
    # Declairing Threads
    print("Starting threads...")  # Test
    # Thread(target = os.system(web_blocker_cmd)).start() -> Still not working
    Thread(target=core_func.layla_run()).start()
