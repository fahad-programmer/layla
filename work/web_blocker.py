""" Website Blocker
----------------------------------------
"""
import time
from datetime import datetime as dt   
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append('../admin')
from admin import admin

# if not admin.isUserAdmin():
#         admin.runAsAdmin()     

def webblocker_run():
    hosts_path = r"C:/Windows/System32/drivers/etc/hosts"   # r is for raw string
    hosts_temp = "hosts"
    redirect = "127.0.0.1"
    web_sites_list = ["www.facebook.com", "facebook.com"]    # users can modify the list of the websites they want to block
    print("For Test")
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,22):
            print("1")
            with open(hosts_path, "r+") as file:
                content = file.read()
                for website in web_sites_list:
                    if website in content:
                        pass
                    else:
                        file.write(redirect+" "+website+"\n")
        else:
            print("2")
            with open(hosts_path, "r+") as file:
                content = file.readlines()
                file.seek(0)  # reset the pointer to the top of the text file
                for line in content:
                    # here comes the tricky line, basically we overwrite the whole file
                    if not any(website in line for website in web_sites_list):
                        file.write(line)
                    # do nothing otherwise
                file.truncate() # this line is used to delete the trailing lines (that contain DNS)
        time.sleep(5)