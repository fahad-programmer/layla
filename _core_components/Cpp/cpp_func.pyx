import random

cdef extern from "greet.cpp":
     char *greet()

cpdef greet_main():
    return greet()

cpdef char *greet_h():
    cdef list responses = ["Hi, Sir", "Hello Sir, Its Good To Hear You", "How's Doing Man", "Hello Handsome"]
    response = random.choice(responses)
    return response.encode('utf-8')