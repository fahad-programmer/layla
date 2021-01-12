import datetime


cdef extern from "greet.cpp":
     char *greet()

cdef extern from "datetime.cpp":
    char *current_date()

cpdef greet_main():
    return greet()

cpdef date_time():
    return current_date()

cpdef char *current_date_now():
    date = datetime.datetime.now()
    main_date = f"{date.strftime('%d')},{date.strftime('%B')}{date.strftime('%Y')}"
    return main_date.encode('utf-8')
	
	
	