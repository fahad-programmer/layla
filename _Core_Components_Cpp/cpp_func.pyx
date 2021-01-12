import datetime


cdef extern from "funcs.cpp":
     char *greet()
     char *saying_bye()
     char *age_question()

cdef extern from "datetime.cpp":
    char *current_date()

cpdef greet_main():
    return greet()

cpdef current_date_main():
    return current_date()

cpdef saying_bye_main():
    return saying_bye()

cpdef age_question_main():
    return age_question()