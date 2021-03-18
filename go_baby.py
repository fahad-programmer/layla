# Importing Files to run
from layla import layla
from work import web_blocker
# Include the modules
from threading import Thread
import os

# Main Program
# Opeing a new CMD and run a new file
web_blocker_cmd = os.system("start cmd /K python work\\web_blocker.py")
# Declairing Threads
print("Stating threads...")       # Test
# Thread(target = web_blocker_cmd).start() -> Still not working
Thread(target = layla.layla_run()).start()
