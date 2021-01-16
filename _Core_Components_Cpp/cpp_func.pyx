import datetime
from libcpp.string cimport string
from functools import reduce
import operator
import datetime

cdef extern from "functions/funcs.cpp":
     char *greet()
     char *saying_bye()
     char *age_question()
     char *saying_thanks()

cdef extern from  "functions/system_function.cpp":
    void open_programs(string query)
    void system_information()


cdef extern from "functions/datetime.cpp":
    char *current_date()

cpdef greet_main():
    return greet()

cpdef current_date_main():
    return current_date()

cpdef saying_bye_main():
    return saying_bye()

cpdef age_question_main():
    return age_question()

cpdef string addition(query):
    cdef list string_numbers = [int(s) for s in query.split() if s.isdigit()]
    cdef int add_numbers = sum(string_numbers)
    cdef string return_answer = f"The Result Of The Addition Is {add_numbers}".encode('UTF-8')
    return return_answer


cpdef saying_thanks_main():
    return saying_thanks()

cpdef string subtract(query):
    cdef list string_numbers = [int(s) for s in query.split() if s.isdigit()]
    cdef int subtract_numbers = reduce(operator.sub, string_numbers)
    cdef string return_answer = f"The Result Of The Subtraction is {subtract_numbers}".encode('UTF-8')
    return return_answer 

cpdef string divide(query):
    cdef double string_numbers_1 = [int(s) for s in query.split() if s.isdigit()][0]
    cdef double string_numbers_2 = [int(s) for s in query.split() if s.isdigit()][1]
    cdef double divide_numbers = string_numbers_1 / string_numbers_2
    cdef string return_answer = f"The Result Of The Calculation Is {divide_numbers}".encode('UTF-8')
    return return_answer

cpdef string multiply(query):
    cdef list string_numbers = [int(s) for s in query.split() if s.isdigit()]
    cdef int multiply_numbers = reduce(operator.mul, string_numbers)
    cdef string return_answer = f"The Result Of The Calculation Is {multiply_numbers}".encode('UTF-8')
    return return_answer


cpdef string current_time():
    cdef string now = datetime.datetime.now()
    cdef string current_time_main = f"Time Right Now is {now.strftime('%H:%M:%S')}".encode('UTf-8')
    return current_time_main


cpdef string assistant_name():
    cdef string name = "My name is, Layla meaning night".encode('UTF-8')
    return name
    
cpdef system_info():
    return system_information()

cpdef open_system_programs(query):
    query = query.replace("open ", "")
    cdef string main_return = query.encode('UTF-8')
    return open_programs(main_return)
    