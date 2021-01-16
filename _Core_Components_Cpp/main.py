import random
import datetime
import webbrowser


def greet():
    responses = [
        "Hi, Sir", "Hello Sir, Its Good To Hear You", "How's Doing Man",
        "Hello Handsome"
    ]
    response = random.choice(responses)
    return response


def current_date():
    date = datetime.datetime.now()
    main_date = f"{date.strftime('%d')},{date.strftime('%B')}{date.strftime('%Y')}"
    return main_date


def current_time_main():
    now = datetime.datetime.now()
    main_time = f"Time Right Now is {now.strftime('%H:%M:%S')}"
    return main_time


def addition_main(query):
    string_numbers = [int(s) for s in query.split() if s.isdigit()]
    add_numbers = sum(string_numbers)
    return_answer = f"The Result Of The Addition Is {add_numbers}"
    return return_answer