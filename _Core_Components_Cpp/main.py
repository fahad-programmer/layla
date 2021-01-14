import random
import datetime

def greet():
	responses = ["Hi, Sir", "Hello Sir, Its Good To Hear You", "How's Doing Man", "Hello Handsome"]
	response = random.choice(responses)
	return response

def current_date():
	date = datetime.datetime.now()
	main_date = f"{date.strftime('%d')},{date.strftime('%B')}{date.strftime('%Y')}"
	return main_date