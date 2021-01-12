import random
import datetime

cpdef char *current_time():
	now = datetime.datetime.now()
	current_time = f"Time Right Now is {now.strftime('%H:%M:%S')}"
	return current_time.encode('utf-8') 

cpdef char *assistant_name():
	name = "My name is, Layla meaning night"
	return name.encode('utf-8')


   		