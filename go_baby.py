from admin import admin

if not admin.isUserAdmin():
        admin.runAsAdmin()

from layla import layla
from work import web_blocker
from threading import Thread


if __name__ == '__main__':
        layla.layla_run()
        
        # Trying to run both statements at the same time
        # >> python go_baby.py runlayla
        
        
        # def runlayla():
                # Thread(target = layla.layla_run).start()
                # Thread(target = web_blocker.webblocker_run).start()
