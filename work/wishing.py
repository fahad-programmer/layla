from datetime import datetime
import random

time = datetime.now()
# print(time) >  2020-08-09 21:19:07.071096 > %d/%m/%Y %H:%M:%S

hour = int(time.strftime('%H'))


def time_pace():
    if 0 <= hour <= 12:
        return "a m"
    else:
        return "p m"


def morning_commands():
    stat = ["increasing gradually", "decreasing"]
    morning = f"Good Morning. It's {hour} A.M. The weather in {location_of_me()} is {weather_go.city_temp} with {weather_go.city_weather}. The wind speed is {weather_go.city_wind_speed} and {random.choice(stat)}, and your exercise time will be starting in 30 minutes "

    return morning


def noon_commands():
    comm = ["Sir what you want today for your lunch", "What are you main goals today",
            "Sir Today you got a meeting at 5 P.M", "How was your breakfast Sir!",
            "Are you working today on new project or want to take on the previous one",
            "Do you want brunch or want to do lunch only today"]
    noon = random.choice(comm)

    return noon


def afternoon_commands():
    comm = ["Good Afternoon Sir!", "How was your launch today", "what would you take in dinner Sir",
            "sir do you want to know your next schedule"]
    afternoon = random.choice(comm)

    return afternoon


def evening_commands():
    comm = ["Dinner is ready Sir", "Good Evening Sir! How was your day going", "Are you going ou today or not", "Hello world hahaha just kidding sir", "Will you take a cup of coffee", "Sir its time to do exercise pf the evening"]
    evening = random.choice(comm)

    return evening

def night_commands():
    comm = ["Happy new day sir", "do you need something to eat sir", "I think so sir this project must be very important to you", "new day is up sir and you are still awake"]
    night = random.choice(comm)

    return night