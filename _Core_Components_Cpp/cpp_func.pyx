import datetime
from libcpp.string cimport string
from functools import reduce
import operator
import datetime
import re


cdef extern from "functions/funcs.cpp":
     char *greet()
     char *saying_bye()
     char *age_question()
     char *saying_thanks()

cdef extern from  "functions/system_function.cpp":
    void open_programs(string query)
    void system_information()

cdef extern from "functions/maths_func.cpp":
    double sqrt_number(int main_num)
    double sin_number(double main_num)
    double cos_number(double main_num)
    double tan_number(double main_num)
    int round_number(double main_num)
    double log_number(double main_num)

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
    cdef list string_numbers = re.findall(r"[-+]?\d*\.\d|\d+", query)
    cdef list main_list = list(map(int, string_numbers))
    cdef double add_numbers = sum(main_list)
    cdef string return_answer = f"The Result Of The Addition Is {add_numbers}".encode('UTF-8')
    return return_answer


cpdef saying_thanks_main():
    return saying_thanks()

cpdef string subtract(query):
    cdef list string_numbers = re.findall(r"[-+]?\d*\.\d|\d+", query)
    cdef list main_list = list(map(int, string_numbers))
    cdef double subtract_numbers = reduce(operator.sub, main_list)
    cdef string return_answer = f"The Result Of The Subtraction is {subtract_numbers}".encode('UTF-8')
    return return_answer 

cpdef string divide(query):
    cdef double string_numbers_1 = [int(s) for s in query.split() if s.isdigit()][0]
    cdef double string_numbers_2 = [int(s) for s in query.split() if s.isdigit()][1]
    cdef double divide_numbers = string_numbers_1 / string_numbers_2
    cdef string return_answer = f"The Result Of The Calculation Is {divide_numbers}".encode('UTF-8')
    return return_answer

cpdef string multiply(query):
    cdef list string_numbers = re.findall(r"[-+]?\d*\.\d|\d+", query)
    cdef list main_list = list(map(int, string_numbers))
    cdef double multiply_numbers = reduce(operator.mul, main_list)
    cdef string return_answer = f"The Result Of The Calculation Is {multiply_numbers}".encode('UTF-8')
    return return_answer


cpdef string current_time():
    now = datetime.datetime.now()
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

cpdef maths_func(query):
    cdef double main_num = float(re.findall(r"[-+]?\d*\.\d|\d+", query)[0])
    cdef string main_return = ""
    cdef int main_int = 0
    cdef double int_main = 0.0
    if "log" in query:
        int_main = log_number(main_num)
        main_return = f"The Log Of {main_num} Is {int_main}".encode('UTF-8')
        return main_return 
    elif "sin" in query:
        int_main = sin_number(main_num)
        main_return = f"The Sin Of {main_num} Is {int_main}".encode('UTF-8')
        return main_return
    elif "cos" in query:
        int_main = cos_number(main_num)
        main_return = f"The Cos Of {main_num} Is {int_main}".encode('UTF-8')
        return main_return
    elif "tan" in query:
        int_main = tan_number(main_num)
        main_return = f"The Tan of {main_num} Is {int_main}".encode('UTF-8')
        return main_return
    elif "square root" in query:
        int_main = sqrt_number(int(main_num))
        main_return = f"The Square Root Of {main_num} Is {int_main}".encode('UTF-8')
        return main_return
    elif "round off" in query:
        main_int = round_number(main_num)
        main_return = f"After Rounding Off The Number {main_num} The Result Is {main_int}".encode('UTF-8')
        return main_return
    else:
        return "Some Internal Error Occured".encode('UTF-8')