import datetime


cdef extern from "greet.cpp":
     char *greet()

cdef extern from "datetime.cpp":
    char *current_date()

cpdef greet_main():
    return greet()

cpdef date_time():
    return current_date()


	
	
	