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

def assistant_name():
	return "My name is Layla, meaning night"

"""
# basic converstaion Questions

http://iteslj.org/questions/

Do you have any pets?
What was the last book you read?
Do you like to cook?
What's your favorite food?
Are you good at cooking/swimming/etc?
Are you married or single?
Do you have brothers and sisters?
Are they older or younger than you?
Do you like baseball?
Do you live alone?
Do you live in a house or an apartment?
Have you ever lived in another country?
Have you ever met a famous person?
How do you spend your free time?
How long have you been studying English?
How old are you?
How tall are you?
Tell me about a favorite event of your adulthood.
Tell me about a favorite event of your childhood.
What are your hobbies?
What two things could you not do when you were...?
What countries have you visited?
What country are you from?
What do you do on Sundays?
What do you do? What's your job?
What do you like to do in your free time?
What hobbies do you have?
What is the nearest bus stop or train station to your house?
What is your motto?
What is your religion? (Perhaps not a good question in some situations.)
What kind of food do you like?
What kind of people do you like?
What kind of people do you not like?
What languages do you speak?
What two things could you not do when you were a child, but you can do now?
What's something you do well?
What's your address?
What's your father like?
What's your mother like?
What's your name?
What's your phone number?
What's your telephone number?
When did you start to study English?
Where are you from?
Where do you live?
Where do you live? How long have you lived there?
Where were you born?
Which sports do you like?
Who do you live with?
Who do you respect the most?
Who has had the most influence in your life?
Why did you decide to take this course?
Why do you want to learn English?
Would you like to be famous?
What do you think you will be doing five years from now?
Where do you think you'll be living five years from now?
What is your goal in life?
Are you a 'morning' or 'night' person?
When do you feel best? In the morning, afternoon, or evening?
How many cities have you lived in?
What jobs have you done?
Which do you prefer, sunrises or sunsets?
What could you do as a child that you can't do now?
Who is your next door neighbor in your home country?
What is he or she like?
Did you get along with each other?
What is the best memory of our country that you will take back home with you?
What is the worst memory of our country?
How many times did you move as a child?
Are you a task oriented person or a people oriented person?
What is the profile of the wife/husband you would meet?
What kind of woman/man would you like to marry?
"""