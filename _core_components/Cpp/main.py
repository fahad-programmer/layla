import random


def greet():
	responses = ["Hi, Sir", "Hello Sir, Its Good To Hear You", "How's Doing Man", "Hello Handsome"]
	response = random.choice(responses)
	return response